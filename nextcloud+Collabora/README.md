# 在Debian12上安装Nextcloud为局域网用户提供服务

本次 Nextcloud 的安装方法参考 [LinuxStory](https://zhuanlan.zhihu.com/p/651099247)。当然，也可以通过 Docker 进行安装，但我并不推荐这种方式。使用 Docker 安装 Nextcloud 的使用体验会比较差，例如进入设置页面或添加用户时可能需要很长时间等待。

请注意，本笔记中的所有命令都是以 root 账号执行的。如果你使用非 root 用户，请确保在命令前添加`sudo`。



## 版本说明

- onlyoffice版本参考下面的docker方法安装写说明时最新版本是version 7.2
- mariadb版本为10.11.5
- Nextcloud Hub 5 (27.0.2)



## 常规方式安装



### 安装Mariadb

```bash
curl -o /etc/apt/keyrings/mariadb-keyring.pgp 'https://mariadb.org/mariadb_release_signing_key.pgp'

# 写入软件源信息
nano /etc/apt/sources.list.d/mariadb.sources
--------------
# MariaDB 10.11 repository list - created 2023-09-01 05:38 UTC
# https://mariadb.org/download/
X-Repolib-Name: MariaDB
Types: deb
# deb.mariadb.org is a dynamic mirror if your preferred mirror goes offline. See https://mariadb.org/mirrorbits/ for details.
# URIs: https://deb.mariadb.org/10.11/debian
URIs: https://mirrors.aliyun.com/mariadb/repo/10.11/debian
Suites: bookworm
Components: main
Signed-By: /etc/apt/keyrings/mariadb-keyring.pgp
--------------

# 更新Debian 12软件包
apt update
apt upgrade

# 安装mariadb
apt install mariadb-server

# 初始化数据库
mysql_secure_installation

# 为NextCloud创建新数据库，注意修改your_password为你实际所需的密码。
mysql -u root -p

CREATE DATABASE nextcloud;
GRANT ALL ON nextcloud.* TO 'nextclouduser'@'localhost' IDENTIFIED BY 'your_password';
FLUSH PRIVILEGES;
EXIT;
```




### 安装Nextcloud所需软件

```bash
# 安装Apache Web服务器
apt install apache2

# 安装PHP和所需扩展
apt install php libapache2-mod-php php-mysql php-common php-gd php-xml php-mbstring php-zip php-curl php-intl

# 配置Apache以供Nextcloud使用，路径/var/www/html/nextcloud/是可以自定义的，修改成你想指定的位置即可，例如我在实际搭建中就将位置修改为通过nfs挂载的一个目录中。your_domain_or_IP_address修改为服务器本机的地址。
nano /etc/apache2/sites-available/nextcloud.conf

--------------
<VirtualHost *:80>
    ServerAdmin admin@example.com
    DocumentRoot /var/www/html/nextcloud/
    ServerName your_domain_or_IP_address

    <Directory /var/www/html/nextcloud/>
        Options +FollowSymlinks
        AllowOverride All
        Require all granted
        <IfModule mod_dav.c>
            Dav off
        </IfModule>
        SetEnv HOME /var/www/html/nextcloud/
        SetEnv HTTP_HOME /var/www/html/nextcloud/
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
--------------

# 启用Nextcloud Apache配置文件如果重启错误。
ln -s /etc/apache2/sites-available/nextcloud.conf /etc/apache2/sites-enabled/
a2enmod headers rewrite env dir mime

# 检查配置文件有无问题，如果显示 Syntax OK 即可，--no-page -l不知道有什么作用，应该不加也行。
systemctl restart apache2 --no-page -l
```



### **下载并提取Nextcloud**

```bash
# 下载最新版本的Nextcloud，写笔记的时候最新版本为27.0.2
wget https://download.nextcloud.com/server/releases/latest.tar.bz2

# 提取下载的存档
tar xvf latest.tar.bz2

# 将提取的文件移动到Apache文档根目录，路径是可以自定义的，与/etc/apache2/sites-available/nextcloud.conf上指定的路径一致
mv nextcloud /var/www/html/

# 创建一个数据目录
mkdir -p /var/www/html/nextcloud/data

# 配置正确权限
chown -R www-data:www-data /var/www/html/nextcloud/
chmod -R 755 /var/www/html/nextcloud/
```



### 通过Web安装程序在Debian 12上安装Nextcloud

使用浏览器访问 http://your_domain_or_IP_address/nextcloud，并创建 NextCloud 管理员账户，包括用户名和密码。接下来，你需要填写用于存储数据的 NextCloud 数据库的详细信息，具体信息为安装Mariadb时创建的数据库名称、nextcloud账号与密码。

填写无误后按 install按钮进行安装。

安装完成后会转到Recommened apps页面，可以选择Skip跳过，或者按Install Recommended apps安装推荐应用。

大功告成！



### 启用https

本案例通过自签证书演示

```bash
# 启动ssl模块
a2enmod ssl

# 2048 位的 RSA 密钥
openssl genrsa -out onlyoffice.key 2048

# 创建一个 CSR 文件 (onlyoffice.csr)，其中包含了公钥以及与证书请求相关的信息，例如组织信息、域名等。
openssl req -new -key onlyoffice.key -out onlyoffice.csr

# 使用 CSR 和私钥来生成一个自签名的数字证书 (onlyoffice.crt)，有效期为1095天（三年）
openssl x509 -req -days 1095 -in onlyoffice.csr -signkey onlyoffice.key -out onlyoffice.crt

# 修改/etc/apache2/sites-available/nextcloud.conf配置，在尾部添加443相关信息
nano /etc/apache2/sites-available/nextcloud.conf

--------------
<VirtualHost *:443>
    DocumentRoot /var/www/html/nextcloud/
    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/nextcloud.crt
    SSLCertificateKeyFile /etc/ssl/private/nextcloud.key
    SSLProtocol  all -SSLv2 -SSLv3
    SSLCipherSuite ECDH:AESGCM:HIGH:!RC4:!DH:!MD5:!aNULL:!eNULL
    SSLHonorCipherOrder on
    ServerName your_domain_or_IP_address

    <Directory /var/www/html/nextcloud/>
        Options +FollowSymlinks
        AllowOverride All
        Require all granted
        <IfModule mod_dav.c>
            Dav off
        </IfModule>
        SetEnv HOME /var/www/html/nextcloud/
        SetEnv HTTP_HOME /var/www/html/nextcloud/
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
--------------

# 将证书放到对应的位置并修改权限
mv nextcloud.crt /etc/ssl/certs/
chmod 644 /etc/ssl/certs/nextcloud.crt
mv nextcloud.key /etc/ssl/private/
chmod 700 /etc/ssl/private/nextcloud.key

# 检查配置文件语法
apache2ctl -t

# 启用虚拟主机配置文件
a2ensite /etc/apache2/sites-available/nextcloud.conf

# 重启apache2
systemctl restart apache2.service
```



### 修改php内存限制

Nextcloud推荐512M，可以适当给大点

```bash
# 修改php文件
nano /etc/php/8.2/apache2/php.ini

--------------
memory_limit = 512M
--------------

# 重启apache2
systemctl restart apache2.service
```



### **修改后台任务方式为Cron**

网页端

1. 登录到Nextcloud网页端，在打开应用管理界面
2. 点击管理设置，在左侧管理一栏找到基本设置后，点击
3. 选择Cron方式

服务端

注意/var/www/nextcloud/cron.php路径，如果是自定义的话，请改修改为`Nextcloud所在文件夹/cron.php`

```bash
# 使用www-data身份编辑crontab，添加下面的语句后保存退出
crontab -u www-data -e

--------------
*/5  *  *  *  * php -f /var/www/nextcloud/cron.php
--------------

# 验证是否添加
crontab -u www-data -l
# 类似返回
[snip]
*/5  *  *  *  * php -f /var/www/nextcloud/cron.php

```



## 安装app

线上安装的话直接在网页端的应用内点击安装即可，下面介绍是安装包安装。

1. 先到[此处](https://apps.nextcloud.com/)找到并下载对应Nextcloud版本的app安装包。
2. 下载完成后将app压缩包上传到服务器
3. 将app压缩包解压缩到位于 Nextcloud 网页文件夹内的名为 "apps" 的文件夹中
4. 执行`chown -R www-data:www-data /{路径}/[app解压后的文件夹名称]`
5. 然后就可以在nextcloud的应用里启用新安装的应用。

下面用Collabora和onlyoffice安装作为演示，实际使用只需安装一个即可，我更推荐Collabora。



## 安装在线办公app



### onlyoffice

在使用onlyoffice 时，避免使用 HTTPS 方式访问 Nextcloud。这是因为需要同时启用 onlyoffice和 Nextcloud 的 HTTPS 访问，但我尝试过并未成功。



#### onlyoffice服务端

要添加字体，先将字体上传到一个文件夹内，如fonts，然后将字体全部复制到 OnlyOffice 的 '/usr/share/fonts' 目录中。然后，在 OnlyOffice Docker 容器内执行以下命令：`./usr/bin/documentserver-generate-allfonts.sh`。

字体可以识别TrueType、OpenType类型，其它类型未尝试。

注意修改`JWT_SECRET=123`为你自己的密码

```bash
docker run -i -t -d -p 9000:80 --name onlyoffice --restart=always \
    -v /usr/local/docker/onlyoffice/DocumentServer/logs:/var/log/onlyoffice  \
    -v /usr/local/docker/onlyoffice/DocumentServer/data:/var/www/onlyoffice/Data  \
    -v /usr/local/docker/onlyoffice/DocumentServer/lib:/var/lib/onlyoffice \
    -v /usr/local/docker/onlyoffice/DocumentServer/db:/var/lib/postgresql \
    -e JWT_SECRET=123 onlyoffice/documentserver

docker cp -a fonts onlyoffice:/usr/share/fonts
docker exec -it onlyoffice ./usr/bin/documentserver-generate-allfonts.sh
```



#### onlyoffice连接器

1. 下载27版本对应的onlyoffice.tar.gz
2. 解压到 Nextcloud 网页文件夹内的名为 "apps" 的文件夹，本笔记的位置在/var/www/html/nextcloud/apps
3. 解压后的文件名为onlyoffice
4. 执行`chown -R www-data:www-data /var/www/html/nextcloud/apps/nextcloud  `

到此app就已经算安装完成了。



#### 配置onlyoffice连接器

1. 登录到Nextcloud网页端，在打开应用管理界面
2. 在“您的应用”寻找到onlyoffice后，启用
3. 点击管理设置，在左侧管理一栏找到onlyoffice后，点击
4. 输入ONLYOFFICE Docs地址，地址为`onlyoffice服务端IP地址:9000`
5. 输入秘钥(留空为关闭)，本笔记为`123`，保存。

如果右上角提示连接成功即可。



### Collabora



#### 安装

1. 本笔记使用的Collabora服务端方式为Collabora Online - Built-in CODE Server
2. 下载richdocumentscode.tar.gz和richdocuments-v8.1.1.tar.gz，前者为Collabora Online - Built-in CODE Server，后者为Collabora连接器
3. 都解压到 Nextcloud 网页文件夹内的名为 "apps" 的文件夹，本笔记的位置在/var/www/html/nextcloud/apps
4. 解压后的文件名有：richdocuments、richdocumentscode
5. 执行

```bash
chown -R www-data:www-data /var/www/html/nextcloud/apps/richdocumentscode
chown -R www-data:www-data /var/www/html/nextcloud/apps/richdocuments
```

6. 到此app就已经算安装完成了。



#### 配置

1. 登录到Nextcloud网页端，在打开应用管理界面
2. 在“您的应用”寻找到Collabora Online - Built-in CODE Server、Nextcloud Office后，启用
3. 点击管理设置，在左侧管理一栏找到Nextcloud Office（或Office）后，点击
4. 点击使用内建的 CODE - Collabora Online 开发版

大功告成



#### 添加字体

将字体文件复制到`/usr/share/fonts/`内，重启apache2即可

`systemctl restart apache2.service`

字体可以识别TrueType、OpenType类型，其它类型未尝试。



## (不推荐)Docker安装方式

数据库使用PostgreSQL演示

### 安装PostgreSQL

正式用还是建议常规安装，此处注意替换密码

```bash
docker volume create pgdata
docker volume inspect pgdata

docker run --name postgres -e POSTGRES_PASSWORD=123 --restart=always -p 5432:5432 -v pgdata:/var/lib/postgresql/data -d postgres:latest
docker exec -it postgres psql -U postgres
```



### (可选)安装portainer

监控容器状况

```bash
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```



### 安装Nextcloud

请注意，你需要替换相关数据库信息或修改映射的位置。在本次演示中，我们将使用 PostgreSQL。

172.17.0.3 是指 PostgreSQL Docker 容器的地址（动态）。我尝试过将其更改为 'localhost' 或本机地址，但都无法成功建立连接。

```bash
docker run -d -p 8080:80 --name nextcloud --restart=always \
-v /usr/local/docker/nextcloud/nextcloud:/var/www/html \
-v /usr/local/docker/nextcloud/apps:/var/www/html/custom_apps \
-v /usr/local/docker/nextcloud/config:/var/www/html/config \
-v /usr/local/docker/nextcloud/data:/var/www/html/data \
-e POSTGRES_DB='nextcloud' \
-e POSTGRES_USER='postgres' \
-e POSTGRES_PASSWORD='123' \
-e POSTGRES_HOST='172.17.0.3:5432' \
nextcloud
```

