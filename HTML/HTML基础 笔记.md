# HTML基础语法

## 标签

### 单标签

无属性	->	<标签名 />

有属性	->	<标签名 属性名="属性值" />

### 双标签

无属性	->	<标签名></标签名>

有属性	->	<标签名 属性名="属性值"><标签名>

### 整体结构

```html
<html></html>	->	表示当前是一个页面
<head></head>	->	头部信息
<body></body>	->	身体部分
```

```html
<!--HTML5版本声明-->
<!DOCTYPE html>
<!--网页区域-->
<html>
    <!--头部区域-->
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>标题</title>	<!--页面的标题, 也是收藏网页时默认的名字-->
        <link rel="stylesheet" href="引入的css文件的路径"/>
        <script src="引入的js文件的路径" type="text/javascript" charset="utf-8"></script>
    </head>
    <!--内容区域, 浏览器可见内容-->
    <body>
    </body>
</html>
```

## 标题和水平线

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<!--
标签的属性之间要以空格隔开
body标签
	bgcolor	背景颜色	可填:颜色名/rgb/16进制
	text	字体颜色	可填:颜色名/rgb/16进制
标题标签
    <h1></h1><h2></h2>~<h5></h5><h6></h6> 依次从小到大
    不建议在页面中写多个h1标签, h1标签可以被搜索殷勤获取到,如果有多个,可能会进入搜索引擎的黑名单
水平线标签
    <hr>
    width:宽度    可填:px/百分比
    align:对齐方式  可填:left/right/center(默认)
    size:水平线粗细 
    
-->
<body bgcolor="pink" text="blue">
    hello
    <h1>hello</h1>
    <h2>hello</h2>
    <h3>hello</h3>
    <h4>hello</h4>
    <h5>hello</h5>
    <h6>hello</h6>
    hello
    <hr width="50%" align="left" size="5">
    <hr width="500px" align="right" size="10">
</body>
</html>
```

![image-20211221000256243](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221000256243.png)

## 段落和换行

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>段落和换行</title>
</head>
<!--
    段落和换行
    段落标签
        <p></p> 段落会自动换行
        常用属性:
            align:对齐方式
                left    居左对齐(默认)
                right   居右对其
                center  居中对齐
                justify 两端对齐
    换行标签
        <br>    相对于p标签来说, 段落距离会小
-->
<body>
    <p>Django是一个开放源代码的Web应用框架，由Python写成。</p>
    <p>Django是一个开放源代码的Web应用框架，由Python写成。</p>
    <hr>

    <p align="left">
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
    </p>
    <p align="right">
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
    </p>
    <p align="center">
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
    </p>
    <hr>

    <p>
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
        hello
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
    </p>
    <p align="justify">
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
        hello
        Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。Django是一个开放源代码的Web应用框架，由Python写成。
    </p>
    <hr>
    HEELO <br>
    WORLD
</body>
</html>
```

![image-20211221000139601](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221000139601.png)

## 列表

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>列表</title>
</head>
<!--
    无序列表
        <ul>
            <li></li>
            <li></li>
        </ul>
        常用属性:
            type    列表的图标
                square  实心方块
                circle  空心圆
                disc    实心圆(默认)
    有序列表
        <ol>
            <li></li>
            <li></li>
        </ol>
        常用属性:
            type    列表的图标
                1   数字符号
                a   小写字母
                A   大写字母
                i   小写罗马字母
                I   大写罗马字母
-->
<body>

    <h2>无序列表</h2>
    <ul>
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ul>
    <ul type="disc">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ul>
    <ul type="square">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ul>
    <ul type="circle">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ul>

    <h2>有序列表</h2>
    <ol type="1">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ol>
    <ol type="a">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ol>
    <ol type="A">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ol>
    <ol type="i">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ol>
    <ol type="I">
        <li>张三</li>
        <li>李四</li>
        <li>王五</li>
    </ol>
