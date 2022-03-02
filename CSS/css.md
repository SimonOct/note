# css

## css的基础语法和注释

![image-20211222021824832](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211222021824832.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>css的基础语法和注释</title>
    <!--样式设置在style标签中,css声明要以 ";"结尾,
        声明要用 "{}" 包含起来,
        如果属性值由多个单词组成,要给值加上引号
    -->
    <style type="text/css">
        body {
            background-color: antiquewhite;
            color: red;
            font-family: "Arial black";
            /* 注释 */
        }
    </style>
</head>
<body>
    Hello
</body>
</html>
```

![image-20211222022826755](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211222022826755.png)

## css的使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>css的使用</title>
    <!-- 定义内部样式 -->
    <style type="text/css">
        /* p标签 */
        p {
            color: rgb(0, 195, 255);
            font-family: 楷体;
        }
    </style>
    <!-- 引入外部的css文件 -->
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>
<!-- 
    行内样式
        将样式定义在html标签上的style属性中;
        以行内样式写的css耦合度较高
    内部样式
        定义在head标签中的style标签内
    外部样式
        通过link标签引入外部的css文件
        <link rel="stylesheet" href="css/style.css" type="text/css">
            rel     当前文件与引入的文件之间的关系
            type    css类型
            href    引入的资源的路径
    优先级
        行内元素优先级最高;head从下往上,优先级越来越低
 -->
<body>
    <!-- 行内样式 -->
    <p style="color: rgb(38, 0, 255);font-family: 楷体;">这是一段文本</p>
    <p>这是一段文本</p>
    <p>这是一段文本</p>
    <p>这是一段文本</p>
</body>
</html>
```

![image-20211222024317851](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211222024317851.png)

## 选择器

### 基本选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>基本选择器</title>
    <style type="text/css">
        /* 
        通用选择器  *
            选择所有元素
            * {
                属性名:属性值
            }
         */
            * {
                /* 字体颜色 */
                color: blue;
            }
            /* 元素选择器/标签选择器
                    选择仔顶元素
                    标签名 {
                        属性名:属性值
                    }
             */
             div {
                 width: 100px;
                 height: 100px;
                 background-color: antiquewhite;
             }
             /* 
                id选择器
                    选择指定id属性值的元素  #
                    #id属性值 {
                        属性名:属性值
                    }
                    id值最好保持唯一
                    id定义规则:以字母、数字、下划线、中划线组成,不要以数字开头
              */
              #div1 {
                  color: rgb(127, 172, 255);
              }
              /* 
                class类选择器   .
                    选择设定指定class属性值的元素
                    .class属性值 {
                        属性名:属性值
                    }
              */
              .class1 {
                  font-weight: bold;
              }
              /* 
                组合选择器/分组选择器
                    选择指定选择器选中的元素
                    选择器1,选择器2,选择器3,...{
                        属性名:属性值
                    }
              */
              #div1,.class1,p {
                  border: 1px solid rgb(127, 255, 148);
              }
    </style>
    <!-- 
        选择器的优先级
            id选择器 > 类选择器 > 元素选择器 > 通用选择器

        行内样式最高
     -->
</head>
<body>
    <div id="div1" class="class1">div1</div>
    <div id="div2" class="class1">div2</div>
    <div id="div3">div3</div>
    <p>p</p>
</body>
</html>
```

![image-20211222030443693](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211222030443693.png)

### 组合选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>组合选择器</title>
    <!-- 
    组合选择器
        后代选择器(以空格分隔)
            选择指定元素的所有的后代元素
            指定元素 指定元素{
                属性名:属性值
            }
        子代选择器(以大于号分隔)
            选择指定元素的第一代元素
        相邻兄弟选择器(以加号分隔)
            选择指定元素相邻的下一个指定元素
        普通兄弟选择器(以波浪号分隔)
            选择指定元素后的同级元素
    -->
    <style type="text/css">
        /* 后代选择器(以空格分隔) */
        .food li {
            background-color: blanchedalmond;
            border: 1px solid red;
        }
        .food1 > li {
            /* 子代选择器(以大于号分隔) */
            border: 1px solid rgb(30, 15, 238);
        }
        #d + div {
            /* 相邻兄弟选择器(以加号分隔) */
            color: red;
        }
        #b ~ li {
            /* 普通兄弟选择器(以波浪号分隔) */
            color: blue;
        }
    </style>
</head>

<body>
    <h1>食物</h1>
    <ul class="food">
        <li>水果
            <ul>
                <li id="b">香蕉</li>
                <li>苹果</li>
                <li>梨</li>
            </ul>
        </li>
        <li>蔬菜
            <ul>
                <li>白菜</li>
                <li>油菜</li>
                <li>卷心菜</li>
            </ul>
        </li>
    </ul>
    <hr>
    <h1>食物</h1>
    <ul class="food1">
        <li>水果
            <ul>
                <li>香蕉</li>
                <li>苹果</li>
                <li>梨</li>
            </ul>
        </li>
        <li>蔬菜
            <ul>
                <li>白菜</li>
                <li>油菜</li>
                <li>卷心菜</li>
            </ul>
        </li>
    </ul>
    <hr>
    <div>
        相邻兄弟选择器
        <ul>
            <li>嘿嘿嘿</li>
            <li id="b">开心麻花</li>
            <li>贾玲</li>
            <li>宋小宝</li>
        </ul>
    </div>
    <div>
        相邻兄弟选择器2
    </div>
    <div>
        相邻兄弟选择器3
    </div>
    <p>相邻兄弟选择器4</p>
</body>
</html>
```

