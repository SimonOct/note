# Git

![img](git%E7%AC%94%E8%AE%B0.assets/1090617-20181008211557402-232838726.png)

**Workspace**： 工作区，就是你平时存放项目代码的地方

**Index / Stage**： 暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信息

**Repository**： 仓库区（或版本库），就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中HEAD指向最新放入仓库的版本

**Remote**： 远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换

初始化`git init`

## 工作流程

git的工作流程一般是这样的：

- 在工作目录中添加、修改文件；
- 将需要进行版本管理的文件放入暂存区域；
- 将暂存区域的文件提交到git仓库。

因此，git管理的文件有三种状态：已修改（modified）,已暂存（staged）,已提交(committed)

## 设置签名

形式：

​	用户名：simon

​	Email地址：simonoct14@gamil.com

作用：区分不同开发人员的身份

辨析：这里设置的签名和登录远程库（代码托管中心）的账号、密码没有任何关系

命令

- 项目级别/仓库级别：仅在当前本地库范围内有效
  - `git config user.name simon`
  - `git config user.email simonoct14@gmail.com`
  - 信息保存在.git/下的config文件
- 系统用户级别：登陆当前操作系统的用户范围
  - `git config --global user.name simon`
  - `git config --global user.email simonoct14@gmail.com`
  - 信息保存在家目录下的.gitconfig
    - 就近原则：项目级别优先于系统用户级别，二者都有时采用项目级别的签名
    - 如果只有系统用户级别的签名，就以系统用户级别的签名为准
    - 不允许二者都没有的情况

## 基本操作

### 文件的四种状态

版本控制就是对文件的版本控制，要对文件进行修改、提交等操作，首先要知道文件当前在什么状态，不然可能会提交了现在还不想提交的文件，或者要提交的文件没提交上。

GIT不关心文件两个版本之间的具体差别，而是关心文件的整体是否有改变，若文件被改变，在添加提交时就生成文件新版本的快照，而判断文件整体是否改变的方法就是用SHA-1算法计算文件的校验和。

![img](git%E7%AC%94%E8%AE%B0.assets/1090617-20181008212040668-1339848607.png)

**Untracked:**  未跟踪, 此文件在文件夹中, 但并没有加入到git库, 不参与版本控制. 通过git add 状态变为Staged.

**Unmodify:**  文件已经入库, 未修改, 即版本库中的文件快照内容与文件夹中完全一致. 这种类型的文件有两种去处, 如果它被修改, 而变为Modified.如果使用git rm移出版本库, 则成为Untracked文件

**Modified:** 文件已修改, 仅仅是修改, 并没有进行其他的操作. 这个文件也有两个去处, 通过git add可进入暂存staged状态, 使用git checkout 则丢弃修改过,返回到unmodify状态, 这个git checkout即从库中取出文件, 覆盖当前修改

**Staged:** 暂存状态. 执行git commit则将修改同步到库中, 这时库中的文件和本地文件又变为一致, 文件为Unmodify状态. 执行git reset HEAD filename取消暂存,文件状态为Modified

![img](git%E7%AC%94%E8%AE%B0.assets/1090617-20181008212245877-52530897.png)

新建文件--->Untracked

使用add命令将新建的文件加入到暂存区--->Staged

使用commit命令将暂存区的文件提交到本地仓库--->Unmodified

如果对Unmodified状态的文件进行修改---> modified

如果对Unmodified状态的文件进行remove操作--->Untracked

### 状态查操作

`git status`

查看工作区、暂存区状态

### 添加操作

`git add [file name]`

将工作区的文件“新添与修改”添加到暂存区

### 提交操作

`git commit -m "commit message" [file name]`

### 查看历史记录

`git log`

![image-20220124001843321](git%E7%AC%94%E8%AE%B0.assets/image-20220124001843321.png)

`git log --pretty=oneline`

![image-20220124002020064](git%E7%AC%94%E8%AE%B0.assets/image-20220124002020064.png)

`git log --oneline`

![image-20220124002034734](git%E7%AC%94%E8%AE%B0.assets/image-20220124002034734.png)

`git reflog`

![image-20220124002050038](git%E7%AC%94%E8%AE%B0.assets/image-20220124002050038.png)

`HEAD@{3}`表示移动到当前版本需要3步

### 前进后退

#### 基于索引值

可以前进也可以后退

`git reset --hard [局部索引值]`

![image-20220124222902088](git%E7%AC%94%E8%AE%B0.assets/image-20220124222902088.png)

`git reset --hard HEAD@{1}`

![image-20220124224104815](git%E7%AC%94%E8%AE%B0.assets/image-20220124224104815.png)

#### 使用^符号

只能后退

