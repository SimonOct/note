# Docker-compose

[文档](https://docs.docker.com/compose/compose-file/compose-file-v3/)

## 是什么

Docker-Compose是Docker官方的开源项目，负责实现对Docker容器集群的快速编排。

## 干什么

docker建议我们每一个容器中只运行一个服务,因为docker容器本身占用资源极少,所以最好是将每个服务单独的分割开来但是这样我们又面临了一个问题？

如果我需要同时部署好多个服务,难道要每个服务单独写Dockerfile然后在构建镜像,构建容器,这样累都累死了,所以docker官方给我们提供了docker-compose多服务部署的工具

例如要实现一个Web微服务项目，除了Web服务容器本身，往往还需要再加上后端的数据库mysql服务容器，redis服务器，注册中心eureka，甚至还包括负载均衡容器等等。。。。。。

Compose允许用户通过一个单独的docker-compose.yml模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。

可以很容易地用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。Docker-Compose 解决了容器与容器之间如何管理编排的问题。

## 安装

[下载地址](https://docs.docker.com/compose/install/#install-compose)

直接根据官网的步骤即可

示例：

本操作的用户是**root**，非root用户则在命令前加上`sudo`

```bash
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

[卸载方法](https://docs.docker.com/compose/install/#uninstallation)

## Compose核心概念

### 一文件

`docker-compose.yml`

### 两要素

- 服务（service）

一个个应用容器实例，比如订单微服务、库存微服务、mysql容器、nginx容器或者redis容器

- 工程（project）

由一组关联的应用容器组成的一个**完整业务单元**，在docker-compose.yml 文件中定义。

## Compose使用的三个步骤

- 编写Dockerfile定义各个微服务应用并构建出对应的镜像文件
- 使用 docker-compose.yml定义一个完整业务单元，安排好整体应用中的各个容器服务。
- 最后，执行docker-compose up命令来启动并运行整个应用程序，完成一键部署上线

## 常用命令

```bash
docker-compose -h                           # 查看帮助

docker-compose up                           # 启动所有docker-compose服务

docker-compose up -d                        # 启动所有docker-compose服务并后台运行

docker-compose down                         # 停止并删除容器、网络、卷、镜像。

docker-compose exec  yml里面的服务id
# 进入容器实例内部  docker-compose exec docker-compose.yml文件中写的服务id /bin/bash

docker-compose ps                      # 展示当前docker-compose编排过的运行的所有容器

docker-compose top                     # 展示当前docker-compose编排过的容器进程

docker-compose logs  yml里面的服务id     # 查看容器输出日志

docker-compose config     # 检查配置

docker-compose config -q  # 检查配置，有问题才有输出

docker-compose restart   # 重启服务

docker-compose start     # 启动服务

docker-compose stop      # 停止服务
```

## Compose编排微服务