![image-20211223172653502](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223172653502.png)

## css常用属性

### 背景

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>背景</title>
    <style type="text/css">
        /* 通过元素选择器获取body元素 */
        body {
            /* 设置元素的背景颜色 */
            background-color: antiquewhite;
            /* 设置元素的背景图片,默认为重复显示 */
            background-image: url(img/image1.png);
            /* 设置背景图片是否重复 no-repeat表示不重复,repeat-x横向重复,repeat-y纵向重复*/
            background-repeat: repeat-y;
            /* 这是图片大小,只设定一个值时,图片会等比放大或缩小,设定两个值则不会 */
            background-size: 100px 100px;
        }
    </style>
</head>
<body>
    
</body>
</html>
```

![image-20211223173904011](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223173904011.png)

### 文本

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文本</title>
    <style type="text/css">
        /* 文本 */
        /* id选择器 */
        #div1 {
            /* 字体颜色,可选单词,rgb,16进制 */
            color: blue;
        }
        #div2 {
            /* 对齐方式,默认为左对齐 */
            text-align: center;
        }
        #div3 {
            /* 文本修饰 */
            /* overline 上划线,underline 下划线,line-trough 删除线 */
            text-decoration: overline;
        }
        #div4 {
            /* 同时设置上中下划线 */
            text-decoration: line-through overline underline;
        }
        a {
            /* 去除自带的下划线 */
            text-decoration: none;
        }
        #p1 {
            /* 首行缩进 */
            text-indent: 2em;
        }
    </style>
</head>
<body>
    
    <div id="div1">文本1</div>
    <div id="div2">文本2</div>
    <div id="div3">文本3</div>
    <div id="div4">文本4</div>

    <a href="#">超链接</a>
    <p id="p1">这是一段文字,我们需要进行首行缩进</p>
</body>
</html>
```

![image-20211223175409432](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223175409432.png)

### 字体

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>字体</title>
    <style type="text/css">
        div {
            /* 设置字体 */
            /* 
            当字体名包含空格或特殊字体时，需要用双引号包含
            font-family有后备字体，可以为元素设置多种字体，当浏览器不识别第一种字体时，会尝试找下一种字体
            多个字体用英文逗号隔开
             */
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif , 楷体, 宋体;
            /* 设置字体大小 */
            font-size: 30px;
            /* 设置字体风格 */
            /* 
            normal  正常
            italic  斜体
            oblique 强制斜体,当字体没有斜体时,也会将其变成斜体
            */
            font-style: italic;
            /* 字体粗细 */
            /* 
            bold    粗体
            100~900
            */
            font-weight: bold;
        }
    </style>
</head>
<body>
    
    <div>这是一段文字</div>
</body>
</html>
```

![image-20211223180415315](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223180415315.png)

### 对齐方式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>对齐方式</title>
    <!-- 
        justify
        right
        center
        right
     -->
    <style type="text/css">
        p {
            text-align: justify;
        }
    </style>
</head>
<body>
    <p>
        階層式樣式表是一種用來為結構化文件添加樣式的電腦語言，由W3C定義和維護。CSS 被分為不同等級：CSS1 現已廢棄， CSS2.1 是推薦標準， CSS3 分成多個小模組且正在標準化中。CSS3現在已被大部分現代瀏覽器支援，而下一版的CSS4仍在開發中。
        階層式樣式表是一種用來為結構化文件添加樣式的電腦語言，由W3C定義和維護。CSS 被分為不同等級：CSS1 現已廢棄， CSS2.1 是推薦標準， CSS3 分成多個小模組且正在標準化中。CSS3現在已被大部分現代瀏覽器支援，而下一版的CSS4仍在開發中。

    </p>
</body>
</html>
```

![image-20211223180929722](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223180929722.png)

