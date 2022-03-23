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