`git reset --hard HEAD^`

一个^表示后退一个版本，两个^表示两个，依此类推

![image-20220124223442496](git%E7%AC%94%E8%AE%B0.assets/image-20220124223442496.png)

#### 使用~符号

只能后退

`git reset --hard HEAD~n`

n表示后退几步

![image-20220124223834121](git%E7%AC%94%E8%AE%B0.assets/image-20220124223834121.png)

### reset命令的三个参数对比

#### --soft

- 仅仅在本地库移动HEAD指针

  ![image-20220124224858060](git%E7%AC%94%E8%AE%B0.assets/image-20220124224858060.png)

#### --mixed

- 在本地库移动HEAD指针

- 重置暂存区

  ![image-20220124225117927](git%E7%AC%94%E8%AE%B0.assets/image-20220124225117927.png)

#### --hard

- 在本地库移动HEAD指针
- 重置暂存区
- 重置工作区

### 文件删除找回

前提：删除前，文件存在时的状态提交到了本地库

操作：`git reset --hard [指针位置]`

- 删除操作已经提交到本地库：指针位置指向历史记录
- 删除操作尚未提交到本地库：指针位置使用HEAD

### 比较文件差异

`git diff [文件名]`

- 将工作区中的文件和暂存区进行比较

`git diff [本地库中历史版本] [文件名]`

- 将工作区中的文件和本地库历史记录比较

不带文件名比较多个文件

## 分支管理

在版本控制中，使用多条线同时推进多个任务

**好处**

- 同时并行推进多个功能开发，提高开发效率
- 各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响，失败的分支删除重新开始即可

### 分支操作

#### 创建分支

`git branch [分支名]`

#### 查看分支

`git branch -v`

#### 切换分支

`git checkout [分支名]`

#### 合并分支

- 第一步，切换到接受修改的分支上

  `git checkout [被合并分支名]`

- 第二部，执行merge命令

  `git merge [有新内容的分支]`

#### 解决冲突

**冲突的表现形式**：

![image-20220125233727512](git%E7%AC%94%E8%AE%B0.assets/image-20220125233727512.png)

![image-20220125233747319](git%E7%AC%94%E8%AE%B0.assets/image-20220125233747319.png)

**冲突的解决**：

- 第一步：编辑文件，删除特殊符号

- 第二步：把文件修改到满意的程度

- 第三步：`gid add [文件名]`

- 第四步：`git commit -m "日志信息"`

  `git commit`时不需要带文件名

## Github使用

创建一个新的文件夹后，在该文件夹下

- `git init`

设置签名

- `git config user.name simon`
- `git config user.email simonoct14@gmail.com`

（可选）添加远程推送别名，此处使用ssh方式，并且已经配置好密钥

- `git remote add first git@github.com:SimonOct/firstGit.git`

### 推送

上本地库内容上传到远程库

- `git push first master`

  `first`为远程推送别名，`master`为本地的主干，在GitHub上的左上角分支选项里，把main改为master即可查看刚上传的文件

![image-20220126155837052](git%E7%AC%94%E8%AE%B0.assets/image-20220126155837052.png)

### 克隆

命令

- 此处使用HTTPS方式

  `git clone https://github.com/SimonOct/firstGit.git`

效果

- 完整地把远程库下载到本地
- 创建origin远程地址别名
- 初始化本地库

![image-20220126162151346](git%E7%AC%94%E8%AE%B0.assets/image-20220126162151346.png)

## 配置gpg

windows上安装git后直接可以z在git bash执行

```bash
gpg --full-generate-key
```

生成gpg密钥，在安装git后已经顺带安装好gpg

查看密钥信息

```bash
gpg --list-secret-keys --keyid-format LONG
```

根据密钥ID（sec那行）导出公钥，将信息完整复制后可以贴到github、gitlab等托管平台账号内的GPG处，2XXXXXXXXXXXXXX3是我的密钥id，不同密钥ID不相同

```bash
gpg --armor --export 2XXXXXXXXXXXXXX3
```

启动全局签名

```bash
git config --global commit.gpgsign true
```

导入github的gpg(可选，这步是为了在github端编辑commit后，在本地pull时看记录能显示已验证，其它平台的密钥自行搜寻)

```bash
curl https://github.com/web-flow.gpg | gpg --import
gpg --sign-key 4AEE18F83AFDEB23
```

导出密钥，将sec那行最长的字符串复制后执行export-secret-key

```bash
gpg --list-secret-keys --keyid-format LONG
gpg --export-secret-key AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX3 > simon.asc
```

导入密钥

```bash
gpg --import simon.asc
```

让Git知道签名所用的GPG密钥ID

```bash
git config --global user.signingkey {key_id}
```

