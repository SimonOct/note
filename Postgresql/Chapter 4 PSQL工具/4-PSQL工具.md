# PSQL工具

英文[文档](https://www.postgresql.org/docs/14/app-psql.html)

中文[文档](http://www.postgres.cn/docs/14/app-psql.html)

正體中文[文檔](https://docs.postgresql.tw/reference/client-applications/psql)

psql是一个PostgreSQL的基于终端的前端。它让你能交互式地键入查询，把它们发送给PostgreSQL，并且查看查询结果。或者，输入可以来自于一个文件或者命令行参数。此外，psql还提供一些元命令和多种类似 shell 的特性来为编写脚本和自动化多种任务提供便利

## `\l`查看数据库

进入到psql的命令交互输入模式使用`\l`命令查看有哪些数据库（我在Windows下运行SQL Shell）

```bash
postgres=# \l
                                                        数据库列表
   名称    |  拥有者  | 字元编码 |            校对规则            |             Ctype              |       存取权限
-----------+----------+----------+--------------------------------+--------------------------------+-----------------------
 postgres  | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |
 study     | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |
 template0 | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 | =c/postgres          +
           |          |          |                                |                                | postgres=CTc/postgres
 template1 | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 | =c/postgres          +
           |          |          |                                |                                | postgres=CTc/postgres
(4 行记录)
```

`postgres`数据库时PostgreSQL安装完成后默认创建的一个数据库，还有两个模板数据库`template0`和`template1`

当用户创建数据库时，默认是从模板数据库`template1`克隆来的，所以通常我们可以定制`template1`数据库中的内容

`template0`是一个最简化的模板库啊，如果创建数据库时明确指定从此数据库克隆，将创建一个最简化的数据库

## `\h`命令

```bash
\h or \help [ command ]
```

给出指定SQL命令的语法帮助。如果没有指定command，则psql会列出可以显示语法帮助的所有命令。如果command是一个星号（*），则会显示所有SQL命令的语法帮助。

与大部分其他元命令不同，该行的所有剩余部分总是会被当做\help的参数，并且在参数中不会执行变量篡改以及反引号展开。 

```bash
postgres=# \h alter table
命令：       ALTER TABLE
描述：       更改数据表的定义
语法：
ALTER TABLE [ IF EXISTS ] [ ONLY ] 名称 [ * ]
    操作 [, ... ]
...
```

## `\d`查看表

对于每一个匹配pattern的关系（表、视图、物化视图、索引、序列或者外部表）或者组合类型，显示所有的列、它们的类型、表空间（如果非默认表空间）以及任何诸如NOT NULL或者默认值的特殊属性。相关的索引、约束、规则以及触发器也会被显示。对于外部表，还会显示相关的外部服务器（下文的Patterns中定义了“匹配模式”）。

对于某些类型的关系，`\d`会为每一列显示额外的信息：对于序列会显示列值，对于索引显示被索引的表达式，对于外部表显示外部数据包装器选项。

命令形式`\d+`是一样的，不过会显示更多信息：与该表的列相关的任何注释，表中是否存在 OID，如果关系是视图则显示视图定义，非默认的replica identity设置。

默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。 

```bash
postgres=# \d
                 关联列表
 架构模式 |    名称    |  类型  |  拥有者
----------+------------+--------+----------
 public   | adult      | 数据表 | postgres
 public   | class      | 数据表 | postgres
 public   | class_info | 数据表 | postgres
 public   | grades     | 数据表 | postgres
 public   | score      | 数据表 | postgres
 public   | student    | 数据表 | postgres
(6 行记录)
```

```bash
postgres=# \d+
                                     关联列表
 架构模式 |    名称    |  类型  |  拥有者  | 持续的 | 访问方法 |    大小    | 描述
----------+------------+--------+----------+--------+----------+------------+------
 public   | adult      | 数据表 | postgres | 永久的 | heap     | 16 kB      |
 public   | class      | 数据表 | postgres | 永久的 | heap     | 8192 bytes |
 public   | class_info | 数据表 | postgres | 永久的 | heap     | 16 kB      |
 public   | grades     | 数据表 | postgres | 永久的 | heap     | 16 kB      |
 public   | score      | 数据表 | postgres | 永久的 | heap     | 0 bytes    |
 public   | student    | 数据表 | postgres | 永久的 | heap     | 8192 bytes |
(6 行记录)
```

如果使用\d但不带有pattern参数，它等价于\dtvmsE，后者将显示所有可见的表、视图、物化视图、序列和外部表的列表。这纯粹是一种便利措施。

`\timing`显示执行SQL语句的时间

```bash
postgres=# \timing on
启用计时功能.
postgres=# SELECT COUNT(*) FROM class;
 count
-------
     4
(1 行记录)


时间：7.627 ms
```

指定客户端字符集的命令

`\encoding`命令指定客户端的字符编码，如`\encoding gbk`

`SHOW client_encoding;`查看当前客户端编码

## `\pset`格式化输出

```bash
\pset [ option [ value ] ]
```

 这个命令设置影响查询结果表输出的选项。option表示要设置哪个选项。value的语义取决于选中的选项。对于某些选项，如果省略value会导致该选项值被切换或者被重置，具体是哪些选项可见特定选项的描述。如果没有上面提到的那种行为，那么省略value只会导致当前设置被显示。

不带任何参数的`\pset`显示所有打印选项的当前状态。 

介绍一下border选项

- `\pset border 0` 表示输出内容无边框
- `\pset border 1` 表示输出内容只有内边框
- `\pset border 3` 表示输出内容内外边框都有

```bash
postgres=# \pset border 0
边缘风格是 0.
postgres=# SELECT * FROM class;
no class_name
-- -----------
 1 初二（1）班
 2 初二（2）班
 3 初二（3）班
 4 初二（4）班
(4 行记录)
```

```bash
postgres=# \pset border 1
边缘风格是 1.
postgres=# SELECT * FROM class;
 no | class_name
----+-------------
  1 | 初二（1）班
  2 | 初二（2）班
  3 | 初二（3）班
  4 | 初二（4）班
(4 行记录)
```

```bash
postgres=# \pset border 2
边缘风格是 2.
postgres=# SELECT * FROM class;
+----+-------------+
| no | class_name  |
+----+-------------+
|  1 | 初二（1）班 |
|  2 | 初二（2）班 |
|  3 | 初二（3）班 |
|  4 | 初二（4）班 |
+----+-------------+
(4 行记录)
```

不管输出的内容加不加边框，内容本身都是对齐的，而有时我们需要把命令的结果输出为其它程序可以读取的文件，如以逗号分隔的文本文件，这时需要`\pset format unaligned`

```bash
postgres=# \pset format unaligned
输出格式是 unaligned.
postgres=# SELECT * FROM class;
no|class_name
1|初二（1）班
2|初二（2）班
3|初二（3）班
4|初二（4）班
(4 行记录)
```

默认分隔符是"\|"，可以使用`\pset fieldsep`设置分隔符

```bash
postgres=# \pset fieldsep ','
栏位分隔符号是 ",".
postgres=# SELECT * FROM class;
no,class_name
1,初二（1）班
2,初二（2）班
3,初二（3）班
4,初二（4）班
(4 行记录)
```

## `\o`将结果指定输出到文件中

```bash
\o or \out [ filename ]
\o or \out [ |command ]
```

 安排把未来的查询结果保存到文件filename中或者用管道导向到 shell 命令command。如果没有指定参数，查询输出会被重置到标准输出。

如果该参数以\|开始，则该行的所有剩余部分总是会被当做要执行的command，并且在参数中不会执行变量篡改以及反引号展开。该行的剩余部分会被简单地按字面传给shell。

“查询结果”包括从数据库服务器得到的所有表、命令响应和提示，还有查询数据库的各种反斜线命令（如`\d`）的输出，但不包括错误消息。 

## `\x`将按行展示的数据变成按列展示的数据

```bash
postgres=# \x
扩展显示已打开.
postgres=# \pset format aligned
输出格式是 aligned.
postgres=# SELECT * FROM class;
+-[ RECORD 1 ]-------------+
| no         | 1           |
| class_name | 初二（1）班 |
+-[ RECORD 2 ]-------------+
| no         | 2           |
| class_name | 初二（2）班 |
+-[ RECORD 3 ]-------------+
| no         | 3           |
| class_name | 初二（3）班 |
+-[ RECORD 4 ]-------------+
| no         | 4           |
| class_name | 初二（4）班 |
+------------+-------------+
```

## 执行存储在外部文件中的SQL命令

```bash
\i or \include filename
```

 从文件filename读取输入并且把它当作从键盘输入的命令来执行。

如果filename是`-`（连字符），那么会一直读取标准输入直到碰到一个 EOF 指示符或者`\q`元命令。这可以用来把交互式输入与文件输入混杂。注意只有在最外层激活了 readline 行为的情况下才将会使用 readline 行为。 

 如果想在屏幕上看到被读入的行，必须把变量ECHO设置成all。 

## 编辑命令

```bash
\e或\edit [ filename ] [ line_number ] 
```

 如果指定了filename，则它是被编辑的文件，在编辑器退出后，该文件的内容会被拷贝到当前查询缓冲区中。如果没有给定filename，当前查询缓冲区会被拷贝到一个临时文件中，并且接着以相同的方式编辑。或者，如果当前查询缓冲区为空，则最近被执行的查询会被拷贝到一个临时文件并且以同样的方式编辑。

然后会根据psql的一般规则重新解析查询缓冲区的新内容，把整个缓冲区当作一个单一行来处理。任何完整的查询都会立即执行； 也就是说，如果查询缓冲区包含分号或以分号结尾，则执行该点之前的所有内容并将其从查询缓冲区中删除。查询缓冲区中剩余的内容将重新显示。输入分号或者`\g`会把它发送出去，输入`\r`会通过清除查询缓冲区来取消它。

把缓冲区当作单一行主要会影响元命令：缓冲区中在一个元命令之后的任何东西都将被当作该元命令的参数，即便元命令之后的内容跨越多行也是如此。（因此不能以这种方式来制作使用元命令的脚本。应该使用\i。）

如果指定了一个行号，psql将会把游标（注意不是服务器端的游标）定位到文件或者查询缓冲区的指定行上。注意如果给出了一个全是数字的参数，psql就会假定它是行号而不是文件名。 

![image-20220224001056881](C:/Users/simon/AppData/Roaming/Typora/typora-user-images/image-20220224001056881.png)

输入`\e`命令后调用一个编辑器，在Linux下通常是Vi，在Windows可能是记事本。当退出编辑后将会执行编辑器内的语句，并且在psql中看不见执行了什么语句

```bash
\ef [ function_description [ line_number ] ] 
```

 这个命令会以一个CREATE OR REPLACE FUNCTION或CREATE OR REPLACE PROCEDURE命令的形式取出并且编辑指定函数或过程的定义。编辑的方式与`\edit`完全相同。在编辑器退出后，在编辑器退出后，则会立即执行更新的命令。否则重新显示；可以键入分号或者`\g`把它发出，也可以用`\r`取消之。

目标函数可以单独用名称或者用名称和参数（例如foo(integer, text)）来指定。如果有多于一个函数具有同样的名称，则必须给出参数的类型。

如果没有指定函数，将会给出一个空白的CREATE FUNCTION模板来编辑。

如果指定了一个行号，psql将把游标定位在该函数体的指定行上（注意函数体通常不是开始于文件的第一行）。

和大部分其他元命令不同，该行的整个剩余部分总是会被当作\ef的参数，并且在参数中不会执行变量篡改以及反引号展开。 

```bash
\ev [ view_name [ line_number ] ] 
```

 这个命令会以一个CREATE OR REPLACE VIEW的形式取出并且编辑指定函数的定义。编辑的方式与`\edit`完全相同。在编辑器退出后，如果向其添加分号，则会立即执行更新的命令。否则重新显示；可以键入分号或者`\g`把它发出，也可以用`\r`取消之。

如果没有指定函数，将会给出一个空白的CREATE VIEW模板来编辑。

如果指定了一个行号，psql将把游标定位在该视图定义的指定行上。

和大部分其他元命令不同，该行的整个剩余部分总是会被当作`\ev`的参数，并且在参数中不会执行变量篡改以及反引号展开。 

`\ef`和`\ev`命令可以用于查看函数或试图的定义，需要注意的是，退出编辑器后要在psql中输入`\reset`

来清除psql的命令缓冲区，防止误执行创建函数和视图的SQL语句

## 输出信息的`\echo`命令

```bash
\echo text [ ... ]
```

将经过计算的参数打印到标准输出，以空格分隔，后跟换行符。这可以用来在脚本的输出中间混入信息，例如： 

```bash
postgres=# \echo hello world
hello world
```

此命令通常用于在使用.sql脚本的文件中输出提示信息

更多的其它命令可以用`\?`命令来显示

## psql的使用技巧

psql是支持命令补全的，当然Windows上的不支持

### 自动提交技巧

在psql中事务是自动提交的，如果不想事务自动提交，方法有两种

一、使用`begin;`

运行`begin;`命令，然后执行DML语句，最后再执行`commit`或`rollback`语句

```bash
postgres=# begin;
BEGIN
时间：0.243 ms
postgres=*# UPDATE class SET class_name = '初二（3）班' WHERE no = 1;
UPDATE 1
时间：0.413 ms
postgres=*# SELECT * FROM class;
+----+-------------+
| no | class_name  |
+----+-------------+
|  2 | 初二（2）班 |
|  3 | 初二（3）班 |
|  4 | 初二（4）班 |
|  1 | 初二（3）班 |
+----+-------------+
(4 行记录)


时间：0.262 ms
postgres=*# rollback;
ROLLBACK
时间：0.200 ms
postgres=# SELECT * FROM class;
+----+-------------+
| no | class_name  |
+----+-------------+
|  2 | 初二（2）班 |
|  3 | 初二（3）班 |
|  4 | 初二（4）班 |
|  1 | 初二（1）班 |
+----+-------------+
(4 行记录)
```

方法二、直接关闭自动提交功能

```bash
\set AUTOCOMMIT off
```

`AUTOCOMMIT`自动提交该参数要大写才能生效，否则即使小写autocommit改为off，虽不报错但不生效
