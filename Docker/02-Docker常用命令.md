# Docker常用命令



## 帮助启动类命令

用root用户演示，非root的注意加上`sudo`

启动docker

```bash
systemctl start docker
```

停止docker

```bash
systemctl stop docker
```

重启docker

```bash
systemctl restart docker
```

查看docker状态

```bash
systemctl status docker
```

开机自启

```bash
systemctl enable docker
```

查看docker概要信息

```bash
docker info
```

查看docker总体帮助文档

```bash
docker --help
```

查看docker命令帮助文档

```bash
docker 具体命令 --help
```

## 镜像命令

```bash
[root@simon ~]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    feb5d9fea6a5   5 months ago   13.3kB
```

各个选项说明：

- REPOSITORY    表示镜像的仓库源
- TAG    镜像的标签版本号
- IMAGE ID    镜像ID
- CREATED    镜像创建时间
- SIZE    镜像大小

同一个仓库源可以有多个TAG版本，代表这个仓库源的不同个版本，我们使用REPOSITORY:TAG 来定义不同的镜像

如果你不指定一个镜像的版本标签，假如你只使用ubuntu，docker将默认使用ubuntu:latest 镜像

### docker images

列出本地主机上的镜像

- -a    列出本地所有的镜像（含历史映像层）
- -q    只显示镜像ID

```bash
[root@simon ~]# docker images -a
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    feb5d9fea6a5   5 months ago   13.3kB
[root@simon ~]# docker images -q
feb5d9fea6a5
```

### docker search 镜像名

Search the Docker Hub for images

![image-20220228072806697](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220228072806697.png)

- NAME    镜像名称
- DESCRIPTION    镜像说明
- STARS    点赞数量
- OFFICIAL    是否是官方
- AUTOMATED    是否是自动构建的

```bash
--limit    只列出N个镜像，默认25个
```

![image-20220228073443008](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220228073443008.png)

### docker pull 镜像名

下载镜像

```bash
docker pull 镜像名[:TAG]
```

没有TAG默认下载最新版

与`docker pull 镜像名:latest`等价

![image-20220228074221312](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220228074221312.png)

### docker system df

查看镜像/容器/数据卷所占的空间

![image-20220228080839359](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220228080839359.png)

### docker rmi 镜像ID

删除镜像remove image

删除单个

```bash
docker rmi 镜像ID
```

如果有提示需要强制卸载，那么就加个`-f`即可

![image-20220228101059289](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220228101059289.png)

删除多个

```bash
docker rmi 镜像ID1 镜像ID2 ... 镜像IDN
```

![image-20220228101220554](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220228101220554.png)

删除全部**（现实中不要这样做）**

```bash
docker rmi $(docker images -qa)
```

### 虚悬镜像(dangling image)

指的是没有仓库名或没有标签的镜像

直接删掉即可

查询显示虚悬镜像

```bash
docker images -f dangling=true
```

删除虚悬镜像

```bash
docker rmi $(docker images -q -f dangling=true)
```

## 容器命令

这里使用ubuntu镜像演示

首先先下载一个ubuntu镜像`docker pull ubuntu`

### 新建/启动容器

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

 OPTIONS说明（常用）

--name="容器新名字"    为容器指定一个名称；

-d: 后台运行容器并返回容器ID，也即启动守护式容器(后台运行)；

-i：以交互模式运行容器，通常与 -t 同时使用；

-t：为容器重新分配一个伪输入终端，通常与 -i 同时使用；也即启动交互式容器(前台有伪终端，等待交互)；

-P: 随机端口映射，大写P

-p: 指定端口映射，小写p

#### 交互式容器

使用镜像ubuntu:latest以交互模式启动一个容器，在容器内执行`/bin/bash`命令，不指定的话默认为`bash`。

`docker run -it ubuntu /bin/bash` 

#### 守护进程式容器

以启动ubuntu为例，引出一个问题

```bash
docker run -d ubuntu
```

![image-20220301041045416](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301041045416.png)

可以使用`docker ps -a`后可以发现，容器一经推出

这是因为docker容器后台运行，就必须有一个前台进程

容器运行的命令如果不是那些一直挂起的命令（如top，tail），就是会自动退出的

这个是docker的机制问题,比如你的web容器,我们以nginx为例，正常情况下,

我们配置启动服务只需要启动响应的service即可。例如service nginx start

但是,这样做,nginx为后台进程模式运行,就导致docker前台没有运行的应用,

这样的容器后台启动后,会立即自杀因为他觉得他没事可做了.

所以，最佳的解决方案是,将你要运行的程序以前台进程的形式运行，

常见就是命令行模式，表示我还有交互操作，别中断

运行redis则没有这个问题

![image-20220301041757608](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301041757608.png)

### 列出当前所有正在运行的容器

```bash
docker ps [OPTIONS]
```

OPTIONS说明（常用）：

-a :列出当前所有正在运行的容器+历史上运行过的

-l :显示最近创建的容器。

-n：显示最近n个创建的容器。

-q :静默模式，只显示容器编号。

### 退出容器

`exit`或快捷键`ctrl+d`

run进去容器，`exit`退出，容器**停止**

快捷键`ctrl+p+q`

run进去容器，`ctrl+p+q`退出，容器**不停止**

### 启动已经停止的容器

```bash
docker start 容器ID或者容器名
```

![image-20220301040037937](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301040037937.png)

### 停止容器

```bash
docker stop 容器ID或者容器名
```

### 强制停止容器

```bash
docker kill 容器ID或者容器名
```

### 删除已经停止的容器

首先停止容器运行

```bash
docker stop 容器ID
```

然后删除

```bash
docker rm 容器ID
```

![image-20220301040343911](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301040343911.png)

当然也可以强制删除正在运行的容器，加个`-f`

```bash
docker rm -f 容器ID
```

一次性删除多个容器（不要在现实中使用）

```bash
docker rm -f $(docker ps -q -a)
```

或

```bash
docker ps -a -q | xargs docker rm
```

### 查看容器日志

```bash
docker logs 容器ID
```

### 查看容器内运行的进程

```bash
docker top 容器ID
```

### 查看容器内部细节

```bash
docker inspect 容器ID
```

### 进入正在运行的容器并以命令行交互

```bash
docker exec -it 容器ID bashShell
```

如， `docker exec -it e1a956e0b08a /bin/bash`，必须要指定shell

重新进入

```bash
docker attach 容器ID
```

`exec -it`与`attach`区别

- attach直接进入容器启动命令的终端，不会启动新的进程，用exit退出会导致容器的停止
- exec实在容器中打开新的终端，并且可以启动新的进程，用exit退出不会导致容器的停止

推荐大家使用`docker exec`命令，因为退出容器终端不会导致容器的停止

### 从容器内拷贝文件到主机上

容器→主机

```bash
docker cp 容器ID:容器内路径 目的主机路径
```

![image-20220301051534531](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301051534531.png)

### 导入和导出容器

导出

导出容器的内容为一个tar归档文件[对应import命令]

```bash
docker export 容器ID > 文件名.tar
```

![image-20220301051856968](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301051856968.png)

导入

iport从tar包中的内容创建一个新的文件系统再导入为镜像[对应export]

```bash
cat 文件名.tar |docker import - 镜像用户/镜像名:镜像版本号
```

![image-20220301052404686](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301052404686.png)

并且原本在/tmp创建的a.txt也在

![image-20220301052508712](02-Docker%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.assets/image-20220301052508712.png)