</body>
</html>
```

![image-20211221000824028](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221000824028.png)

## div和span

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>div和span</title>
</head>
<!--
    div标签
        层, 块级元素, 标签会自动换行, 默认宽度占满屏幕, 常用于布局
        常用属性: 
            align   div元素中内容的对齐方式
    span标签
        块, 行内元素, 标签不会自动换行
-->
<body>
    <div align="center">
        层, 块级元素, 标签会自动换行, 默认宽度占满屏幕, 常用于布局
    </div>
    你好
    <div>
        层, 块级元素, 标签会自动换行, 默认宽度占满屏幕, <br>
        常用于布局
    </div>
    <hr>
    <span>
        张三
    </span>
</body>
</html>
```

![image-20211221001400176](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221001400176.png)

![image-20211221001415762](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221001415762.png)

![image-20211221001618061](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221001618061.png)

## 格式化标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>格式化标签</title>
</head>
<!--
    font标签    行内元素
        设置字体相关属性
        常用属性
            color   字体颜色    颜色名/rgb/16进制
            size    字体大小
            face    字体风格
    pre标签
        定义格式化的文本,保留文本中的空格和换行
    粗体: b标签和strong标签 行内元素
    粗体: i
    下划线: u
    删除线: del
    下标: sub
    上标: sup

-->
<body>
    你好<br>
    <font color="red" size="7" face="楷体">你好</font>
    <hr>

    HELLO         WORLD
    <hr>
    <pre>
        HELLO         WORLD
        !
    </pre>
    <hr>
    粗体 -- <b>粗体</b> -- <strong>粗体</strong> <br>
    斜体 -- <i>斜体</i><br>
    下划线 -- <u>下划线</u><br>
    删除线 -- <del>删除线</del><br>
    下标 -- H<sub>2</sub>O<br>
    上标 -- 2<sup>x</sup>
</body>
</html>
```

![image-20211221003228636](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221003228636.png)

## a标签

### 超链接

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>超链接a标签</title>
</head>
<!--
    a标签
        定义超链接,用于从一个页面链接到另外一个页面
        行内元素
        常用属性:
            href    这是一个必须属性,如果未设置改属性,则a标签与普通文本无区别
            target
                _self   当前窗口打开(默认)
                _blank   新建标签页打开链接
                _parent
                _top

-->
<body>
    <!--此处写的是相对路径,也可以写绝对路径,还可以是一个外站网址-->
    <a href="05-格式化标签.html">05-格式化标签.html</a>
    <a>列表</a>
    <hr>
    <!--新建标签页打开页面-->
    <a href="05-格式化标签.html" target="_blank">05-格式化标签.html</a>

</body>
</html>
```

![image-20211221004405083](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221004405083.png)

