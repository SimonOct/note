# SQL入门



由于已经将前几个月(2021年10月)学MySQL入门时学到的SQL语句忘得差不多了，这一章我不能跳过😢

这章用的示例语句分别由书本提供以及从[PostgreSQL Tutorial](https://www.postgresqltutorial.com/)拷贝

导入PostgreSQL Tutorial提供的[Sample database](https://www.postgresqltutorial.com/postgresql-sample-database/)，导入[方法](https://www.postgresqltutorial.com/load-postgresql-sample-database/)

## 语句分类

SQL命令一般分为DQL、DML、DDL三类

- DQL(Data Query Language)    数据查询语句，基本就是SELECT查询命令，用于数据查询
- DML(Data Manipulation Language)    即数据操纵语言，主要用于插入、更新、删除数据，所以也分为INSERT、UPDATE、DELETE三种语句
- DDL(Data Definition Language)    即数据定义语言，简单来说，是用于创建、删除、修改表、索引等数据库对象的语言

## DDL

### 建表语句

语法格式

```sql
CREATE TABLE table_name (
col01_name data_type,
col02_name data_type,
col03_name data_type,
...
coln_name data_type
);
```

书本实际创建表的代码

```sql
CREATE TABLE score (
student_name varchar(40),
chinese_score int,
math_score int,
test_date date
);
```

在psql中执行的效果

```bash
postgres=# create table score (
postgres(# student_name varchar(40),
postgres(# chinese_score int,
postgres(# math_score int,
postgres(# test_date date
postgres(# );
CREATE TABLE
```

使用`\d`显示数据库中有那些表

```bash
postgres=# \d
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | score | table | postgres
(1 row)
```

使用`\d score`可以显示这张表的定义情况

```bash
postgres=# \d score
                          Table "public.score"
    Column     |         Type          | Collation | Nullable | Default
---------------+-----------------------+-----------+----------+---------
 student_name  | character varying(40) |           |          |
 chinese_score | integer               |           |          |
 math_score    | integer               |           |          |
 test_date     | date                  |           |          |
```

加主键的话直接在data_type后面加上 `primary key`就好了，如

```sql
CREATE TABLE test_score (
student_id int primary key,
student_name varchar(40),
chinese_score int,
math_score int,
test_date date
);
```

```bash
postgres=# \d test_score
                       Table "public.test_score"
    Column     |         Type          | Collation | Nullable | Default
---------------+-----------------------+-----------+----------+---------
 student_id    | integer               |           | not null |
 student_name  | character varying(40) |           |          |
 chinese_score | integer               |           |          |
 math_score    | integer               |           |          |
 test_date     | date                  |           |          |
Indexes:
    "test_score_pkey" PRIMARY KEY, btree (student_id)
```

### 删除表语句

格式

`DROP TABLE table_name;`

实际使用

```bash
postgres=# DROP TABLE test_score;
DROP TABLE
```

## DML语句

创建一个表

```sql
CREATE TABLE student (no int primary key, student_name varchar(40), age int);
```

### 插入语句

依次填入no，student_name，age

```sql
INSERT INTO student VALUES (1, '张三', 14);
```

也可以只填一部分，未填的部分为NULL

```sql
INSERT INTO student(no, student_name) VALUES (2, '王二');
```

还可以指定插入数据时的顺序

```sql
INSERT INTO student(no, age, student_name) VALUES (3, 13, '李四');
```

查询数据

```bash
postgres=# select * from student ;
 no | student_name | age
----+--------------+-----
  1 | 张三       |  14
  2 | 王二       |
  3 | 李四       |  13
(3 rows)
```

### 更新语句

```sql
UPDATE student SET age = 15;
```

这个语句是将age列全部设置成15

```bash
postgres=# SELECT * FROM student;
 no | student_name | age
----+--------------+-----
  1 | 张三         |  15
  2 | 王二         |  15
  3 | 李四         |  15
(3 行记录)
```

如果需要指定某一行，则需要使用WHERE过滤

```sql
UPDATE student SET age = 14 WHERE no = 3;
```

```bash
postgres=# SELECT * FROM student;
 no | student_name | age
----+--------------+-----
  1 | 张三         |  15
  2 | 王二         |  15
  3 | 李四         |  14
(3 行记录)
```

也可以同时在同一行内更新多个列的值

```sql
UPDATE student SET age = 13 , student_name = '李五' WHERE no = 3;
```

```bash
postgres=# SELECT * FROM student;
 no | student_name | age
----+--------------+-----
  1 | 张三         |  15
  2 | 王二         |  15
  3 | 李五         |  13
(3 行记录)
```

### 删除语句

```sql
DELETE FROM student WHERE no = 3;
```

```bash
postgres=# SELECT * FROM student;
 no | student_name | age
----+--------------+-----
  1 | 张三         |  15
  2 | 王二         |  15
(2 行记录)
```

## 查询语句

基本的SELECT我还是记得的，因此这里就跳过

- 单表查询
- 条件查询(WHERE)
- 排序
- 别名

### 分页

这里介绍FETCH，作用与LIMIT一样，区别是FETCH是SQL标准而LIMIT不是

```sql
OFFSET start { ROW | ROWS }
FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY
```

在PostgreSQL中`OFFSET`（如果有）和`FETCH`顺序可以调换，但是SQL:2008要求OFFSET子句必须在FETCH子句之前，因此写的时候要`OFFSET`（如果有）在前，`FETCH`在后

`OFFSET`后面跟着的是从哪一行开始（不包含该行），如果不写默认从第零行开始

`FETCH`后面的`FIRST`或`NEXT`都可以，作用一样但必须有。row_count表示要多少行，不写则默认为1

如从第5行开始取10行

```sql
SELECT
    film_id,
    title
FROM
    film
ORDER BY
    title 
OFFSET 5 ROWS
FETCH FIRST 10 ROW ONLY; 
```

`ROW`和`ROWS`任选一个即可

```bash
 film_id |      title
---------+------------------
       6 | Agent Truman
       7 | Airplane Sierra
       8 | Airport Pollock
       9 | Alabama Devil
      10 | Aladdin Calendar
      11 | Alamo Videotape
      12 | Alaska Phantom
      13 | Ali Forever
      14 | Alice Fantasia
      15 | Alien Center
(10 行记录)
```

选从第一行开始，取一条数据

```sql
SELECT
    film_id,
    title
FROM
    film
ORDER BY
    title 
FETCH FIRST ROW ONLY;
```

```bash
 film_id |      title
---------+------------------
       1 | Academy Dinosaur
(1 行记录)
```

### 多表关联查询

先创建两个表（把上面创建的student表删除重建）

```sql
CREATE TABLE class(no INT PRIMARY KEY, class_name VARCHAR(40));
```

```sql
CREATE TABLE student(no INT PRIMARY KEY, student_name VARCHAR(40), age INT, class_no INT);
```

分别插入一些数据

```sql
INSERT INTO class VALUES (1, '初二（1）班');
INSERT INTO class VALUES (2, '初二（2）班');
INSERT INTO class VALUES (3, '初二（3）班');
INSERT INTO class VALUES (4, '初二（4）班');
```

```bash
postgres=# SELECT * FROM class;
 no | class_name
----+-------------
  1 | 初二（1）班
  2 | 初二（2）班
  3 | 初二（3）班
  4 | 初二（4）班
(4 行记录)
```

```sql
INSERT INTO student VALUES(1, '张三', 14, 1);
INSERT INTO student VALUES(2, '吴二', 15, 1);
INSERT INTO student VALUES(3, '李四', 13, 2);
INSERT INTO student VALUES(4, '吴三', 15, 2);
INSERT INTO student VALUES(5, '王二', 15, 3);
INSERT INTO student VALUES(6, '李三', 14, 3);
INSERT INTO student VALUES(7, '吴二', 15, 4);
INSERT INTO student VALUES(8, '张四', 14, 4);
```

```bash
postgres=# SELECT * FROM student;
 no | student_name | age | class_no
----+--------------+-----+----------
  1 | 张三         |  14 |        1
  2 | 吴二         |  15 |        1
  3 | 李四         |  13 |        2
  4 | 吴三         |  15 |        2
  5 | 王二         |  15 |        3
  6 | 李三         |  14 |        3
  7 | 吴二         |  15 |        4
  8 | 张四         |  14 |        4
(8 行记录)
```

假设想查询每个学生的名字与班级名称的关系，那么就需要关联查询两张表

```sql
SELECT student_name, class_name FROM student s, class c WHERE s.class_no = c.no;
```

结果

```
postgres=# SELECT student_name, class_name FROM student s, class c WHERE s.class_no = c.no;
 student_name | class_name
--------------+-------------
 张三         | 初二（1）班
 吴二         | 初二（1）班
 李四         | 初二（2）班
 吴三         | 初二（2）班
 王二         | 初二（3）班
 李三         | 初二（3）班
 吴二         | 初二（4）班
 张四         | 初二（4）班
(8 行记录)
```

#### 笛卡尔积错误

先看一下下面的多表查询语句

```sql
SELECT student_name, class_name FROM student, class;
```

结果

```bash
postgres=# SELECT student_name, class_name FROM student, class;
 student_name | class_name
--------------+-------------
 张三         | 初二（1）班
 吴二         | 初二（1）班
 李四         | 初二（1）班
 吴三         | 初二（1）班
 王二         | 初二（1）班
 李三         | 初二（1）班
 吴二         | 初二（1）班
 张四         | 初二（1）班
 张三         | 初二（2）班
 吴二         | 初二（2）班
 李四         | 初二（2）班
 吴三         | 初二（2）班
 王二         | 初二（2）班
 李三         | 初二（2）班
 吴二         | 初二（2）班
 张四         | 初二（2）班
 张三         | 初二（3）班
 吴二         | 初二（3）班
 李四         | 初二（3）班
 吴三         | 初二（3）班
 王二         | 初二（3）班
 李三         | 初二（3）班
 吴二         | 初二（3）班
 张四         | 初二（3）班
 张三         | 初二（4）班
 吴二         | 初二（4）班
 李四         | 初二（4）班
 吴三         | 初二（4）班
 王二         | 初二（4）班
 李三         | 初二（4）班
 吴二         | 初二（4）班
 张四         | 初二（4）班
(32 行记录)

```

这样的查询语句是错误的（与目的相悖），结果是每个学生与每个班级都匹配了一遍(4x8)。之所以称为笛卡尔积错误，是因为造成这种错误的方式与笛卡尔积相似

出错的原因有

- 缺少了多表的连接条件
- 连接条件（或关联条件）无效
- 目的就是要让表中所有行相互连接~~（这个就不算错误了）~~

SQL92中，笛卡尔积也称为`交叉连接`，英语是`CROSS JOIN`。在SQL99中也是使用CROSS JOIN表示交叉连接。它的作用是可以把任意表进行连接，即使这两张表不相关

```sql
SELECT student_name, class_name FROM student CROSS JOIN class;
```

这条语句的执行结果与上面的一致

多表查询的正确方式是需要**包含连接条件**

#### 多表查询的分类

分类方式一：等值连接与非等值连接

分类方式二：自连接与非自连接

分类方式三：内连接与外连接

##### 等值连接与非等值连接

非等值连接的例子

创建一个表

```sql
CREATE TABLE adult(is_adult VARCHAR, lowest_age INT, highest_age INT);
```

插入值

```sql
INSERT INTO adult VALUES ('adult', 18, 150);
INSERT INTO adult VALUES ('children', 0, 17);
```

```bash
postgres=# SELECT * FROM adult;
 is_adult | lowest_age | highest_age
----------+------------+-------------
 adult    |         18 |         150
 children |          0 |          17
(2 行记录)
```

查询一下学生年龄处在什么阶段

```sql
SELECT s.student_name, s.age, a.is_adult FROM student s, adult a WHERE s.age BETWEEN a.lowest_age AND a.highest_age;
```

```bash
postgres=# SELECT s.student_name, s.age, a.is_adult FROM student s, adult a WHERE s.age BETWEEN a.lowest_age AND a.highest_age ORDER BY s.no;
 student_name | age | is_adult
--------------+-----+----------
 张三         |  14 | children
 吴二         |  15 | children
 李四         |  13 | children
 吴三         |  15 | children
 王二         |  15 | children
 李三         |  14 | children
 吴二         |  15 | children
 张四         |  14 | children
(8 行记录)
```

全部都处在children的区间内，此时插入一个18岁与一个25岁的学生数据后再执行一次查询

```sql
INSERT INTO student VALUES (9, '王九', 18, 4);
INSERT INTO student VALUES (10, '李使', 25, 4);
```

```bash
postgres=# SELECT s.student_name, s.age, a.is_adult FROM student s, adult a WHERE s.age BETWEEN a.lowest_age AND a.highest_age ORDER BY s.no;
 student_name | age | is_adult
--------------+-----+----------
 张三         |  14 | children
 吴二         |  15 | children
 李四         |  13 | children
 吴三         |  15 | children
 王二         |  15 | children
 李三         |  14 | children
 吴二         |  15 | children
 张四         |  14 | children
 王九         |  18 | adult
 李使         |  25 | adult
(10 行记录)
```

`s.age BETWEEN a.lowest_age AND a.highest_age` 可以换成`s.age >= a.lowest_age AND s.age <= a.highest_age`，含义相同

##### 自连接与非自连接

自连接例子

创建一个表

```sql
CREATE TABLE class_info (school_id int, name varchar, teacher_id int);
```

插入数据

```sql
INSERT INTO class_info VALUES (1, '李珊珊');
INSERT INTO class_info VALUES (2, '王曙光');
INSERT INTO class_info VALUES (3, '张三', 1);
INSERT INTO class_info VALUES (4, '吴三', 1);
INSERT INTO class_info VALUES (5, '李四', 2);
INSERT INTO class_info VALUES (5, '张四', 2);
```

```bash
postgres=# SELECT * FROM class_info;
 school_id |  name  | teacher_id
-----------+--------+------------
         1 | 李珊珊 |
         2 | 王曙光 |
         3 | 张三   |          1
         4 | 吴三   |          1
         5 | 李四   |          2
         5 | 张四   |          2
(6 行记录)
```

查询学生id，学生姓名及其老师的id和姓名

```sql
SELECT stu.school_id student_id, stu.name student_name, te.school_id teacher_id, te.name teacher_name FROM class_info stu, class_info te WHERE stu.teacher_id = te.school_id;
```

```bash
postgres=# SELECT stu.school_id student_id, stu.name student_name, te.school_id teacher_id, te.name teacher_name FROM class_info stu, class_info te WHERE stu.teacher_id = te.school_id;
 student_id | student_name | teacher_id | teacher_name
------------+--------------+------------+--------------
          3 | 张三         |          1 | 李珊珊
          4 | 吴三         |          1 | 李珊珊
          5 | 李四         |          2 | 王曙光
          5 | 张四         |          2 | 王曙光
(4 行记录)
```

自连接就是同一个表连接自身的意思

##### 内连接与外连接

这里直接给定义以及语法示例，详情看下方的具体介绍

内连接指的是：合并具有同一列的两张及以上表的行，结果集里不包含一个表与其它表不匹配的行

外连接指的是：合并具有同一列的两张及以上表的行，结果集里除了包含一个表与其它表匹配的行外，还包含左表或右表里不匹配的行

- 左外连接(LEFT OUTTER JOIN)
- 右外连接(RIGHT OUTTER JOIN)
- 满外连接(FULL OUTTER JOIN)

语法举例：

先往`student`表中一个尚未安排班级的学生

```sql
INSERT INTO student VALUES(11, '张十一', 14);
```

```bash
postgres=# SELECT * FROM student;
 no | student_name | age | class_no
----+--------------+-----+----------
  1 | 张三         |  14 |        1
  2 | 吴二         |  15 |        1
  3 | 李四         |  13 |        2
  4 | 吴三         |  15 |        2
  5 | 王二         |  15 |        3
  6 | 李三         |  14 |        3
  7 | 吴二         |  15 |        4
  8 | 张四         |  14 |        4
  9 | 王九         |  18 |        4
 10 | 李使         |  25 |        4
 11 | 张十一       |  14 |
(11 行记录)
```

上面的多表联查都是内连接，那些就是SQL92语法

使用内连接与外连接查询学生班级具体名称

**内连接SQL99语法举例**

```sql
SELECT student_name, class_name FROM student s INNER JOIN class c ON s.class_no = c.no;
```

其中`INNER`可以被省略

```sql
SELECT student_name, class_name FROM student s JOIN class c ON s.class_no = c.no;
```

```bash
postgres=# SELECT student_name, class_name FROM student s JOIN class c ON s.class_no = c.no;
 student_name | class_name
--------------+-------------
 张三         | 初二（1）班
 吴二         | 初二（1）班
 李四         | 初二（2）班
 吴三         | 初二（2）班
 王二         | 初二（3）班
 李三         | 初二（3）班
 吴二         | 初二（4）班
 张四         | 初二（4）班
 王九         | 初二（4）班
 李使         | 初二（4）班
(10 行记录)
```

**外连接语法举例**

SQL92，postgresql与mysql不支持这种写法"(+)"

```sql
SELECT s.no, s.student_name, c.class_name FROM student s, class c WHERE s.class_no = c.no(+);
```

SQL99

```sql
SELECT s.no, s.student_name, c.class_name FROM student s LEFT OUTER JOIN class c ON s.class_no = c.no;
```

也可以省略`OUTER`，写成

```sql
SELECT s.no, s.student_name, c.class_name FROM student s LEFT JOIN class c ON s.class_no = c.no;
```

```bash
postgres=# SELECT s.no, s.student_name, c.class_name FROM student s LEFT JOIN class c ON s.class_no = c.no;
 no | student_name | class_name
----+--------------+-------------
  1 | 张三         | 初二（1）班
  2 | 吴二         | 初二（1）班
  3 | 李四         | 初二（2）班
  4 | 吴三         | 初二（2）班
  5 | 王二         | 初二（3）班
  6 | 李三         | 初二（3）班
  7 | 吴二         | 初二（4）班
  8 | 张四         | 初二（4）班
  9 | 王九         | 初二（4）班
 10 | 李使         | 初二（4）班
 11 | 张十一       |
(11 行记录)
```

### Joins

#### 内连接(INNER JOIN)

![PostgreSQL Join - Inner Join](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Inner-Join.png)

##### 使用PostgreSQL INNER JOIN链接两个表

`customer`与`payment`表的结构

![customer and payment tables](SQL%E5%85%A5%E9%97%A8.assets/customer-and-payment-tables.png)

在这些表中，每当用户付费后，一个新行就会随之在`payment`中创建

每个用户也许拥有一个或者多个payments，但是每个payment只能属于某一个客户

`customer_id`列用来联系这两个表的关系，下面有三种使用习惯，本人倾向使用别名，但无论哪种，输出的结果都应该是**一致**的

普通版

```sql
SELECT
	customer.customer_id,
	first_name,
	last_name,
	amount,
	payment_date
FROM
	customer
INNER JOIN payment 
    ON payment.customer_id = customer.customer_id
ORDER BY payment_date;
```

别名版，也有`customer as c`，`payment as p`这种表达方式

需要注意的是，起了别名后，本次查询就不能够使用customer指代`customer`表、payment指代`payment`表了

```sql
SELECT
	c.customer_id,
	first_name,
	last_name,
	amount,
	payment_date
FROM
	customer c
INNER JOIN payment p
	ON p.customer_id = c.customer_id
ORDER BY payment_date;
```

USING版

```sql
SELECT
	customer_id,
	first_name,
	last_name,
	amount,
	payment_date
FROM
	customer
INNER JOIN payment USING(customer_id)
ORDER BY payment_date;
```

**注意！**`customer.customer_id`或`c.customer_id`这样的表达方式是指明`customer_id`是源自哪张表的，因为能够发现`customer`与`payment`表都含有`customer_id`，如果不指明会报错

```bash
错误:  字段关联 "customer_id" 是不明确的
第2行customer_id,
```

执行结果：一共有14596 rows affected，此处展示部分

![image-20220219023742792](SQL%E5%85%A5%E9%97%A8.assets/image-20220219023742792.png)

##### 使用PostgreSQL INNER JOIN链接三个表

下面的图表说明了三张表的关系：`staff`, `payment`, `customer`

- 每位员工处理零或多个payments，并且每个payment只能由一位员工处理
- 每位顾客能创建零或多个payments，每个payment由一位顾客创建

![customer, payment and staff tables](SQL%E5%85%A5%E9%97%A8.assets/customer-payment-staff-tables.png)

下面链接三个表的语句，`INNER JOIN`的顺序可以替换

```sql
SELECT
	c.customer_id,
	c.first_name customer_first_name,
	c.last_name customer_last_name,
	s.first_name staff_first_name,
	s.last_name staff_last_name,
	amount,
	payment_date
FROM
	customer c
INNER JOIN payment p 
    ON p.customer_id = c.customer_id
INNER JOIN staff s 
    ON p.staff_id = s.staff_id
ORDER BY payment_date;
```

![image-20220219025911387](SQL%E5%85%A5%E9%97%A8.assets/image-20220219025911387.png)

#### 左外连接(LEFT OUTER JOIN)



[原教程](https://www.postgresqltutorial.com/postgresql-left-join/)，接下来是我的翻译

假设有两张表：`A`和`B`

![A and B tables](SQL%E5%85%A5%E9%97%A8.assets/A-and-B-tables1.png)

`A`表里的每一行可能在`B`表有零行或多行对应的行，而`B`表的每一行在`A`表只会有一行对应的行

要从`A`表中查询数据，这些数据在`B`表中不一定有相对应的记录，你可以使用`LEFT JOIN`子句。

下面的语句演示了连接`A`表与`B`表的左连接语法：

```sql
SELECT
	pka,
	c1,
	pkb,
	c2
FROM
	A
LEFT JOIN B ON pka = fka;
```

要左连接`A`表与`B`表，需要遵循下列的步骤：

- 首先，在两张表中指定`SELECT`子句中要查询的列
- 其次，在`FROM`子句指定左表(这里指的是`A`表)
- 最后，在`LEFT JOIN`子句指定右侧的表(这里指的是`B`表)并且在`ON`关键字后指定连接条件

`LEFT JOIN`子句从左表开始查询数据。对于左表的每一行，数据库将比较`pka`列与右表`fka`列每一行的值

如果这些值相等，`LEFT JOIN`子句就会创建一行包含`SELECT`子句中要查询的列的新行，并且把这行添加到结果集中

当这些值不相等，`LEFT JOIN`子句也会创建一行包含`SELECT`子句中要查询的列的新行。此外，数据库将来自右表的列填充为NULL

下面的维恩图(用圆表示集与集之间关系)说明了`LEFT JOIN`是如何工作的：

![PostgreSQL Join - Left Join](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Left-Join.png)

使用postgresql tutorial的示例数据库演示

查看下面的`film`和`inventory`表结构

![Film and Inventory tables](SQL%E5%85%A5%E9%97%A8.assets/film-and-inventory-tables.png)

`film`表的每一行在`inventory`表中可以有零或许多行。`inventory`表中的每一行在`film`表中都有且仅有一行

`film_id`列建立了`film`表和`inventory`表之间的联系

下面的语句使用`LEFT JOIN`子句来连接`film`表和`inventory`表

```sql
SELECT
	f.film_id,
	title,
	inventory_id
FROM
	film f
LEFT JOIN inventory i
   ON i.film_id = f.film_id
ORDER BY title;
```

![image-20220220021910257](SQL%E5%85%A5%E9%97%A8.assets/image-20220220021910257.png)

当`film`表中的某条记录在`inventory`表中没有匹配的记录时，这条记录的`inventory_id`列的值为NULL

![image-20220220022442231](SQL%E5%85%A5%E9%97%A8.assets/image-20220220022442231.png)

下面的语句添加了一个`WHERE`子句来查找不在库存中的影片

```sql
SELECT
	f.film_id,
	title,
	inventory_id
FROM
	film f
LEFT JOIN inventory i
   ON i.film_id = f.film_id
WHERE i.film_id IS NULL
ORDER BY title;
```

USING版

```sql
SELECT
	f.film_id,
	title,
	inventory_id
FROM
	film f
LEFT JOIN inventory i USING (film_id)
WHERE i.film_id IS NULL
ORDER BY title;
```

![image-20220220022719014](SQL%E5%85%A5%E9%97%A8.assets/image-20220220022719014.png)

下面的维恩图说明是这语句是如何工作的：

![PostgreSQL Join - Left Join with Where](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Left-Join-with-Where.png)

当你想从一个表中选择在另一个表中没有匹配行的行时，这种技术很有用

#### 右外连接(RIGHT OUTER JOIN)

先创建两张表，`films`与`film_reviews`

```sql
DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS film_reviews;

CREATE TABLE films(
   film_id SERIAL PRIMARY KEY,
   title varchar(255) NOT NULL
);

INSERT INTO films(title)
VALUES('Joker'),
      ('Avengers: Endgame'),
      ('Parasite');

CREATE TABLE film_reviews(
   review_id SERIAL PRIMARY KEY,
   film_id INT,
   review VARCHAR(255) NOT NULL	
);

INSERT INTO film_reviews(film_id, review)
VALUES(1, 'Excellent'),
      (1, 'Awesome'),
      (2, 'Cool'),
      (NULL, 'Beautiful');
```

一部电影可以有零次或多次评价，一次评价属于零部或一部电影。`films`中的`film_id`列引用`film_reviews`表中的`film_id`列

查看`films`与`film_id`的内容

```sql
SELECT * FROM films;
```

```bash
study=# SELECT * FROM films;
 film_id |       title
---------+-------------------
       1 | Joker
       2 | Avengers: Endgame
       3 | Parasite
(3 行记录)
```

```sql
SELECT * FROM film_reviews;
```

```bash
study=# SELECT * FROM film_reviews;
 review_id | film_id |  review
-----------+---------+-----------
         1 |       1 | Excellent
         2 |       1 | Awesome
         3 |       2 | Cool
         4 |         | Beautiful
(4 行记录)
```

下面使用`RIGHT JOIN`语句从`films`和`film_reviews`表中查询数据

```sql
SELECT 
   review, 
   title
FROM 
   films
RIGHT JOIN film_reviews 
   ON film_reviews.film_id = films.film_id;
```

USING版

```sql
SELECT review, title
FROM films
RIGHT JOIN film_reviews USING (film_id);
```

```bash
  review   |       title
-----------+-------------------
 Excellent | Joker
 Awesome   | Joker
 Cool      | Avengers: Endgame
 Beautiful |
(4 行记录)
```

在这个语句中，`films`是左表，`film_reviews`是右表

`RIGHT JOIN`子句开始从右表（film_reviews）查询数据

对于右表（film_reviews）的每一条记录，它检查`film_reviews`表的`film_id`列的值是否等于左表（films）每一条记录的`film_id`列的值

如果它们相等，`RIGHT JOIN`会创建一条新的记录，包含SELECT子句中指定的两个表的列，并将这条新的记录包含在结果集中

否则，RIGHT JOIN仍然会创建一条新的记录，包含来自两个表的列，并将这条新的记录包括在结果集中。然而，它将左表的列（film）填充为NULL

换句话说，`RIGHT JOIN`选择右表的所有记录，无论它们是否与左表的记录匹配

下面的维恩图说明了`RIGHT JOIN`是如何工作的：

![PostgreSQL Join - Right Join](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Right-Join.png)

为了从右表中找到在左表中没有任何对应记录的记录，你可以添加一个WHERE子句

```sql
SELECT review, title
FROM films
RIGHT JOIN film_reviews using (film_id)
WHERE title IS NULL;
```

```bash
  review   | title
-----------+-------
 Beautiful |
(1 行记录)
```

下面的维恩图说明是这语句是如何工作的：

![PostgreSQL Join - Right Join with Where](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Right-Join-with-Where.png)

#### 满外连接(FULL OUTER JOIN)

MySQL不支持这个，如果想要实现FULL JOIN则可以使用`UNION`将左连接右连接拼起来，以达到FULL JOIN的效果

语法示例：

```sql
SELECT * FROM A
FULL [OUTER] JOIN B on A.id = B.id;
```

- 在这个语法中，`OUTER`关键字是可选的
- 全外连接结合了左连接和右连接的结果
- 如果连接的表中的行不匹配，全外连接为没有匹配行的表中的每一列设置NULL值
- 如果一个表中的行与另一个表中的行相匹配，那么结果行将包含由两个表中的行的列填充的列

下面的维恩图说明了`FULL OUTER JOIN`是如何工作的：

![PostgreSQL Join - Full Outer Join](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Full-Outer-Join.png)

PostgreSQL FULL OUTER JOIN示例

为演示创建两张表：`employees` 与 `departments`

```sql
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;

CREATE TABLE departments (
	department_id serial PRIMARY KEY,
	department_name VARCHAR (255) NOT NULL
);

CREATE TABLE employees (
	employee_id serial PRIMARY KEY,
	employee_name VARCHAR (255),
	department_id INTEGER
);
```

每个部门有零位或多位雇员，每位雇员属于零个或一个部门

第二，在`employees`和`departments`表中插入一些样本数据

```sql
INSERT INTO departments (department_name)
VALUES
	('Sales'),
	('Marketing'),
	('HR'),
	('IT'),
	('Production');

INSERT INTO employees (
	employee_name,
	department_id
)
VALUES
	('Bette Nicholson', 1),
	('Christian Gable', 1),
	('Joe Swank', 2),
	('Fred Costner', 3),
	('Sandra Kilmer', 4),
	('Julia Mcqueen', NULL);
```

第三，从`employees`和`departments`表查询数据

```sql
SELECT * FROM departments;
```

```bash
 department_id | department_name
---------------+-----------------
             1 | Sales
             2 | Marketing
             3 | HR
             4 | IT
             5 | Production
(5 行记录)
```

```sql
SELECT * FROM employees;
```

```bash
 employee_id |  employee_name  | department_id
-------------+-----------------+---------------
           1 | Bette Nicholson |             1
           2 | Christian Gable |             1
           3 | Joe Swank       |             2
           4 | Fred Costner    |             3
           5 | Sandra Kilmer   |             4
           6 | Julia Mcqueen   |
(6 行记录)
```

第四，使用`FULL OUTER JOIN`来查询`employees`和`departments`两个表的数据

```sql
SELECT
	employee_name,
	department_name
FROM
	employees e
FULL OUTER JOIN departments d 
        ON d.department_id = e.department_id;
```

```bash
  employee_name  | department_name
-----------------+-----------------
 Bette Nicholson | Sales
 Christian Gable | Sales
 Joe Swank       | Marketing
 Fred Costner    | HR
 Sandra Kilmer   | IT
 Julia Mcqueen   |
                 | Production
(7 行记录)
```

结果集包括每个属于某个部门的雇员和每个有雇员的部门。此外，它还包括每个不属于某个部门的雇员和每个没有雇员的部门

为了找到没有任何雇员的部门，可以使用如下的WHERE子句

```sql
SELECT
	employee_name,
	department_name
FROM
	employees e
FULL OUTER JOIN departments d 
        ON d.department_id = e.department_id
WHERE
	employee_name IS NULL;
```

也可以使用右连接实现

```sql
SELECT
	employee_name,
	department_name
FROM
	employees e
RIGHT JOIN departments d
	ON e.department_id = d.department_id
WHERE
	e.employee_name IS NULL;
```

```bash
 employee_name | department_name
---------------+-----------------
               | Production
(1 行记录)
```

结果显示，Production部门没有任何雇员



为了找到不属于任何部门的雇员，可以在WHERE子句中检查部门名称是否为NULL

```sql
SELECT
	employee_name,
	department_name
FROM
	employees e
FULL OUTER JOIN departments d ON d.department_id = e.department_id
WHERE
	department_name IS NULL;
```

也可以使用左连接实现

```sql
SELECT
	employee_name,
	department_name
FROM
	employees e
LEFT JOIN departments d
	ON e.department_id = d.department_id
WHERE
	d.department_name IS NULL;
```

```bash
 employee_name | department_name
---------------+-----------------
 Julia Mcqueen |
(1 行记录)
```

结果显示，Julia Mcqueen不属于任何部门



想要一次查询没有员工的部门以及没有部分的员工

```sql
SELECT
	employee_name,
	department_name
FROM
	employees e
FULL OUTER JOIN departments d 
        ON d.department_id = e.department_id
WHERE
	employee_name IS NULL OR department_name IS NULL;
```

```bash
 employee_name | department_name
---------------+-----------------
 Julia Mcqueen |
               | Production
(2 行记录)
```

下面的维恩图说明是这语句是如何工作的：

![PostgreSQL Join - Full Outer Join with Where](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Join-Full-Outer-Join-with-Where.png)

下面的维恩图综合展示了内连接，左外连接，右外连接与满外连接共七种情况

![PostgreSQL Joins](SQL%E5%85%A5%E9%97%A8.assets/PostgreSQL-Joins.png)

#### 自然连接(NATURAL JOIN)

SQL99在SQL92的基础上提供了一些特殊语法，比如`NATURAL JOIN`用来表示自然连接。我们可以把自然连接理解为SQL92中的等值连接。它会自动查询两张连接表中**所有相同的字段**，然后进行**等值连接**

示例，先创建两张表

```sql
DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
	category_id serial PRIMARY KEY,
	category_name VARCHAR (255) NOT NULL
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	product_id serial PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	category_id INT NOT NULL,
	FOREIGN KEY (category_id) REFERENCES categories (category_id)
);
```

每个类别有零个或多个产品，每个产品属于一个且仅属于一个类别

`products`表中的`category_id`列是引用`category`表的主键的外键。`category_id`是我们将用来执行自然连接的公共列

向表插入一些数据

```sql
INSERT INTO categories (category_name)
VALUES
	('Smart Phone'),
	('Laptop'),
	('Tablet');

INSERT INTO products (product_name, category_id)
VALUES
	('iPhone', 1),
	('Samsung Galaxy', 1),
	('HP Elite', 2),
	('Lenovo Thinkpad', 2),
	('iPad', 3),
	('Kindle Fire', 3);
```

下面的语句使用NATURAL JOIN子句来连接`products`表和`category`表

```sql
SELECT * FROM products
NATURAL JOIN categories;
```

USING版

```sql
SELECT	* FROM products
INNER JOIN categories USING (category_id);
```

```bash
 category_id | product_id |  product_name   | category_name
-------------+------------+-----------------+---------------
           1 |          1 | iPhone          | Smart Phone
           1 |          2 | Samsung Galaxy  | Smart Phone
           2 |          3 | HP Elite        | Laptop
           2 |          4 | Lenovo Thinkpad | Laptop
           3 |          5 | iPad            | Tablet
           3 |          6 | Kindle Fire     | Tablet
(6 行记录)
```

`NATURAL JOIN`的方便之处在于它不需要你指定连接子句，因为它使用了一个基于公共列的隐含连接子句

然而，你应该尽可能避免使用`NATURAL JOIN`，因为有时它可能会导致一个意外的结果

例子，查看sample database的`city` 与 `country`表

![img](SQL%E5%85%A5%E9%97%A8.assets/city.png)

![img](SQL%E5%85%A5%E9%97%A8.assets/country.png)

两个表都有相同的`country_id`列，所以你可以使用`NATURAL JOIN`来连接这些表，如下所示

```sql
SELECT * 
FROM city
NATURAL JOIN country;
```

```bash
 country_id | last_update | city_id | city | country
------------+-------------+---------+------+---------
(0 行记录)
```

该查询返回一个空的结果集

原因是这两个表还有一个共同的列，叫做`last_update`，这个列不能用于连接。然而，`NATURAL JOIN`子句只是使用了`last_update`列

修改一下，使用内连接方式

```
SELECT * 
FROM city
INNER JOIN country USING (country_id) ORDER BY country;
```

![image-20220220060804383](SQL%E5%85%A5%E9%97%A8.assets/image-20220220060804383.png)

### 函数

PostgreSQL为内建的数据类型提供了大量的函数和操作符。 用户也可以定义它们自己的函数和操作符， 如[第 V 部分](https://www.postgresql.org/docs/14/server-programming.html)所述。psql命令`\df`和`\do`可以分别被用于显示所有可用的函数和操作符的列表

如果你关心移植性，那么请注意，我们在本章描述的大多数函数和操作符， 除了最琐碎的算术和比较操作符以及一些做了明确标记的函数以外，都没有在SQL标准里声明。某些这种扩展的功能也出现在许多其它SQL数据库管理系统中，并且在很多情况下多个实现的这种功能是相互兼容的和一致的。本章也并没有穷尽一切信息；一些附加的函数在本手册的相关小节里出现

英文[文档](https://www.postgresql.org/docs/14/functions.html)

简体中文[文档](http://www.postgres.cn/docs/14/functions.html)

正體中文[文檔](https://docs.postgresql.tw/the-sql-language/functions-and-operators)

这里演示部分函数，更具体的放在第五章结合数据类型

#### 单行函数

- 操作数据对象
- 接收参数返回一个结果
- 只对一行进行变换
- 每行返回一个结果
- 可以嵌套
- 参数可以是一列或一个值

##### 基本函数

```sql
SELECT
ABS(-123),ABS(32),SIGN(-23),SIGN(43),PI(),CEIL(32.32),CEILING(-43.23),FLOOR(32.32),FLOOR(-43.23),MOD(12,5);
```

![image-20220221015510844](SQL%E5%85%A5%E9%97%A8.assets/image-20220221015510844.png)

| 函数                                                         | 描述                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| abs ( numeric_type ) → numeric_type                          | 绝对值                                                  |
| sign ( numeric ) → numeric <br /> sign ( double precision ) → double precision | 参数的符号 (-1, 0, 或 +1)                               |
| pi ( ) → double precision                                    | π的近似值                                               |
| ceil ( numeric ) → numeric <br /> ceil ( double precision ) → double precision | 大于或等于参数的最接近的整数                            |
| ceiling ( numeric ) → numeric <br /> ceiling ( double precision ) → double precision | 大于或等于参数的最接近的整数 (与 ceil 相同)             |
| floor ( numeric ) → numeric <br /> floor ( double precision ) → double precision | 小于或等于参数的最接近整数                              |
| mod ( y numeric_type, x numeric_type ) → numeric_type        | y/x的余数； 适用于smallint、integer、bigint、和 numeric |

```sql
SELECT RANDOM(),RANDOM(),RANDOM(),RANDOM();
```

![image-20220221021422772](SQL%E5%85%A5%E9%97%A8.assets/image-20220221021422772.png)

| 函数                                | 描述                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| random ( ) → double precision       | 返回一个范围 0.0 <= x < 1.0 中的随机值                       |
| setseed ( double precision ) → void | 为后续的random()调用设置种子；参数必须在-1.0和1.0之间，包括边界值 |

`random()`函数使用了一个简单的线性共轭算法。它的速度很快，但不适合于密码学应用；如果`setseed()`被调用，那么当前会话中的一系列后续`random()`调用的结果能够通过使用相同的参数重新发布`setseed()`来重复

需要注意的是，如果种子设置成一样，那么生成的随机数也是相同的

```sql
SELECT
ROUND(12.33),ROUND(12.343,2),ROUND(12.324,-1),TRUNC(12.66,1),TRUNC(12.66,-1);
```

![image-20220221022242235](SQL%E5%85%A5%E9%97%A8.assets/image-20220221022242235.png)

| 函数                                                         | 描述                         |
| ------------------------------------------------------------ | ---------------------------- |
| round ( numeric ) → numeric<br />round ( double precision ) → double precision | 四舍五入到最近的整数         |
| round ( v numeric, s integer ) → numeric                     | 把 v 四舍五入到 s 位小数     |
| trunc ( numeric ) → numeric<br />trunc ( double precision ) → double precision | 截断整数 (向零靠近)          |
| trunc ( v numeric, s integer ) → numeric                     | 截断 v 到 s 位小数位置的数字 |

##### 字符串函数

| 函数                                                         | 描述                                                         | 示例                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ascii ( text ) → integer                                     | 返回参数的第一个字符的数字代码。在UTF8编码中，返回该字符的Unicode代码点。 在其他多字节编码中，该参数必须是一个ASCII字符。 | ascii('x') → 120                                             |
| char_length ( text ) → integer<br />character_length ( text ) → integer | 返回字符串中的字符数。                                       | char_length('josé') → 4                                      |
| length ( text ) → integer                                    | 返回字符串中的字符数。                                       | length('jose') → 4                                           |
| concat ( val1 "any" [, val2 "any" [, ...] ] ) → text         | 连接所有参数的文本表示。空参数被忽略。                       | concat('abcde', 2, NULL, 22) → abcde222                      |
| concat_ws ( sep text, val1 "any" [, val2 "any" [, ...] ] ) → text | 用分隔符连接除第一个参数外的所有参数。第一个参数用作分隔符字符串，不应为NULL。其他NULL参数将被忽略。 | concat_ws(',', 'abcde', 2, NULL, 22) → abcde,2,22            |
| overlay ( string text PLACING newsubstring text FROM start integer [ FOR count integer ] ) → text | 替换string从start字符开始的子串，并用newsubstring扩展到count字符。 如果省略了count，则默认为newsubstring的长度。 | overlay('Txxxxas' placing 'hom' from 2 for 4) → Thomas       |
| replace ( string text, from text, to text ) → text           | 将string 中当前的子串from替换为子串to。                      | replace('abcdefabcdef', 'cd', 'XX') → abXXefabXXef           |
| upper ( text ) → text                                        | 根据数据库的定位规则，将字符串转换为所有大写。               | upper('tom') → TOM                                           |
| lower ( text ) → text                                        | 根据数据库的语言环境规则，将字符串转换为全部小写。           | lower('TOM') → tom                                           |
| initcap ( text ) → text                                      | 将每个单词的第一个字母转换为大写，其余字母转换为小写。单词是由非字母数字字符分隔的字母数字字符序列。 | initcap('hi THOMAS') → Hi Thomas                             |
| left ( string text, n integer ) → text                       | 以字符串返回第一个 n 字符，或在 n 为负时, 返回最后n的绝对值个字符之外的全部字符 | left('abcde', 2) → ab                                        |
| right ( string text, n integer ) ) → text                    | 返回字符串中的最后n个字符，或者在n>为负时，返回除了前面的n的绝对值字符之外的全部字符 | right('abcde', 2) → de                                       |
| lpad ( string text, length integer [, fill text ] ) → text   | 将string扩展为长度length，通过前置字符fill（默认空格）。 如果string已经超过length那么它将被截断（在右侧）。 | lpad('hi', 5, 'xy') → xyxhi                                  |
| rpad ( string text, length integer [, fill text ] ) ) → text | 扩展 string 到长度 length，通过追加fill 字符(默认为空格). 如果string 已经比 length 长，则截断它。 | rpad('hi', 5, 'xy') → hixyx                                  |
| ltrim ( string text [, characters text ] ) → text            | 从string开始删除包含characters（默认空格）中仅包含字符的最长字符串。 | ltrim('zzzytest', 'xyz') → test                              |
| rtrim ( string text [, characters text ] ) → text            | 从string末尾删除包含characters（默认为空格）中仅包含字符的最长字符串。 | rtrim('testxxzx', 'xyz') → test                              |
| trim ( [ LEADING \| TRAILING \| BOTH ] [ characters text ] FROM string text ) → text | 从string的开始、末端或两端(默认为BOTH )移除仅包含characters(默认为空格)字符的最长字符串。 | trim(both 'xyz' from 'yxTomxx') → Tom                        |
| trim ( [ LEADING \| TRAILING \| BOTH ] [ FROM ] string text [, characters text ] ) → text | 这是一个非标准的trim()语法。                                 | trim(both from 'yxTomxx', 'xyz') → Tom                       |
| repeat ( string text, number integer ) → text                | 重复string指定number的次数。                                 | repeat('Pg', 4) → PgPgPgPg                                   |
| reverse ( text ) → text                                      | 颠倒字符串中字符的顺序。                                     | reverse('abcde') → edcba                                     |
| substr ( string text, start integer [, count integer ] ) → text | 提取string从start字符开始的子字符串，并扩展count字符，如果指定了的话。 (与 子字符串(string 从 start 开始计数 count)相同。) | substr('alphabet', 3) → phabet <br /> substr('alphabet', 3, 2) → ph |

关于计算字符串中的字符数的函数，`length`、`char_length` 与 `character_length` 效果都一样

部分函数使用示例

`OVERLAY`函数与MySQL的`INSERT`函数作用相似

```sql
SELECT OVERLAY ('helloworld' PLACING 'aaaaa' FROM 2 for 3);
```

```bash
   overlay
--------------
 haaaaaoworld
(1 行记录)
```

```sql
SELECT REPLACE ('hello', 'll', 'mmm');
```

```bash
study=# SELECT REPLACE ('hello', 'll', 'mmm');
 replace
---------
 hemmmo
(1 行记录)
```

可以使用`LPAD`与`RPAD`实现类似左右对齐的效果

先查看`actor`表

```bash
study=# SELECT first_name FROM actor OFFSET 10 ROWS FETCH FIRST 10 ROW ONLY;
 first_name
------------
 Zero
 Karl
 Uma
 Vivien
 Cuba
 Fred
 Helen
 Dan
 Bob
 Lucille
(10 行记录)
```

左对齐不明显，这里演示右对齐

```bash
study=# SELECT LPAD(first_name, 10) FROM actor OFFSET 10 ROWS FETCH FIRST 10 ROW ONLY;
    lpad
------------
       Zero
       Karl
        Uma
     Vivien
       Cuba
       Fred
      Helen
        Dan
        Bob
    Lucille
(10 行记录)
```

#### 聚合函数/聚集函数

上一节讲到了 SQL 单行函数。实际上 SQL 函数还有一类，叫做聚合（或聚集、分组）函数，它是对
一组数据进行汇总的函数，输入的是一组数据的集合，输出的是单个值

注意，PostgreSQL/MySQL聚合函数不允许嵌套使用(Oracle可以)，想要达到嵌套的效果，可以使用子查询实现

```bash
错误:  不允许嵌套调用聚合函数
第5行MIN(AVG (amount))
```

不过`MIN(AVG (amount))`可以用`ORDER BY + FETCH NEXT ONLY`得出😉

##### 常用的几个聚合函数

| 函数                                                         | 描述                                                         | 部分模式 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| avg ( smallint ) → numeric<br/><br/>avg ( integer ) → numeric<br/><br/>avg ( bigint ) → numeric<br/><br/>avg ( numeric ) → numeric<br/><br/>avg ( real ) → double precision<br/><br/>avg ( double precision ) → double precision<br/><br/>avg ( interval ) → interval | 计算所有非空输入值的平均值(算术平均值)。                     | Yes      |
| sum ( smallint ) → bigint<br/><br/>sum ( integer ) → bigint<br/><br/>sum ( bigint ) → numeric<br/><br/>sum ( numeric ) → numeric<br/><br/>sum ( real ) → real<br/><br/>sum ( double precision ) → double precision<br/><br/>sum ( interval ) → interval<br/><br/>sum ( money ) → money | 计算非空输入值的总和。                                       | Yes      |
| max ( see text ) → same as input type                        | 计算非空输入值的最大值。适用于任何数字、字符串、日期/时间或enum类型， 以及inet, interval, money, oid, pg_lsn,tid和任何这些类型的数组。 | Yes      |
| min ( see text ) → same as input type                        | 计算非空输入值的最小值。可用于任何数字、字符串、日期/时间或enum类型， 以及inet, interval,money, oid, pg_lsn,tid和任何这些类型的数组。 | Yes      |
| count ( * ) → bigint                                         | 计算输入行的数量。                                           | Yes      |
| count ( "any" ) → bigint                                     | 计算输入值不为空的输入行的数量。                             | Yes      |

###### AVG()与SUM()函数

`AVG()`函数是PostgreSQL中最常用的聚合函数之一。`AVG()`函数允许你计算一个集合的平均数值

你可以在SELECT和`HAVING`语句中使用`AVG()`函数

我们将使用dvdrental示例数据库中的以下`payment`表进行演示

![payment table](SQL%E5%85%A5%E9%97%A8.assets/payment-table.png)

如果你想知道客户支付的平均金额，你可以对金额列应用`AVG()`函数

```sql
SELECT AVG(amount)
FROM payment;
```

```bash
        avg
--------------------
 4.2006056453822965
(1 行记录)
```

为了使输出结果更易读，你可以使用cast操作符

```sql
SELECT AVG(amount)::numeric(10,2) 
FROM payment;
```

```bash
 avg
------
 4.20
(1 行记录)
```

要计算一个集合中不同数值的平均值，你可以使用`DISTINCT`选项

```sql
SELECT AVG(DISTINCT amount)::numeric(10,2)
FROM payment;
```

```bash
 avg
------
 6.14
(1 行记录)
```

下面的查询同时使用`SUM()`和`AVG()`函数来计算客户的付款总额和所有交易的平均值

```sql
SELECT
	AVG(amount)::numeric(10,2),
	SUM(amount)::numeric(10,2)
FROM
	payment;
```

```bash
 avg  |   sum
------+----------
 4.20 | 61312.04
(1 行记录)
```

为了计算一个组的平均值，你可以使用`AVG()`函数和`GROUP BY`子句。首先，`GROUP BY`子句将表的行分成组，然后将`AVG()`函数应用于每个组

下面的例子使用带`GROUP BY`子句的`AVG()`函数来计算每个客户支付的平均金额

```sql
SELECT
	customer_id,
	first_name,
	last_name,
	AVG (amount)::NUMERIC(10,2)
FROM
	payment
INNER JOIN customer USING(customer_id)
GROUP BY
	customer_id
ORDER BY
	customer_id
OFFSET 100 ROWS
FETCH FIRST 5 ROWS ONLY;
```

```bash
 customer_id | first_name | last_name | avg
-------------+------------+-----------+------
         101 | Peggy      | Myers     | 3.77
         102 | Crystal    | Ford      | 4.32
         103 | Gladys     | Hamilton  | 4.44
         104 | Rita       | Graham    | 3.54
         105 | Dawn       | Sullivan  | 4.26
(5 行记录)
```

你可以在`HAVING`子句中使用`AVG()`函数，根据某个条件来过滤这个组。例如，对于所有客户，你可以得到平均付款额大于5美元的客户。下面的查询可以帮助你做到这一点

```sql
SELECT
	customer_id,
	first_name,
	last_name,
	AVG (amount)::NUMERIC(10,2)
FROM
	payment
INNER JOIN customer USING(customer_id)
GROUP BY
	customer_id
HAVING
	AVG (amount) > 5
ORDER BY
	customer_id
FETCH FIRST 5 ROWS ONLY;
```

```bash
 customer_id | first_name | last_name | avg
-------------+------------+-----------+------
           3 | Linda      | Williams  | 5.45
          19 | Ruth       | Martinez  | 5.49
         137 | Rhonda     | Kennedy   | 5.04
         181 | Ana        | Bradley   | 5.08
         187 | Brittany   | Riley     | 5.62
(5 行记录)
```

这个查询与上面的查询类似，增加了一个`HAVING`子句。我们在`HAVING`子句中使用`AVG()`函数来过滤那些平均金额小于或等于5的组

`AVG()`、`SUM()`函数会忽略`NULL`值，意味着含有`NULL`值的行不会参与这些函数计算

###### MAX()函数

PostgreSQL 的 `MAX()` 函数是一个集合函数，它返回一组数值中的最大值。`MAX()`函数在很多情况下都很有用。例如，你可以用`MAX()`函数来查找工资最高的员工，或者查找最贵的产品等

```sql
SELECT MAX(amount)
FROM payment;
```

```bash
  max
-------
 11.99
(1 行记录)
```

为了获得最高付款的其他信息，你可以使用一个子查询

```sql
SELECT * FROM payment
WHERE amount = (
   SELECT MAX (amount)
   FROM payment
);
```

```bash
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date
------------+-------------+----------+-----------+--------+----------------------------
      20403 |         362 |        1 |     14759 |  11.99 | 2007-03-21 21:57:24.996577
      22650 |         204 |        2 |     15415 |  11.99 | 2007-03-22 22:17:22.996577
      23757 |         116 |        2 |     14763 |  11.99 | 2007-03-21 22:02:26.996577
      24553 |         195 |        2 |     16040 |  11.99 | 2007-03-23 20:47:59.996577
      24866 |         237 |        2 |     11479 |  11.99 | 2007-03-02 20:46:39.996577
      28799 |         591 |        2 |      4383 |  11.99 | 2007-04-07 19:14:17.996577
      28814 |         592 |        1 |      3973 |  11.99 | 2007-04-06 21:26:57.996577
      29136 |          13 |        2 |      8831 |  11.99 | 2007-04-29 21:06:07.996577
(8 行记录)
```

首先，子查询使用`MAX()`函数返回最高付款额，然后外部查询选择所有金额与子查询返回的最高付款额相同的行

从两列或多列中找出最大的数值

首先，创建一个名为 `ranks` 的新表，由四列组成：第一列存储用户ID，其他三列存储从1到3的等级

```sql
DROP TABLE IF EXISTS ranks;
CREATE TABLE ranks (
	user_id INT PRIMARY KEY,
	rank_1 INT NOT NULL,
	rank_2 INT NOT NULL,
	rank_3 INT NOT NULL
);
```

往里插入一些数据

```sql
INSERT INTO ranks
VALUES
	(1, 6, 3, 5),
	(2, 2, 8, 5),
	(3, 5, 9, 8);
```

为了实现这一点，你可以使用`GREATEST()`函数而不是`MAX()`函数。`GREATEST()`函数从一个值的列表中返回最大的值

```sql
SELECT
	user_id,
	GREATEST (rank_1, rank_2, rank_3) AS largest_rank
FROM
	ranks;
```

```bash
 user_id | largest_rank
---------+--------------
       1 |            6
       2 |            8
       3 |            9
(3 行记录)
```

###### MIN()函数

PostgreSQL的`MIN()`函数是一个集合函数，用来返回一组数值中的最小值

要找到表中某一列的最小值，你要把该列的名称传给`MIN()`函数。列的数据类型可以是数字、字符串或任何可比较的类型

与`AVG()`, COUNT()和`SUM()`函数不同，DISTINCT选项对MIN()函数没有任何影响

我们将使用dvdrental样本数据库中的`film` , `film_category`和category表进行演示

![film film_category category tables](SQL%E5%85%A5%E9%97%A8.assets/film-film_category-category-tables.png)

下面的例子使用`MIN()`函数从电影表的`rental_rate`列中获得最低的租金。

```sql
SELECT
   MIN (rental_rate)
FROM
   film;
```

```bash
 min
------
 0.99
(1 行记录)
```

为了获得租金最低的电影，你可以使用以下查询

```sql
SELECT
	film_id,
	title,
	rental_rate
FROM
	film
WHERE
	rental_rate = (
		SELECT MIN(rental_rate)
                FROM film
	)
FETCH FIRST 10 ROWS ONLY;
```

```bash
 film_id |        title         | rental_rate
---------+----------------------+-------------
       1 | Academy Dinosaur     |        0.99
      11 | Alamo Videotape      |        0.99
      12 | Alaska Phantom       |        0.99
     213 | Date Speed           |        0.99
      14 | Alice Fantasia       |        0.99
      17 | Alone Trip           |        0.99
      18 | Alter Victory        |        0.99
      19 | Amadeus Holy         |        0.99
      23 | Anaconda Confessions |        0.99
      26 | Annie Identity       |        0.99
(10 行记录)
```

- 首先，子查询`SELECT`最低的出租率
- 然后，外层查询`SELECT`租金等于子查询返回的最低租金的影片

在实践中，你经常使用`MIN()`函数和`GROUP BY`子句来寻找每组中的最低值

下面的语句使用`MIN()`函数和`GROUP BY`子句，按类别找到影片的最低重置成本

```sql
SELECT 
	name category,
	MIN(replacement_cost) replacement_cost
FROM category
INNER JOIN film_category USING (category_id)
INNER JOIN film USING (film_id)
GROUP BY name
ORDER BY name;
```

```bash
  category   | replacement_cost
-------------+------------------
 Action      |             9.99
 Animation   |             9.99
 Children    |             9.99
 Classics    |            10.99
 Comedy      |             9.99
 Documentary |             9.99
 Drama       |             9.99
 Family      |             9.99
 Foreign     |             9.99
 Games       |             9.99
 Horror      |            10.99
 Music       |            10.99
 New         |             9.99
 Sci-Fi      |             9.99
 Sports      |             9.99
 Travel      |             9.99
(16 行记录)
```

可以在`HAVING`子句中使用`MIN()`函数来过滤那些最小值符合某个条件的组

下面的查询使用`MIN()`函数找到按类别分组的电影的最低重置成本，只选择重置成本大于9.99的组

```sql
SELECT 
	name category,
	MIN(replacement_cost) replacement_cost
FROM category
INNER JOIN film_category USING (category_id)
INNER JOIN film USING (film_id)
GROUP BY name
HAVING MIN(replacement_cost) > 9.99
ORDER BY name;
```

```bash
 category | replacement_cost
----------+------------------
 Classics |            10.99
 Horror   |            10.99
 Music    |            10.99
(3 行记录)
```

在同一个查询中，可以将`MIN()`函数与其他聚合函数如`MAX()`函数一起使用

下面的例子使用`MIN()`和`MAX()`函数，按类别查找最短和最长的影片

```sql
SELECT 
	name category,
	MIN(length) min_length,
	MAX(length) max_length
FROM category
INNER JOIN film_category USING (category_id)
INNER JOIN film USING (film_id)
GROUP BY name
ORDER BY name;
```

```bash
  category   | min_length | max_length
-------------+------------+------------
 Action      |         47 |        185
 Animation   |         49 |        185
 Children    |         46 |        178
 Classics    |         46 |        184
 Comedy      |         47 |        185
 Documentary |         47 |        183
 Drama       |         46 |        181
 Family      |         48 |        184
 Foreign     |         46 |        184
 Games       |         57 |        185
 Horror      |         48 |        181
 Music       |         47 |        185
 New         |         46 |        183
 Sci-Fi      |         51 |        185
 Sports      |         47 |        184
 Travel      |         47 |        185
(16 行记录)
```

从两列或多列中找出最小的值

没`ranks`表的先创建

```sql
DROP TABLE IF EXISTS ranks;
CREATE TABLE ranks (
	user_id INT PRIMARY KEY,
	rank_1 INT NOT NULL,
	rank_2 INT NOT NULL,
	rank_3 INT NOT NULL
);
```

```sql
INSERT INTO ranks
VALUES
	(1, 6, 3, 5),
	(2, 2, 8, 5),
	(3, 5, 9, 8);
```

在这种情况下，你不能使用`MIN()`函数，因为`MIN()`函数是应用于行，而不是列。要找到两列或多列的最小值，你可以使用`LEAST()`函数

```sql
SELECT
	user_id,
	LEAST (rank_1, rank_2, rank_3) AS lowest_rank
FROM
	ranks;
```

```bash
 user_id | lowest_rank
---------+-------------
       1 |           3
       2 |           2
       3 |           5
(3 行记录)
```

###### COUNT()函数

`COUNT()`函数是一个聚合函数，允许你获得符合查询的特定条件的行数

下面的语句说明了使用`COUNT()`函数的各种方法

`COUNT(*)`函数返回由`SELECT`语句返回的行数，包括NULL和重复的行数

```sql
SELECT 
   COUNT(*) 
FROM 
   table_name
WHERE
   condition;
```

当你对整个表应用`COUNT(*)`函数时，PostgreSQL必须按顺序扫描整个表。

如果你在一个大表上使用`COUNT(*)`函数，查询会很慢。这与PostgreSQL的MVCC实现有关。因为多个事务同时看到不同状态的数据，`COUNT(*)`函数没有办法直接在整个表中计数，因此PostgreSQL必须扫描所有的行

与`COUNT(*)`函数类似，`COUNT(column)`函数返回由SELECT子句返回的行数。但是，它**不考虑**列中的NULL值

```sql
SELECT 
   COUNT(column) 
FROM 
   table_name
WHERE
   condition;
```

在这种形式下，`COUNT(DISTINCT 列)`返回该列中唯一非空值的列

```sql
SELECT 
   COUNT(DISTINCT column) 
FROM 
   table_name
WHERE
   condition;
```

我们经常使用`COUNT()`函数和GROUP BY子句来返回每个组的项目数。例如，我们可以使用`COUNT()`与`GROUP BY`子句来返回每个电影类别中的电影数量

下面用样板数据库演示

![img](SQL%E5%85%A5%E9%97%A8.assets/payment.png)

1) PostgreSQL COUNT(*) example

```sql
SELECT
   COUNT(*)
FROM
   payment;
```

```bash
 count
-------
 14596
(1 行记录)
```

2) PostgreSQL COUNT(DISTINCT column) example

为了获得客户支付的不同金额，你可以使用COUNT(DISTINCT amount)函数

```sql
SELECT
	COUNT (DISTINCT amount)
FROM
	payment;
```

```bash
 count
-------
    19
(1 行记录)
```

PostgreSQL COUNT() with GROUP BY clause

为了获得客户的付款数量，你使用`GROUP BY`子句，根据客户ID将付款分组，并使用`COUNT()`函数来计算每个组的付款数量

```sql
SELECT
	customer_id,
	COUNT (customer_id)
FROM
	payment
GROUP BY
	customer_id
FETCH NEXT 10 ROWS ONLY;
```

```bash
 customer_id | count
-------------+-------
           1 |    30
           2 |    26
           3 |    24
           4 |    22
           5 |    35
           6 |    25
           7 |    28
           8 |    23
           9 |    20
          10 |    24
(10 行记录)
```

PostgreSQL COUNT() with HAVING clause

你可以在`HAVING`子句中使用`COUNT()`函数，将一个特定的条件应用于组。例如，下面的语句可以找到付款超过40次的客户

```sql
SELECT
	customer_id,
	COUNT (customer_id)
FROM
	payment
GROUP BY
	customer_id
HAVING
	COUNT (customer_id) > 40;
```

```bash
 customer_id | count
-------------+-------
         526 |    42
         148 |    45
(2 行记录)
```

##### GROUP BY

GROUP BY子句被用来把表中在所列出的列上具有相同值的行分组在一起。 这些列的列出顺序并没有什么关系。其效果是把每组具有相同值的行组合为一个组行，它代表该组里的所有行。 这样就可以删除输出里的重复和/或计算应用于这些组的聚集。例如： 

```bash
study=# SELECT * FROM employees;
 employee_id |  employee_name  | department_id
-------------+-----------------+---------------
           1 | Bette Nicholson |             1
           2 | Christian Gable |             1
           3 | Joe Swank       |             2
           4 | Fred Costner    |             3
           5 | Sandra Kilmer   |             4
           6 | Julia Mcqueen   |
(6 行记录)

study=# SELECT department_id FROM employees GROUP BY department_id;
 department_id
---------------

             3
             4
             2
             1
(5 行记录)
```

在第二个查询里，我们不能写成`SELECT * FROM employees GROUP BY department_id;`， 因为其它列里没有哪个值可以和每个组相关联起来。被分组的列可以在选择列表中引用是因为它们在每个组都有单一的值。 

```bash
错误:  字段 "employees.employee_id" 必须出现在 GROUP BY 子句中或者在聚合函数中使用
第1行SELECT * FROM employees GROUP BY department_id;
```

使用`GROUP BY`子句时需要注意的有

- SELECT中出现的非组函数的字段必须声明在GROUP BY中。反之，GROUP BY 中声明的字段可以不出现在SELECT中
- GROUP BY声明在FROM后面、WHERE后面、ORDER BY 前面、LIMIT前面

##### HAVING的使用

`HAVING`子句为一个组或一个集合指定了一个搜索条件。`HAVING`子句通常与`GROUP BY`子句一起使用，用于根据指定的条件过滤组或集合

```bash
错误:  聚合函数不允许出现在WHERE中
```
- 如果过滤条件中使用了聚合函数，则必须使用HAVING来替换WHERE


```bash
错误:  字段 "xxx.xxx" 必须出现在 GROUP BY 子句中或者在聚合函数中使用
```

- HAVING必须声明在GROUP BY后面

**HAVING vs. WHERE**

`WHERE`子句允许你根据一个指定的条件来过滤记录。然而，`HAVING`子句允许你根据一个指定的条件来过滤记录组

换句话说，`WHERE`子句适用于行，而`HAVING`子句则适用于行组，虽然`HAVING`可以单独使用

因为根据他们的执行顺序，WHERE要先于HAVING执行

- 当过滤条件中有聚合函数时，则过滤条件必须声明在`HAVING`中

- 当过滤条件中没有聚合函数时，则此过滤条件声明再`WHERE`中或`HAVING`中都可以，但建议使用`WHERE`

如果没有聚合函数，`WHERE`效率会比`HAVING`高，理由见SQL执行过程

`WHERE` 和 `HAVING` 也不是互相排斥的，我们可以在一个查询里面同时使用 `WHERE` 和 `HAVING`。包含分组统计函数的条件用 `HAVING`，普通条件用 `WHERE`。这样，我们就既利用了 `WHERE` 条件的高效快速，又发挥了 `HAVING` 可以使用包含分组统计函数的查询条件的优点。当数据量特别大的时候，运行效率会有很大的差别

1) Using PostgreSQL HAVING clause with SUM function example

![payment table](SQL%E5%85%A5%E9%97%A8.assets/payment-table-16455420750041.png)

```sql
SELECT
	customer_id,
	SUM (amount)
FROM
	payment
GROUP BY
	customer_id
HAVING
	SUM (amount) > 200;
```

```bash
 customer_id |  sum
-------------+--------
         526 | 208.58
         148 | 211.55
(2 行记录)
```

2) PostgreSQL HAVING clause with COUNT example

![customer table](SQL%E5%85%A5%E9%97%A8.assets/customer-table.png)

```sql
SELECT
	store_id,
	COUNT (customer_id)
FROM
	customer
GROUP BY
	store_id
HAVING
	COUNT (customer_id) > 300;
```

```bash
 store_id | count
----------+-------
        1 |   326
(1 行记录)
```



##### SQL底层执行原理

SELECT语句的完整结构

**SQL92语法：**

```sql
SELECT ...., ...., ....(存在聚合函数)
FROM ...., ...., ....
WHERE 多表的连接条件 AND 不包含聚合函数的过滤条件
GROUP BY ...., ....
HAVING 包含聚合函数的过滤条件
ORDER BY ...., ....(ASC / DESC)
OFFSET .... ROW
FETCH NEXT .... ROWS ONLY
```

**SQL99语法：**

```sql
SELECT ....,....,....(存在聚合函数)
FROM .... (LEFT / RIGHT / FULL ...) JOIN .... ON 多表的连接条件
(LEFT / RIGHT / FULL ...) JOIN .... ON ....
WHERE 不包含聚合函数的过滤条件
GROUP BY ...., ....
HAVING 包含聚合函数的过滤条件
ORDER BY ...., ....(ASC / DESC)
OFFSET .... ROW
FETCH NEXT .... ROWS ONLY
```

###### SQL语句的执行过程

```sql
FROM ....,....→ ON → (LEFT / RIGHT / FULL ...) JOIN 
→ WHERE → GROUP BY → HAVING
→ SELECT → DISTINCT → ORDER BY → FETCH
```

`WHERE`要比`HAVING`先执行。因此`WHERE`先把不需要的数据过滤了一遍后分组，再执行`HAVING`。而分组后执行`HAVING`时本应不参与计算的数据也计算了，然后再挑出需要的。所以没有聚合函数时`WHERE`要比`HAVING`效率高

也因为`WHERE`要比`GROUP BY`先执行，所以`WHERE`不能处理聚合函数

### 子查询

子查询指一个查询语句嵌套在另一个查询语句内部的查询

假设我们想找到那些出租率高于平均出租率的电影。我们可以分两步来做。

- 通过使用`SELECT`语句和平均函数（AVG）找到平均出租率。
- 在第二个`SELECT`语句中使用第一个查询的结果，找到我们想要的影片。

下面的查询得到的是平均出租率

```sql
SELECT
	AVG (rental_rate)
FROM
	film;
```

```bash
        avg
--------------------
 2.9800000000000000
(1 行记录)
```

平均出租率是2.98

现在，我们能够得到高于平均出租率的电影

```sql
SELECT
	film_id,
	title,
	rental_rate
FROM
	film
WHERE
	rental_rate > 2.98
FETCH NEXT 10 ROWS ONLY;
```

```bash
 film_id |       title       | rental_rate
---------+-------------------+-------------
     133 | Chamber Italian   |        4.99
     384 | Grosse Wonderful  |        4.99
       8 | Airport Pollock   |        4.99
      98 | Bright Encounters |        4.99
       2 | Ace Goldfinger    |        4.99
       3 | Adaptation Holes  |        2.99
       4 | Affair Prejudice  |        2.99
       5 | African Egg       |        2.99
       6 | Agent Truman      |        2.99
       7 | Airplane Sierra   |        4.99
(10 行记录)
```

这段代码并不优雅，它需要两个步骤。我们想要一种方法，在一个查询中把第一个查询的结果传递给第二个查询。解决方案是使用一个子查询

子查询是一个嵌套在另一个查询中的查询，如`SELECT`、`INSERT`、`DELETE`和`UPDATE`。在本教程中，我们只专注于`SELECT`语句

为了构造一个子查询，我们把第二个查询放在括号里，在`WHERE`子句中作为表达式使用

```sql
SELECT
	film_id,
	title,
	rental_rate
FROM
	film
WHERE
	rental_rate > (
		SELECT
			AVG (rental_rate)
		FROM
			film
	)
FETCH NEXT 10 ROWS ONLY;
```

```bash
 film_id |       title       | rental_rate
---------+-------------------+-------------
     133 | Chamber Italian   |        4.99
     384 | Grosse Wonderful  |        4.99
       8 | Airport Pollock   |        4.99
      98 | Bright Encounters |        4.99
       2 | Ace Goldfinger    |        4.99
       3 | Adaptation Holes  |        2.99
       4 | Affair Prejudice  |        2.99
       5 | African Egg       |        2.99
       6 | Agent Truman      |        2.99
       7 | Airplane Sierra   |        4.99
(10 行记录)
```

括号内的查询被称为子查询(subquery)或内部查询(inner query)。包含子查询的查询被称为外查询(outer query)

PostgreSQL按以下顺序执行包含子查询的查询

- 首先，执行子查询
- 第二，获取结果并将其传递给外部查询
- 第三，执行外部查询

注意上面的示例子查询的结果输出为一条，如果输出为0或者多于一条的数据，则会报错

#### IN

一个子查询可以返回0或更多的记录。为了使用这个子查询，你在`WHERE`子句中使用`IN`操作符

例如，要获得返还日期在2005-05-29和2005-05-30之间的影片，你可以使用以下查询

```sql
SELECT
	inventory.film_id
FROM
	rental
INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
WHERE
	return_date BETWEEN '2005-05-29'
AND '2005-05-30'
FETCH NEXT 10 ROWS ONLY;
```

```bash
 film_id
---------
     870
     971
     573
     288
      89
     681
     858
     776
     257
     397
(10 行记录)
```

它返回多条记录，因此我们可以在查询的WHERE子句中把这个查询作为子查询使用，如下所示

```sql
SELECT
	film_id,
	title
FROM
	film
WHERE
	film_id IN (
		SELECT
			inventory.film_id
		FROM
			rental
		INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
		WHERE
			return_date BETWEEN '2005-05-29'
		AND '2005-05-30'
	)
FETCH NEXT 10 ROWS ONLY;
```

```bash
 film_id |       title
---------+-------------------
     307 | Fellowship Autumn
     255 | Driving Polish
     388 | Gunfight Moon
     130 | Celebrity Horn
     563 | Massacre Usual
     397 | Hanky October
     898 | Tourist Pelican
     228 | Detective Vision
     347 | Games Bowfinger
    1000 | Zorro Ark
(10 行记录)
```

在这个样板数据库中film_id为471拥有两个inventory_id，因此第一次查询一共有83条数据，而第二次查询一共只有82条数据

子查询还可以多重嵌套

```
SELECT
	film_id,title
FROM
	film
WHERE
	film_id IN (
        SELECT
        	film_id
        FROM
        	inventory
        WHERE
        	inventory_id IN (
                SELECT
                	inventory_id
                FROM
                	rental
                WHERE
                	return_date BETWEEN '2005-05-29'
                AND '2005-05-30'
			)
	);
```

#### ANY/ALL

ANY表示**任一**

ALL表示**所有**

返回比**任一**平均金额在3.81 到 3.85 之间高的客户

```SQL
SELECT
	customer_id,
	first_name,
	last_name,
	AVG (amount)::NUMERIC(10,3) AVG
FROM
	payment
INNER JOIN customer USING(customer_id)
GROUP BY
	customer_id
HAVING
	AVG (amount) > ANY (
        SELECT DISTINCT
            AVG (amount)::NUMERIC(10,2)
        FROM
            payment
        INNER JOIN customer USING(customer_id)
        GROUP BY
            customer_id
        HAVING
            AVG (amount) BETWEEN 3.81 AND 3.85
    )
ORDER BY AVG;
```

```bash
 customer_id | first_name  |  last_name   |  avg
-------------+-------------+--------------+-------
          52 | Julie       | Sanchez      | 3.811
         351 | Jack        | Foust        | 3.816
         597 | Freddie     | Duggan       | 3.816
         595 | Terrence    | Gunderson    | 3.818
         525 | Adrian      | Clary        | 3.823
....
```

意味着只要大于3.81即可

返回比**所有**平均金额在3.81 到 3.85 之间高的客户

```sql
SELECT
	customer_id,
	first_name,
	last_name,
	AVG (amount)::NUMERIC(10,3) AVG
FROM
	payment
INNER JOIN customer USING(customer_id)
GROUP BY
	customer_id
HAVING
	AVG (amount) > ALL (
        SELECT DISTINCT
            AVG (amount)::NUMERIC(10,2)
        FROM
            payment
        INNER JOIN customer USING(customer_id)
        GROUP BY
            customer_id
        HAVING
            AVG (amount) BETWEEN 3.81 AND 3.85
    )
ORDER BY AVG;
```

```bash
 customer_id | first_name  |  last_name   |  avg
-------------+-------------+--------------+-------
          42 | Carolyn     | Perez        | 3.852
         186 | Holly       | Fox          | 3.852
         592 | Terrance    | Roush        | 3.852
         158 | Veronica    | Stone        | 3.857
         231 | Georgia     | Jacobs       | 3.860
....
```

意味着只要大于3.85

这里所举的例子没有实际意义，只是示范

#### EXISTS

一个子查询可以是`EXISTS`操作符的输入。如果子查询返回任何行，`EXISTS`操作符返回真。如果子查询没有返回任何行，`EXISTS`操作符的结果是**false**。

`EXISTS`操作符只关心从子查询返回的行数，而不关心行的内容，因此，`EXISTS`操作符的常用编码规则如下所示

```sql
SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	EXISTS (
		SELECT
			1
		FROM
			payment
		WHERE
			payment.customer_id = customer.customer_id
	)
FETCH NEXT 10 ROWS ONLY;
```

```bash
 first_name | last_name
------------+-----------
 Jared      | Ely
 Mary       | Smith
 Patricia   | Johnson
 Linda      | Williams
 Barbara    | Jones
 Elizabeth  | Brown
 Jennifer   | Davis
 Maria      | Miller
 Susan      | Wilson
 Margaret   | Moore
(10 行记录)
```

这个查询的工作方式类似于对customer_id列的inner join。然而，它对客户表中的每一条记录最多返回一条记录，尽管在支付表中有一些相应的记录

**把外层的查询结果代入到内层，看内层查询是否成立**，如果成立则输出到结果集中

#### FROM

还可以把内层的查询结果当做外层的临时表，供外层SQL再次查询

```SQL
SELECT
	*
FROM (
		SELECT
			inventory.film_id
		FROM
			rental
		INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
		WHERE
			return_date BETWEEN '2005-05-29'
		AND '2005-05-30'
	) s;
```

注意，在PostgreSQL/MySQL里，`FROM` 中的子查询必须有一个别名

用这样的操作可以弥补PostgreSQL不支持聚合函数嵌套的遗憾