### display

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>display属性</title>
    <style type="text/css">
        /* display属性 */
        /* 
        规定元素生成框的类型
        block   元素会被显示,且元素会变成块级元素,元素前后会有换行符
        none    元素会被隐藏
        inline  元素会显示为行内元素,元素前后没有换行符
        inline-block    行内块级元素

        块级元素,可以设置元素的宽高和边距
        行内元素,不可以设置元素的宽高和边距,元素不会自动换行
        行内块级元素,可以设置元素的宽高和边距,元素不会自动换行
        */
        #sp2 {
            /* 隐藏元素 */
            /* 由下往上匹配,先匹配到下面的sp2,此处的属性不会生效 */
            display: none;
        }
        #sp2 {
            /* 设置block */
            display: block;
            width: 200px;
            height: 100px;
            background-color: antiquewhite;
        }
        #sp1 {
            /* 不会生效 */
            width: 100px;
            height: 100px;
            background-color: antiquewhite;
        }
        /* 设置元素为行内元素 */
        #div1 {
            background-color: azure;
        }
        #div2 {
            background-color: rgb(23, 201, 201);
        }
        #div3 {
            background-color: rgb(118, 145, 145);
        }
        div {
            display: inline;
            /* 不会生效 */
            width: 100px;
        }
        p {
            width: 200px;
            height: 200px;
            background-color: aqua;
            display: inline-block;
        }
    </style>
</head>
<body>
    
    <span id="sp1">
        这是一个span1
    </span>
    <span id="sp2">
        这是一个span2
    </span>
    <span id="sp3">
        这是一个span3
    </span>
    <hr>
    <div id="div1">div1</div>
    <div id="div2">div2</div>
    <div id="div3">div3</div>
    <hr>
    <p>文本1</p>
    <p>文本2</p>
</body>
</html>
```

![image-20211223182536593](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223182536593.png)

### 浮动

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>浮动</title>
    <style type="text/css">
        #div1 {
            width: 100px;
            height: 100px;
            background-color: gray;
            float: right;
        }
        #div2 {
            width: 100px;
            height: 100px;
            background-color: rgb(130, 178, 206);
            float: right;
        }
        img {
            width: 100px;
            float: left;
        }

    </style>
</head>
<body>
    <div id="div1"></div>
    <div id="div2"></div>
    <hr>
    <!-- 清除浮动 -->
    <div style="clear: both;"></div>
    <div>
        层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。
        层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。
        <img src="img/image1.png">
        层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。
        层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。
    </div>
</body>
</html>
```

![image-20211223210946065](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223210946065.png)

### 盒子模型

#### border

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>盒子模型-border</title>
    <!-- 
        设置元素边框的宽度/颜色/类型
        单独设置边框的颜色/宽度/类型
            border-color
            border-width
            border-style
            boeder-collapse 合并边框
            ...
     -->
    <style type="text/css">
        #div1 {
            border: 1px blue dotted;
        }
        #div2 {
            border-style: dashed;
            border-color: antiquewhite;
            border-width: 1px;
        }
        #div3 {
            /* 
            设定一个值的时候,代表是个边框相同样式.
            设定两个字的时候分上下和左右一组.
            三个的时候是上右下.
            四个分为上右下左
             */
            border-style: solid dashed dotted double;
            border-color: rgb(158, 95, 230) rgb(187, 60, 60) rgb(43, 75, 43) rgb(114, 114, 129);
            border-width: 10px 7px 4px 1px;
        }
        table {
            border-collapse: collapse;
        }
    </style>
</head>
<body>
    
    <div id="div1">
        这是一段文字
    </div>
    <div id="div2">
        这是一段文字
    </div>
    <hr>
    <div id="div3">
        这是一段文字
    </div>
    <hr>
    <table border="" cellspacing="" cellpadding="">
        <tr><th>Header</th><th>Body</th></tr>
        <tr><td>Data</td><td>Data</td></tr>
    </table>
</body>
</html>
```

![image-20211223212701809](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223212701809.png)

#### padding

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>padding</title>
    <style type="text/css">
        td {
            /* padding: 10px 20px 30px 40px; */
            /* 设置左边距 */
            padding-left: 10px;
        }
    </style>
</head>
<body>
    <table border="1" align="center" width="500px" style="border-collapse: collapse;">
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
</body>
</html>
```

![image-20211223215240632](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223215240632.png)

#### margin

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>margin</title>
    <style type="text/css">
        p {
            background-color: aquamarine;
        }
        #p1 {
            /* margin: 50px 100px; */
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <p>这是一段文字</p>
    <p id="p1">这是一段文字</p>
</body>
</html>
```

![image-20211223215852583](C:\Users\simon\OneDrive\Typroa\CSS\css.assets\image-20211223215852583.png)