### 锚点

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>锚点</title>
</head>
<!--
    锚点的实现
        ( 如果想要跳转到当前页面,那么href的值可以设置为# )
        1.利用a标签的name属性
        2.利用其他标签的id属性
-->
<body>
   <h2><a name="context1">内容1</a></h2> 
    h <hr id="hr1"><br><br><br><br><br><br><br><br><br><br>i <hr><br><br><br><br><br><br><br><br><br><br>! <br><br><br><br><br><br><br><br><br><br>! <hr>
    <h2><a name="context2">内容2</a></h2> 
    h <hr id="hr2"><br><br><br><br><br><br><br><br><br><br>i <hr><br><br><br><br><br><br><br><br><br><br>! <br><br><br><br><br><br><br><br><br><br>! <hr>
    <h2><a name="context3">内容3</a></h2> 
    h <hr id="hr3"><br><br><br><br><br><br><br><br><br><br>i <hr><br><br><br><br><br><br><br><br><br><br>! <br><br><br><br><br><br><br><br><br><br>! <hr>
    
    <!--相当于刷新页面-->
    <a href="">锚点1</a><br>
    <!--跳到最顶部-->
    <a href="#">锚点2</a><br>
    <!--a标签的href属性指向某个a标签的name属性-->
    <a href="#context1">回到内容1</a><br>
    <a href="#context3">回到内容2</a><br>
    <a href="#context3">回到内容3</a><br>
    <!--a标签的href属性指向某个标签的id属性-->
    <a href="#hr1">回到水平分割线1</a><br>
    <a href="#hr2">回到水平分割线2</a><br>
    <a href="#hr3">回到水平分割线3</a><br>
</body>
</html>
```

## 图片

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>图片</title>
</head>
<!--
    img标签,行内标签,不会自动换行
        必须属性
            src 被引用的图片的地址
        常用属性
            title   当鼠标悬停在图片上时显示的文字
            alt     当图片加载失败时显示的文本
            width   设置图片的宽度
            height  设置图片的高度
            border  边框
            align   对齐方式,规定如何根据文本来排列对象


-->
<body>
    <!--本地资源-->
    <img src="img/img1.png" width="200px">
    <img src="img/img2.png" width="200px" height="50px">
    <img src="error" alt="图片显示错误">
    <!--网络资源-->
    <a href="https://www.baidu.com" target="_blank">
        <img src="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" title="百度" border="2" align="right">
    </a>
</body>
</html>
```

![image-20211221235223274](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211221235223274.png)

## 表格

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>表格</title>
</head>
<!--
    table   表示表格
    tr      表示表格中的行(每一行可以包含一个或多个td或th)
    td      表示表格中的标准单元格
    th      表示表格中的表头单元格(具有标题的效果)
    table常用属性
        border  表格的边框
        width   宽度    (百分比/像素)
        height  高度    (百分比/像素)
        align   整个表格的对齐方式(不是表格内的字)
    tr常用属性
        align   行内的对齐方式
        valign  垂直方向的对齐方式  top/middle/bottom/baseline  (基线是一条虚构的线。在一行文本中，大多数字母以基线为基准。)
        bgcolor 背景颜色
        rowspan 纵向合并    参数是数字,表示合并多少格
        colspan 横向合并    参数是数字,表示合并多少格
    css样式
        style="border-collapse: collapse;"  合并表格边框
-->
<body>
    <table border="1" align="center" width="500px" height="300px" style="border-collapse: collapse;">
        <tr align="center">
            <th>班级</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>性别</th>
        </tr>
        <tr align="center" valign="top" bgcolor="antiquewhite">
            <td>101班</td>
            <td>张三</td>
            <td>18</td>
            <td>男</td>
        </tr>
        <tr align="left">
            <td>101班</td>
            <td>李四</td>
            <td>19</td>
            <td>女</td>
        </tr>
        <tr align="right">
            <td>102班</td>
            <td>王五</td>
            <td>20</td>
            <td>男</td>
        </tr>
    </table>
    <hr>
    <h3 align="center">纵向合并rowspan</h3>
    <table border="1" align="center" width="500px" height="300px" style="border-collapse: collapse;">
        <tr align="center">
            <th>班级</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>性别</th>
        </tr>
        <tr align="center" valign="top" bgcolor="antiquewhite">
            <td rowspan="2">101班</td>
            <td>张三</td>
            <td>18</td>
            <td>男</td>
        </tr>
        <tr align="center">
            <td>李四</td>
            <td>19</td>
            <td>女</td>
        </tr>
        <tr align="center">
            <td>102班</td>
            <td>王五</td>
            <td>20</td>
            <td>男</td>
        </tr>
    </table>
    <hr>
    <h3 align="center">横向合并colspan</h3>
    <table border="1" align="center" width="500px" height="300px" style="border-collapse: collapse;">
        <tr align="center">
            <th>班级</th>
            <th colspan="2">姓名 年龄</th>
            <th>性别</th>
        </tr>
        <tr align="center" valign="top" bgcolor="antiquewhite">
            <td>101班</td>
            <td>张三</td>
            <td>18</td>
            <td>男</td>
        </tr>
        <tr align="center">
            <td>101班</td>
            <td>李四</td>
            <td>19</td>
            <td>女</td>
        </tr>
        <tr align="center">
            <td>102班</td>
            <td>王五</td>
            <td>20</td>
            <td>男</td>
        </tr>
    </table>
</body>
</html>
```

![image-20211222002031012](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211222002031012.png)

## 表单

### form

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>表单</title>
</head>
<!--
    所有标签都有的属性
        id      用来标识元素的唯一性
        name    用来提交数据时的参数名
        style   设置元素的行内样式(具体的样式)
        class   设置元素的样式名

    form    块级元素,表单提交时必须设计表单元素的name属性值,否则无法获取数据,表单需要结合表单元素一起使用
    常用属性
        action  提交表单的地址
        method  提交方式(不区分大小写)
                get
                post
                dialog
                get与post的区别(post请求需要服务器的支持)
                    1.get请求时,参数会跟在浏览器地址栏的后面,而post请求不会(post请求将数据存放在请求体中)
                    2.get请求相对于post请求而言,不那么安全
                    3.get请求传递的数据长度是有限的,而post基本无限制(具体与服务器相关)
                    4.get请求比post请求快(2倍左右)
                    5.get请求有缓存(会将数据存放在浏览器中),而post请求无缓存

        target  提交数据时打开窗口的方式
                _self
                _blank
-->
<body>
    <form action="https://www.baidu.com" method="get" target="_blank">
        姓名: <input type="text" name="uname">
        <button>提交</button>
    </form>
</body>
</html>
```

### input

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>input</title>
</head>
<!--
    input   行内元素
        name        没有name属性,无法提交数据
        type        元素类型
            password    密码
            text        文本框
            radio       单选框
                单选框需要通过name属性设置为一组
            checkebox   多选框
            file        上传文件
                如果表单需要上传文件,则表单需要设置一个属性 enctype="multipart/form-data",提交方式post
            hidden      隐藏域
            button      普通按钮
            submit      提交按钮,搭配表单使用
            reset       重置按钮,不会重置value的值
            date        日期框,选择日期
        value       元素的值
        readonly    只读
        maxlength   限制长度
        disabled    禁用标签
            
-->
<body>
    <form action="" method="get">
        文本框: <input type="text" value="张三" maxlength="10"><br>
        文本框: <input type="text" value="张三" readonly><br>
        密码框: <input type="password"><br>
        单选框: <input type="radio" value="man" name="sex">男 <input type="radio" value="nv" name="sex">女<br>
        多选框: <input type="checkbox" value="1" name="check">1
        <input type="checkbox" value="2" name="check">2
        <input type="checkbox" value="3" name="check">3 <br>
        文件域: <input type="file"><br>
        隐藏域: <input type="hidden" value="admin"><br>
        普通按钮: <input type="button" value="普通按钮" disabled><br>
        提交按钮: <input type="submit" value="提交"><br>
        重置按钮: <input type="reset" value="重置"><br>
        日期框: <input type="date">
    </form>
</body>
</html>
```

![image-20211222010808362](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211222010808362.png)

### textarea_label_button_select

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>textarea_label_button_select</title>
</head>
<!--
    textarea    定义可输入多行文本的控件
        cols    文本的可见宽度
        rows    文本的可见行数
    label       聚焦用的
        for     当for属性与元素的id属性值一致时,点击label标签,会自动聚焦元素
    button
        html5新添,与input type基本一致.但button比input好的的方式可以添加内容,如图片/文本之类的,而input只有纯文本
        type
            button
            submit(默认值)
            reset
    select      下拉列表
        multiple    多选
        siez        可见选项数
    option      与下拉框搭配使用
        selected    默认选中项
        value       提交给服务器的选项值
            如果未设置value,值提交option双标签中的文本值


-->
<body>
    姓名: <input type="text" name="uname"><br>
    简介: <textarea cols="30" rows="10"></textarea><br>
    <hr>
    <label for="uname">姓名: <input type="text" id="uname"></label><br>
    <hr>
    <form action="https://www.baidu.com">
        <input type="text">
        <input type="button" value="普通按钮">
        <input type="submit" value="提交按钮">
        <input type="reset" value="重置按钮">
        <hr>
        <button type="button">普通按钮</button>
        <button type="submit">提交按钮</button>
        <button type="reset">重置按钮</button>
    </form><br>
    <hr>
    <select name="city" multiple size="2">
        <option>请选择城市</option>
        <option selected>广州</option>
        <option>上海</option>
        <option>北京</option>
        <option>深圳</option>
    </select>
    <select name="city" multiple size="2" disabled>
        <option>请选择城市</option>
        <option>广州</option>
        <option>上海</option>
        <option>北京</option>
        <option>深圳</option>
    </select>
    <select name="city">
        <option>请选择城市</option>
        <option selected>广州</option>
        <option>上海</option>
        <option disabled>北京</option>
        <option>深圳</option>
    </select>
</body>
</html>
```

![image-20211222013608885](HTML%E5%9F%BA%E7%A1%80%20%E7%AC%94%E8%AE%B0.assets/image-20211222013608885.png)
