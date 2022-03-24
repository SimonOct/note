# ansible安装和入门

## 安装

此处安装使用epel源

```markdown
名称    ：ansible
架构    ：noarch
版本    ：2.9.27
发布    ：1.el7
大小    ：17 M
源    ：epel/x86_64
```

```bash
yum install ansible -y
```

debian10的话直接即可，默认安装版本为2.10，这也是这个笔记用到的版本

```
apt install ansible -y
```

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible --version
ansible 2.10.8
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/simon/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.9.2 (default, Feb 28 2021, 17:03:44) [GCC 10.2.1 20210110]
```

## 修改配置文件

如果没有的话可以去[ansible](https://github.com/ansible/ansible/tree/stable-2.10/examples)的GitHub找到相应版本的模板复制进去就好了

```bash
config file = /etc/ansible/ansible.cfg
hosts file = /etc/ansible/hosts
存放角色的目录 = /etc/ansible/roles/
```

## 命令格式

```bash
ansible <host-pattern> [-m module_name] [-a args]
```

### 测试

```bash
ansible all -m ping -k
```

```bash
SSH password:
192.168.109.152 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
192.168.109.151 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
192.168.109.153 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
```

`-k`表示使用密码想让这个命令成功运行，首先修改`ansible.cfg`里的`remote_user = root`, `host_key_checking = False`

**注意！**这里只是测试，现实中这样的做法需要三思

#### 使用ssh免密登录

```bash
ssh-keygen
ssh-copy-id root@192.168.109.153
ssh-copy-id root@192.168.109.152
ssh-copy-id root@192.168.109.151
```

再次测试

```bash
ansible all -m ping
```

即使不使用`-k`也能成功连通

## ansible 相关工具

### ansible-playbook

```bash
ansible-playbook hello.yml
cat hello.yml
#hello world yml file
- hosts: websrvs
  remote_user: root
  gather_facts: no

  tasks:
    - name: hello world
      command: /usr/bin/wall hello world
```

### ansible-vault

用来加密playbook文件的

加密

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible-vault encrypt hello.yml
New Vault password:
Confirm New Vault password:
Encryption successful
simon@DESKTOP-KFFEQ8I:~$ cat hello.yml
$ANSIBLE_VAULT;1.1;AES256
62353063666334623866663337313166376338646539663263396262396333663062613266663261
3361326264613762663933323939336433366366366631310a303766646434353130353237343737
32386264663135383539303131623831383130653264316663333038323730333361366135386236
6239326566306436310a336434623862343961623632303362313365363661616335306562383262
37656633646339646161613836323939373865353031333632623566316334616138306534656365
32346532663239353935613037333136383662373937366332356131616563636133363034326131
36656561363966633565643937666332393732616161626234653962616338313535653239646337
65643261353463653531353933626361346534636236383930633134613833653031623966643166
63366163643238373539653761633263333163373032326436313663383235366261626135386261
31373431643266623863396338663963313132373638326134363463636637613663356266313437
39316262633831626363633138666337366639663935613163623531643261353863303661663139
31653536346631363436
```

解密

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible-vault decrypt hello.yml
Vault password:
Decryption successful
simon@DESKTOP-KFFEQ8I:~$ cat hello.yml
#hello world yml file
- hosts: websrvs
  remote_user: root
  gather_facts: no

  tasks:
    - name: hello world
      command: /usr/bin/wall hello world
```

### ansible-console

提示符格式

```bash
执行用户@当前操作的主机组(当前组的主机数)[f: 并发数]$
```

## ansible模块

### command

在远程主机执行命令，此为默认模块，可忽略-m选项，这个模块在使用上有很大的局限

如不支持通配符，有时候执行命令不成功但也没报错

示例

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible websrvs -m command -a 'cat /etc/centos-release'
192.168.109.153 | CHANGED | rc=0 >>
CentOS Linux release 7.9.2009 (Core)
192.168.109.152 | CHANGED | rc=0 >>
CentOS Linux release 7.9.2009 (Core)
simon@DESKTOP-KFFEQ8I:~$ ansible websrvs -m command -a 'chdir=/etc cat /etc/centos-release'
192.168.109.152 | CHANGED | rc=0 >>
CentOS Linux release 7.9.2009 (Core)
192.168.109.153 | CHANGED | rc=0 >>
CentOS Linux release 7.9.2009 (Core)
```

