# DockerFIle解析

## 是什么

Dockerfile是用来构建Docker镜像的文本文件，是由一条条构建镜像所需的指令和参数构成的脚本。

[官方文档](https://docs.docker.com/engine/reference/builder/)

![index](08-DockerFile.assets/index.png)

构建三部曲

- 编写Dockerfile
- docker build命令构建镜像
- docker run依镜像运行容器示例

## DockerFile构建过程解析

### dockerfile内容基础知识

- 每条保留字指令都**必须为大写字母**且后面要跟随至少一个参数
- 指令按照从上到下，顺序执行
- \#表示注释
- 每条指令都会创建一个新的镜像层并对镜像进行提交

### Docker执行Dockerfile的大致流程

- docker从基础镜像运行一个容器
- 执行一条指令并对容器作出修改
- 执行类似docker commit的操作提交一个新的镜像层
- docker再基于刚提交的镜像运行一个新容器
- 执行dockerfile中的下一条指令直到所有指令都执行完成

从应用软件的角度来看，Dockerfile、Docker镜像与Docker容器分别代表软件的三个不同阶段，

- Dockerfile是软件的原材料
- Docker镜像是软件的交付品
- Docker容器则可以认为是软件镜像的运行态，也即依照镜像运行的容器实例

### 总结

Dockerfile面向开发，Docker镜像成为交付标准，Docker容器则涉及部署与运维，三者缺一不可，合力充当Docker体系的基石。

![index](08-DockerFile.assets/index-16463204329411.png)

Dockerfile，需要定义一个Dockerfile，Dockerfile定义了进程需要的一切东西。Dockerfile涉及的内容包括执行代码或者是文件、环境变量、依赖包、运行时环境、动态链接库、操作系统的发行版、服务进程和内核进程(当应用进程需要和系统服务和内核进程打交道，这时需要考虑如何设计namespace的权限控制)等等;

Docker镜像，在用Dockerfile定义一个文件之后，docker build时会产生一个Docker镜像，当运行 Docker镜像时会真正开始提供服务;

Docker容器，容器是直接提供服务的。

## DokerFile常用保留字指令

参考tomcat8的[dockerfile](https://github.com/docker-library/tomcat/blob/master/10.0/jdk8/corretto/Dockerfile)

### FROM

基础镜像，当前新镜像是基于哪个镜像的，指定一个已经存在的镜像作为模板，第一条必须是from

### MAINTAINER

镜像维护者的姓名和邮箱地址

### RUN

RUN是在docker build时运行

容器构建时需要运行的命令，有两种格式

- shell

RUN <命令行命令>	等同于，在终端操作的shell命令

- exec

RUN ["可执行文件", "参数1", "参数2" ]

如，RUN ["./test.php", "dev", offline""] 等价于 RUN ./test.php dev offline

### EXPOSE

当前容器对外暴露出的端口

### WORKDIR

指定在创建容器后，终端默认登陆的进来工作目录，一个落脚点

### USER

指定该镜像以什么样的用户去执行，如果都不指定，默认是root

### ENV

用来在构建镜像过程中设置环境变量

ENV MY_PATH /usr/mytest

这个环境变量可以在后续的任何RUN指令中使用，这就如同在命令前面指定了环境变量前缀一样；

也可以在其它指令中直接使用这些环境变量，

比如：WORKDIR $MY_PATH

### ADD

将宿主机目录下的文件拷贝进镜像且会自动处理URL和解压tar压缩包

### COPY

类似ADD，拷贝文件和目录到镜像中。

将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置

- COPY src dest
- COPY ["src", "dest"]
- <src源路径>：源文件或者源目录
- <dest目标路径>：容器内的指定路径，该路径不用事先建好，路径不存在的话，会自动创建。

### VOLUME

容器数据卷，用于数据保存和持久化工作

相当于`-v`

### CMD

指定容器启动后的要干的事情

CMD指令的格式和RUN相似，也是两种格式

- shell格式	CMD <命令>
- exec格式	CMD ["可执行文件", "参数1", "参数2" ...]
- 在指定ENTRYPOINT后，exec格式的[]都代表参数

Dockerfile 中可以有多个 CMD 指令，但**只有最后一个生效**，CMD 会被 docker run 之后的参数替换

也就是`docker run -it xxx /bin/bash`后，CMD会变成CMD ["/bin/bash"]了

CMD是在docker run 时运行。

### ENTRYPOINT

也是用来指定一个容器启动时要运行的命令

类似于 CMD 指令，但是ENTRYPOINT**不会**被docker run后面的命令覆盖，而且这些命令行参数会被当作参数送给 ENTRYPOINT 指令指定的程序

命令有两种格式

exec

```bash
ENTRYPOINT ["executable", "param1", "param2"]
```

shell

```shell
ENTRYPOINT command param1 param2
```

ENTRYPOINT可以和CMD一起用，一般是变参才会使用 CMD ，这里的 CMD 等于是在给 ENTRYPOINT 传参。

当指定了ENTRYPOINT后，CMD的含义就发生了变化，不再是直接运行其命令而是将CMD的内容作为参数传递给ENTRYPOINT指令，他两个组合会变成\<ENTRYPOINT\> "\<CMD\>"

案例如下：假设已通过 Dockerfile 构建了 nginx:test 镜像：

```bash
FROM nginx
ENTRYPOINT ["nginx", "-c"]
CMD ["/etc/nginx/nginx.conf"]
```

| 是否传参         | 按照dockerfile编写执行         | 传参运行                                       |
| ---------------- | ------------------------------ | ---------------------------------------------- |
| Docker命令       | docker run nginx:test          | docker run nginx:test  /etc/nginx/**new.conf** |
| 衍生出的实际命令 | nginx -c /etc/nginx/nginx.conf | nginx -c /etc/nginx/**new.conf**               |

### 总结

| BUILD         | Both    | RUN        |
| ------------- | ------- | ---------- |
| FROM          | WORKDIR | CMD        |
| MAINTAINER    | USER    | ENV        |
| COPY          |         | EXPOSE     |
| ADD           |         | VOLEME     |
| RUN           |         | ENTRYPOINT |
| ONBUILD       |         |            |
| .dockerignore |         |            |

## 自定义镜像

### 需求

Centos7镜像具备vim+ifconfig+jdk8

先[下载jdk8](https://www.oracle.com/java/technologies/downloads/#java8)

### 编写

新建一个文件夹/myfile，并切换到该目录下

在该目录下新建一个名为Dockerfile文件，输入

```bash
FROM centos:centos7.9.2009
MAINTAINER simon<simonoct14@foxmail.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH

#安装vim编辑器
RUN yum -y install vim
#安装ifconfig命令查看网络IP
RUN yum -y install net-tools
#安装java8及lib库
RUN yum -y install glibc.i686
RUN mkdir /usr/local/java
#ADD 是相对路径jar,把jdk-8u321-linux-x64.tar.gz添加到容器中,安装包必须要和Dockerfile文件在同一位置
ADD jdk-8u321-linux-x64.tar.gz /usr/local/java/
#配置java环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_321
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH

EXPOSE 80

# 前两个CMD会运行，只是都会被最后一个CMD覆盖
CMD echo $MYPATH
CMD echo "success--------------ok"
CMD /bin/bash
```

### 构建

注意不要遗漏“.”

```bash
docker build -t 新镜像名字:TAG .
```

如

```bash
docker build -t centosjava8:1.5 .
```

```bash
[root@simon myfile]# docker build -t centosjava8:1.5 .
Sending build context to Docker daemon  146.8MB
Step 1/17 : FROM centos:centos7.9.2009
 ---> eeb6ee3f44bd
Step 2/17 : MAINTAINER simon<simonoct14@foxmail.com>
 ---> Running in d6bd6dd27ed9
Removing intermediate container d6bd6dd27ed9
 ---> b5ce8d11ebc1
Step 3/17 : ENV MYPATH /usr/local
 ---> Running in 7b0ed4bee8b5
Removing intermediate container 7b0ed4bee8b5
 ---> 161062e445fa
Step 4/17 : WORKDIR $MYPATH
 ---> Running in 3859a59aedaf
Removing intermediate container 3859a59aedaf
 ---> 0410f3192e8a
Step 5/17 : RUN yum -y install vim
 ---> Running in 8a4faa826a67

...略...

Step 9/17 : ADD jdk-8u321-linux-x64.tar.gz /usr/local/java/
 ---> 0bedd1a150d4
Step 10/17 : ENV JAVA_HOME /usr/local/java/jdk1.8.0_321
 ---> Running in a402a2bee256
Removing intermediate container a402a2bee256
 ---> 3816dc5159ce
Step 11/17 : ENV JRE_HOME $JAVA_HOME/jre
 ---> Running in b1df149700d5
Removing intermediate container b1df149700d5
 ---> 8cf16b38f201
Step 12/17 : ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
 ---> Running in 4ab00a76e0c1
Removing intermediate container 4ab00a76e0c1
 ---> 5fa9fd02ae35
Step 13/17 : ENV PATH $JAVA_HOME/bin:$PATH
 ---> Running in 55f834273901
Removing intermediate container 55f834273901
 ---> dfdb422c351f
Step 14/17 : EXPOSE 80
 ---> Running in ae7b0e81977a
Removing intermediate container ae7b0e81977a
 ---> f037984f1111
Step 15/17 : CMD echo $MYPATH
 ---> Running in 0f530971a6f3
Removing intermediate container 0f530971a6f3
 ---> c05a68446c78
Step 16/17 : CMD echo "success--------------ok"
 ---> Running in a69ca1056199
Removing intermediate container a69ca1056199
 ---> b8d022e55a48
Step 17/17 : CMD /bin/bash
 ---> Running in 2b1f567c4588
Removing intermediate container 2b1f567c4588
 ---> 89c1c5e8b5d6
Successfully built 89c1c5e8b5d6
Successfully tagged centosjava8:1.5
```

注意，每一步都会产生一个层，尽量能写一行的指令就写一行

从这里可以再次体会到UnionFS

### 运行

跟之前的一样

```bash
[root@simon myfile]# docker run -it 89c1c5e8b5d6
[root@c7133a8ca0b5 local]# echo $SHELL
/bin/bash
[root@c7133a8ca0b5 local]# vi
vi        view      vigr      vim       vimdiff   vimtutor  vipw
[root@c7133a8ca0b5 local]# if
if         ifconfig   ifenslave
[root@c7133a8ca0b5 local]# java -version
java version "1.8.0_321"
Java(TM) SE Runtime Environment (build 1.8.0_321-b07)
Java HotSpot(TM) 64-Bit Server VM (build 25.321-b07, mixed mode)
[root@c7133a8ca0b5 local]#
[root@c7133a8ca0b5 local]# [root@simon myfile]#
[root@simon myfile]# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
c7133a8ca0b5   89c1c5e8b5d6   "/bin/sh -c /bin/bash"   2 minutes ago   Up 2 minutes   80/tcp    romantic_almeida
```

## 虚悬镜像

### 是什么

仓库名、标签都是<none>的镜像，俗称dangling image

### 示例

编写Dockerfile

```bash
from ubuntu
CMD echo 'action is success'
```

```
root@simon:/myfile# docker build .
Sending build context to Docker daemon  2.048kB
Step 1/2 : from ubuntu
 ---> ba6acccedd29
Step 2/2 : CMD echo 'action is success'
 ---> Running in 8d646ce036a3
Removing intermediate container 8d646ce036a3
 ---> 35ef91efc29f
Successfully built 35ef91efc29f
root@simon:/myfile# docker images
REPOSITORY                                                      TAG             IMAGE ID       CREATED         SIZE
<none>                                                          <none>          35ef91efc29f   9 seconds ago   72.8MB
```

### 查看

```bash
docker image ls -f dangling=true
```

### 删除

虚悬镜像已经失去存在价值，可以删除

```bash
docker image prune
```

