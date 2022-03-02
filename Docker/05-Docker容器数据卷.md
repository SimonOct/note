# Docker容器数据卷

Docker挂载主机目录访问如果出现**cannot open directory. : Permission denied**

解决办法：在挂载目录后多加一个`--privileged=true`参数即可

如果是CentOS7安全模块比之前系统版本加强，不安全的会先禁止，所以目录挂载的情况被默认为不安全的行为，

在SELinux里面挂载目录被禁止掉了额，如果要开启，我们一般使用--privileged=true命令，扩大容器的权限解决挂载目录没有权限的问题，也即

使用该参数，container内的root拥有真正的root权限，否则，container内的root只是外部的一个普通用户权限。

## 是什么

卷就是目录或文件，存在于一个或多个容器中，由docker挂载到容器，但不属于联合文件系统，因此能够绕过Union File System提供一些用于持续存储或共享数据的特性：

卷的设计目的就是**数据的持久化**，完全独立于容器的生存周期，因此Docker不会在容器删除时删除其挂载的数据卷

命令解析

```bash
docker run -d -p 5000:5000  -v /simon/myregistry:/tmp/registry --privileged=true registry
```

-v就是指定将本机的/simon/myregistry(绝对路径)映射到镜像中的/tmp/registry

作用是将docker容器内的数据保存进宿主机的磁盘中

## 作用

将运用与运行的环境打包镜像，run后形成容器实例运行 ，但是我们对数据的要求希望是**持久化**的

Docker容器产生的数据，如果不备份，那么当容器实例删除后，容器内的数据自然也就没有了。

为了能保存数据在docker中我们使用卷。

特点：

- 数据卷可在容器之间共享或重用数据
- 卷中的更改可以直接实时生效
- 数据卷中的更改不会包含在镜像的更新中
- 数据卷的生命周期一直持续到没有容器使用它为止

## 案例

### 宿主与容器之间映射添加容器卷

语法

```bash
docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名
```

使用（若目录不存在，会自动创建）

```bash
docker run -it --privileged=true -v /tmp/host_data:/tmp/docker_data --name=u1 ubuntu
```

在容器的`/tmp/docker_data`里面新建一个文件

返回到宿主机后查看`/tmp/host_data`

![image-20220302221924681](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302221924681.png)

在宿主机`/tmp/host_data`下新建一个文件

返回到容器查看`/tmp/docker_data`目录

![image-20220302222102366](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302222102366.png)

即使宿主机在容器停止的情况下往`/tmp/host_data`目录写入数据，当容器重新启动后，也能看到最新的数据

### 读写规则映射添加说明

下面该命令默认是允许读与写

```bash
docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名
```

只读

```bash
docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录:ro 镜像名
```

该命令只限制容器，而不限制宿主机。意味着宿主机写入新数据后，容器能读取但不能修改

示例

```bash
docker run -it --privileged=true -v /mydocker/u:/tmp/u:ro --name=u2 ubuntu
```

![image-20220302224128984](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302224128984.png)

### 卷的继承和共享

先启动一个容器

```bash
docker run -it --privileged=true -v /mydocker/u:/tmp/u --name=u1 ubuntu
```

容器2继承容器1的卷规则

语法

```bash
docker run -it --privileged=true --volumes-from 父类 --name u2 ubuntu
```

示例

```bash
docker run -it --privileged=true --volumes-from u1 --name u2 ubuntu
```

![image-20220302224804295](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302224804295.png)

在容器u1上查看能否获取新数据

![image-20220302224841305](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302224841305.png)

尝试停止u1后在宿主机与u2添加数据

![image-20220302225034601](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302225034601.png)

![image-20220302225047711](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302225047711.png)

成功，可以得出结论，u2继承的只是规则与u1是否启动毫无关系

尝试启动u1

![image-20220302225232826](05-Docker%E5%AE%B9%E5%99%A8%E6%95%B0%E6%8D%AE%E5%8D%B7.assets/image-20220302225232826.png)

能看到新增的文件