### shell

可以理解为command加强版

如果想要指定shell为默认的模块，可以修改ansible.cfg里的配置即可

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible websrvs -m shell -a 'echo hello > /data/hello.log'
192.168.109.152 | CHANGED | rc=0 >>

192.168.109.153 | CHANGED | rc=0 >>

simon@DESKTOP-KFFEQ8I:~$ ansible websrvs -m shell -a 'cat /data/hello.log'
192.168.109.153 | CHANGED | rc=0 >>
hello
192.168.109.152 | CHANGED | rc=0 >>
hello
simon@DESKTOP-KFFEQ8I:~$ ansible websrvs -m shell -a 'chdir=/data creates=/etc/issue cat hello.l
og'
192.168.109.152 | SUCCESS | rc=0 >>
skipped, since /etc/issue exists
192.168.109.153 | SUCCESS | rc=0 >>
skipped, since /etc/issue exists
```

### script

在所有被控节点上运行控制节点上的脚本

先写一个脚本

```shell
simon@DESKTOP-KFFEQ8I:~$ cat /data/test.sh
#!/bin/bash

echo "My hostname is `hostname`."
```

执行

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible websrvs -m script -a '/data/test.sh'
192.168.109.153 | CHANGED => {
    "changed": true,
    "rc": 0,
    "stderr": "Shared connection to 192.168.109.153 closed.\r\n",
    "stderr_lines": [
        "Shared connection to 192.168.109.153 closed."
    ],
    "stdout": "My hostname is node4.\r\n",
    "stdout_lines": [
        "My hostname is node4."
    ]
}
192.168.109.152 | CHANGED => {
    "changed": true,
    "rc": 0,
    "stderr": "Shared connection to 192.168.109.152 closed.\r\n",
    "stderr_lines": [
        "Shared connection to 192.168.109.152 closed."
    ],
    "stdout": "My hostname is node3.\r\n",
    "stdout_lines": [
        "My hostname is node3."
    ]
}
```

正常情况下执行结束后.ansible/tmp下缓存的test.sh脚本会自动删除

如果ctrl+c强制停止，也是会自动删除的

### copy

从ansible服务器主控端复制文件到远程主机

如果src=file 如果是没指明路径，则为当前目录或当前目录下的files目录下的file文件

```bash
# 如果目标存在，默认覆盖，此处指定先备份
ansible websrvs -m copy -a 'src=/root/test1.sh dest=/tmp/test2.sh owner=simon mode=600 backup=yes'
# 指定内容，直接生成目标文件
ansible websrvs -m copy -a "content='test line1\ntest line2\n' dest=/tmp/test.txt"

# 复制/etc目录自身，注意/etc/后面没有/
ansible websrvs -m copy -a "src=/etc dest=/backup"

# 复制/etc/下的文件。不包括/etc/目录自身，注意/etc/后面有/
ansible websrvs -m copy -a "src=/etc/ dest=/backup"
```

### fetch

作用与copy相反，不支持目录

### file

设置文件属性，创建软连接等

```bash
# 创建空文件
ansible all -m file -a 'path=/data/test.txt state=touch'
ansible all -m file -a 'path=/data/test.txt state=absent'
ansible all -m file -a "path=/root/test.sh owner=simon mode=755"
# 创建目录
ansible all -m file -a "path=/data/mysql state=directory owner=mysql group=mysql"
# 创建软连接
ansible all -m file -a 'src=/data/testfile path|dest|name=/data/testfile-link state=link'
# 创建目录
ansible all -m file -a 'path=/data/testdir state=directory'

# 递归修改目录属性，但不递归至子目录
ansible all -m file -a "path=/data/mysql state=directory owner=mysql group=mysql"

# 递归修改目录及子目录的属性
ansible all -m file -a "path=/data/mysql state=directory owner=mysql group=mysql recurse=yes"
```

### unarchive

解压缩

1. 将ansible主机上的压缩包传到远程主机后解压缩至特定目录，设置copy=yes
2. 将远程主机上的某个压缩包解压缩到指定路径下，设置copy=no

常见参数

```markdown
copy：默认为yes，当copy=yes，拷贝的文件是从ansible主机复制到远程主机上，如果设置为copy=no，会在远程主机上寻找src源文件
remote_src：和copy功能一样且互斥，yes表示在远程主机，不在ansible主机。no表示文件在ansible主机上
src：源路径，可以是ansible主机上的路径，也可以是远程主机（被管理端或者第三方主机）上的路径，如果是远程主机上的路径，则需要设置copy=no
dest：远程主机上的目标路径
mode：设置解压缩后的文件权限
```

### archive

打包压缩

```bash
ansible websrvs -m archive -a 'path=/var/log/ dest=/data/log.tar.bz2 format=bz2 owner=simon mode=0600'
```

### hosotname

管理主机名

```bash
simon@DESKTOP-KFFEQ8I:~$ ansible 192.168.109.153 -m hostname -a 'name=node3.simon'
192.168.109.153 | CHANGED => {
    "ansible_facts": {
        "ansible_domain": "simon",
        "ansible_fqdn": "node3.simon",
        "ansible_hostname": "node3",
        "ansible_nodename": "node3.simon",
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": true,
    "name": "node3.simon"
}
simon@DESKTOP-KFFEQ8I:~$ ansible 192.168.109.153 -m shell -a "hostname"
192.168.109.153 | CHANGED | rc=0 >>
node3.simon
```

### cron

计划任务

支持时间：minute, hour, day, month, weekday

```bash
# 创建任务
ansible dbsrvs -m cron -a "hour=2 minute=30 weekday=1-5 name='backup mysql' job=/root/mysql_backup.sh"
ansible srv -m cron -a "minute=*/5 job='/usr/sbin/ntpdate 172.20.0.1 &> /dev/null' name=Synctime"
# 禁用计划任务
ansible srv -m cron -a "minute=*/5 job='/usr/sbin/ntpdate 172.20.0.1 &> /dev/null' name=Synctime disabled=yes"
# 启用计划任务
ansible srv -m cron -a "minute=*/5 job='/usr/sbin/ntpdate 172.20.0.1 &> /dev/null' name=Synctime disabled=no"
# 删除任务
ansible srv -m cron -a "name='backup mysql' state=absent"
ansible srv -m cron -a 'state=absent name=Synctime'
```

### yum

管理软件包，只支持RHEL, CentOS, Fedora

```bash
# 安装软件，不添加state的话默认就是安装
ansible websrvs -m yum -a "name=httpd"
ansible websrvs -m yum -a "name=httpd state=present"
# 卸载软件
ansible websrvs -m yum -a "name=httpd state=absent"
```

### service

管理服务

```bash
ansible websrvs -m service -a "name=httpd state=started enabled=yes"
ansible websrvs -m service -a "name=httpd state=stopped"
ansible websrvs -m service -a "name=httpd state=reloaded"
ansible websrvs -m service -a "name=httpd state=restarted"
```

### user

管理用户

```bash
# 创建用户
ansible srv -m user -a 'name=user1 comment="test user" uid=2048 home=/app/user1 group=root'

ansible srv -m user -a 'name=nginx comment=nginx uid=88 group=nginx groups="root,daemon" shell=/sbin/nologin system=yes create_home=no home=/data/nginx non_unique=yes'

# 删除用户及家目录等数据
ansible srv -m user  -a 'name=nginx state=absent remove=yes'
```

### group

管理组

```bash
# 创建组
ansible websrvs -m group -a 'name=nginx gid=88 system=yes'
# 删除组
ansible websrvs -m group -a 'name=nginx state=absent'
```

### lineinfile

ansible在使用sed进行替换时，经常会遇到需要转义的问题，而且ansible在遇到特殊符号进行替换时，存在问题，无法正常进行替换。其实在ansible字体提供了两个模块：lineinfile和replace，可以方便的进行替换

```bash
ansible all -m lineinfile -a "path=/etc/selinux/config regexp='^SELINUX=' line='SELINUX=enforcing'"
ansible all -m lineinfile -a 'dest=tec/fstab state=absent regexp="^#"'
```

### replace

```bash
ansible all -m replace -a "path=/etc/fstab regexp='^(UUID.*)' replace='#\1'"
ansible all -m replace -a "path=/etc/fstab regexp='^#(.*)' replace='\1'"
```

### setup

收集主机的系统信息，这些facts信息可以直接以变量的形式使用，但是如果主机较多，会影响执行速度，可以使用`gather_facts: no`来禁止ansible手机facts信息

```bash
ansible srv -m setup
ansible srv -m setup -a "filter=ansible_nodename"
ansible srv -m setup -a "filter=ansible_hostname"
ansible srv -m setup -a "filter=ansible_domain"
ansible srv -m setup -a "filter=ansible_memtotal_mb"
ansible srv -m setup -a "filter=ansible_memory_mb"
ansible srv -m setup -a "filter=ansible_memfree_mb"
ansible srv -m setup -a "filter=ansible_os_family"
ansible srv -m setup -a "filter=ansible_distribution_major_version"
ansible srv -m setup -a "filter=ansible_distribution_version"
ansible srv -m setup -a "filter=ansible_processor_vcpus"
ansible srv -m setup -a "filter=ansible_all_ipv4_addresses"
ansible srv -m setup -a "filter=ansible_architecture"
```

# playbook

## YAML介绍

```markdown
YAML是一个可读性高的用来表达资料序列的格式。
    YAML参考了其他多种语言，包括：XML、C语言、Python、Perl以及电子邮件格式RFC2822等。
    Clark Evans在2001年在首次发表了这种语言，另外Ingy döt Net与Oren Ben-Kiki也是这语言的共同设计者

YAML Ain't Markup Language，即YAML不是XML。
不过，在开发的这种语言时，YAML的意思其实是："Yet Another Markup Language"（仍是一种标记语言）

特性
    YAML的可读性好
    YAML和脚本语言的交互性好
    YAML使用实现语言的数据类型
    YAML有一个一致的信息模型
    YAML易于实现
    YAML可以基于流来处理
    YAML表达能力强，扩展性好

更多的内容及规范参见：http://www.yaml.org
```

### YAML语法简介

```markdown
> 在单一档案中，可用连续三个连字号(——)区分多个档案。
  另外，还有选择性的连续三个点号( ... )用来表示档案结尾
> 次行开始正常写Playbook的内容，一般建议写明该Playbook的功能
> 使用#号注释代码
> 缩进必须是统一的，不能空格和tab混用
> 缩进的级别也必须是一致的，同样的缩进代表同样的级别，程序判别配置的级别是通过缩进结合换行来实现的
> YAML文件内容是区别大小写的，k/v的值均需大小写敏感
> 多个k/v可同行写也可换行写，同行使用:分隔
> v可是个字符串，也可是另一个列表[]
> 一个完整的代码块功能需最少元素需包括 name 和 task
> 一个name只能包括一个task
> YAML文件扩展名通常为yml或yaml
```

### YAML语法

```yaml
List：列表，其所有元素均使用“-”打头
      列表代表同一类型的元素
示例：
# A list of tasty fruits
- Apple
- Orange
- Strawberry
- Mango

Dictionary：字典，通常由多个key与value构成 键值对
示例：
---
# An employee record
name: Example Developer
job: Developer
skill: Elite

也可以将key:value放置于{}中进行表示，用,分隔多个key:value
示例：
---
# An employee record
{name: Example Developer, job: Developer, skill: Elite}  有空格
```

### 三种常见的数据交换格式

```xml
<Servers>
    <Server>
        <name>Server1</name>
        <owner>John</owner>
        <created>123456</created>
        <status>active</status>
    </Server>
</Servers>
```

```json
{
  "Servers": {
    "Server": {
      "name": "Server1",
      "owner": "John",
      "created": "123456",
      "status": "active"
    }
  }
}
```

```yaml
---
Servers:
  Server:
    name: Server1
    owner: John
    created: '123456'
    status: active
```

