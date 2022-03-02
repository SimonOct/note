# bootstrap5

开始前可以用官方提供的cdn模板

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>
```

## Layout

### Breakpoint(断点)

斷點是 Bootstrap 中的觸發器，用於控制排版如何在不同的設備或視區大小進行響應式的變化。

**核心觀念**

- **斷點是響應式開發的基礎。** 使用斷點來控制在特定尺寸或設備上調整佈局。

  ***Breakpoints are the building blocks of responsive design.** Use them to control when your layout can be adapted at a particular viewport or device size.*

- **使用 media queries 的斷點構建 CSS。** media queries 是 CSS 的一個特性，它允許您根據瀏覽器和操作系統参數有條件地套用樣式。我們最常在 media queries 中使用 `min-width`.

  ***Use media queries to architect your CSS by breakpoint.**  Media queries are a feature of CSS that allow you to conditionally apply styles based on a set of browser and operating system parameters. We  most commonly use `min-width` in our media queries.*

- **在響應式開發中，主要會以行動版為優先。** Bootstrap 的 CSS 旨在使用最少的樣式來使佈局在最小的斷點處工作，然後在樣式上分層以針對較大的設備調整該設計。這樣可以優化CSS，縮短渲染時間，並為訪問者提供出色的體驗。

  ***Mobile first, responsive design is the goal.**  Bootstrap’s CSS aims to apply the bare minimum of styles to make a  layout work at the smallest breakpoint, and then layers on styles to  adjust that design for larger devices. This optimizes your CSS, improves rendering time, and provides a great experience for your visitors.*

| Breakpoint        | Class infix | Dimensions |
| ----------------- | ----------- | ---------- |
| X-Small           | *None*      | <576px     |
| Small             | `sm`        | ≥576px     |
| Medium            | `md`        | ≥768px     |
| Large             | `lg`        | ≥992px     |
| Extra large       | `xl`        | ≥1200px    |
| Extra extra large | `xxl`       | ≥1400px    |

### Containers(容器)

容器是 Bootstrap 的基本建構區塊，在給定的設備或是視區中包含、填充和對齊你的內容

容器是 Bootstrap 中最基本的佈局元素，**在使用我們的網格系統時是必需的**。容器用於在容納，填充和（有時）使內容居中。儘管容器 *可以* 巢狀，但大部分排版不需要巢狀。

Bootstrap 本身自帶三種不同的容器：

- `.container`, 每一個響應式斷點都會設置一個 `max-width`
- `.container-fluid`, 所有斷點都是 `width: 100%`
- `.container-{breakpoint}`, 直到指定斷點之前，都會是 `width: 100%`

下表說明了每個容器的 `max-width` 與每個斷點處的原始 `.container` 和 `.container-fluid` 的比較。

|                  | Extra small<br /><576px | Small<br />≥576px | Medium<br />≥768px | Large<br />≥992px | X-Large<br />≥1200px | XX-Large<br />≥1400px |
| ---------------- | ----------------------- | ----------------- | ------------------ | ----------------- | -------------------- | --------------------- |
| `.container`     | 100%                    | 540px             | 720px              | 960px             | 1140px               | 1320px                |
| `.container-sm`  | 100%                    | 540px             | 720px              | 960px             | 1140px               | 1320px                |
| `.container-md`  | 100%                    | 100%              | 720px              | 960px             | 1140px               | 1320px                |
| `.container-lg`  | 100%                    | 100%              | 100%               | 960px             | 1140px               | 1320px                |
| `.container-xl`  | 100%                    | 100%              | 100%               | 100%              | 1140px               | 1320px                |
| `.container-xxl` | 100%                    | 100%              | 100%               | 100%              | 100%                 | 1320px                |





### grid(格线/网格)

Bootstrap 提供了一套响应式、移动设备优先的流式网格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多 <u>**12**</u> 列。

简单使用方式一,自动栏宽：

col-md-4 表示像普通平板类型的设备(≥768px)竖版显示时,显示三个格线: 12/4=3

lg(≥992px)

xl(≥1200px)

xxl(≥1400px)

g 代表每个栏的边距，不用也行，自动留白. g-0代表无边距, 可以放置在row, 也可以放置在col,下面的代码放置在row上.

```html
    <div class="container-fluid">
        <div class="row g-4">
            <!-- 要多少栏,就用多少个 div class="col" -->
            <div class="col col-md-6 col-lg-4 col-xl-3 col-xxl-2">
                <div class="item">
                  <!-- w-100 = width 100% -->
                  <img src="img/img1.png" class="w-100">
                  <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
                </div>
            </div>
            <div class="col col-md-6 col-lg-4 col-xl-3 col-xxl-2">
                <div class="item">
                  <!-- w-100 = width 100% -->
                  <img src="img/img1.png" class="w-100">
                  <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
                </div>
            </div>
            <div class="col col-md-6 col-lg-4 col-xl-3 col-xxl-2">
                <div class="item">
                  <!-- w-100 = width 100% -->
                  <img src="img/img1.png" class="w-100">
                  <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
                </div>
            </div>
            <div class="col col-md-6 col-lg-4 col-xl-3 col-xxl-2">
              <div class="item">
                <!-- w-100 = width 100% -->
                <img src="img/img1.png" class="w-100">
                <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
              </div>
          </div>
          <div class="col col-md-6 col-lg-4 col-xl-3 col-xxl-2">
            <div class="item">
              <!-- w-100 = width 100% -->
              <img src="img/img1.png" class="w-100">
              <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
            </div>
        </div>
        </div>
    </div>
```

简单使用方式二,固定宽度:

col-12 表示满版,一个格线占满整个屏幕

```html
    <div class="container-fluid">
        <div class="row g-4">
            <div class="col-12 col-md-6 col-lg-4 col-xl-3 col-xxl-2">
                <div class="text">
                  <img src="img/img1.png">
                  Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.
                </div>
            </div>
            <div class="col-12 col-md-6 col-lg-4 col-xl-3 col-xxl-2">
              <div class="text">
                <img src="img/img1.png">
                Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.
              </div>
            </div>
            <div class="col-12 col-md-6 col-lg-4 col-xl-3 col-xxl-2">
              <div class="text">
                <img src="img/img1.png">
                Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.
              </div>
            </div>
            <div class="col-12 col-md-6 col-lg-4 col-xl-3 col-xxl-2">
              <div class="text">
                <img src="img/img1.png">
                Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.
              </div>
            </div>
            <div class="col-12 col-md-6 col-lg-4 col-xl-3 col-xxl-2">
              <div class="text">
                <img src="img/img1.png">
                Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.
              </div>
            </div>
            <div class="col-12 col-md-6 col-lg-4 col-xl-3 col-xxl-2">
              <div class="text">
                <img src="img/img1.png">
                Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.
              </div>
            </div>
        </div>
    </div>
```

#### 对齐与分布

justify-content-around

justify-content-between

justify-content-center

justify-content-start

justify-content-end

相当于css中的justify-content样式,如:

```css
.flex {

	justify-content: space-between;

}
```

用来调整分隔页面时,空白与格线之间的排列方式, 同样有sm, md, lg, xl, xxl可选

```html
    <div class="container">
        <div class="row justify-content-around">
            <div class="col-12 col-md-3">
                <div class="item">
                    <img src="img/img1.png" class="w-100">
                    <h3>Title</h3>
                    <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>  
                </div>
            </div>
            <div class="col-12 col-md-3">
                <div class="item">
                    <img src="img/img1.png" class="w-100">
                    <h3>Title</h3>
                    <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
                </div>
            </div>
            <div class="col-12 col-md-3">
                <div class="item">
                    <img src="img/img1.png" class="w-100">
                    <h3>Title</h3>
                    <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>  
                </div>
            </div>
        </div>
    </div>
```

文字在图像中, 并文字居中

![image-20220104020400722](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104020400722.png)

align-content-center	垂直居中,也就是y轴居中

justify-content-center	水平居中,也就是x轴居中

h-100 高度100%

```css
    <style>
        .kv {
            width: 100%;
            height: 98vh;
            background-image: url(https://picsum.photos/1400/900/?random=10);
            background-size: cover;
        }
        .kv .text {
            text-align: center;
        }
    </style>

```

```html
    <div class="kv">
        <div class="container h-100">
            <div class="row h-100 justify-content-center align-content-center">
                <div class="col-8 col-md-6">
                    <div class="text">
                        <h1>Simon学bootstrap5</h1>
                        <p>Include every Bootstrap JavaScript plugin and dependency with one of our two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers. For more information about what’s included in Bootstrap, please see our contents section.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
```

#### 排序控制

用来控制排序, 

如:在手机上显示的顺序为ABCD,在电脑上显示为CABD,可以用order来控制

下面的h-100用来控制在不同设备上,每个栏都有相同的高度

mb是控制行间距

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello, world!</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  <style>
      .item:first-letter {
          font-size: 50px;
          float: left;
      }
      .item {
          background-color: #CCC;
      }
  </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-3 mb-4 ">
                <div class="item h-100">
                    A Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.
                </div>
            </div>
            <div class="col-12 col-md-3 mb-4 ">
                <div class="item h-100">
                    B Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.
                </div>
            </div>
            <div class="col-12 col-md-3 mb-4 order-md-first">
                <div class="item h-100">
                    C Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.
                </div>
            </div>
            <div class="col-12 col-md-3 mb-4 ">
                <div class="item h-100">
                    D Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

交错式排列

offset用来移动栏, 单位是栏

offset-md-4的意思是,当分辨率达到md时,这个栏向右移动4栏的间隔

 @media screen and (min-width: 768px) 的意思是,当屏幕大于768px时,应用某个样式

![image-20220104030607277](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104030607277.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello, world!</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<style>
  .text {
    background-color: #CCC;
    padding: 20px;
  }

  @media screen and (min-width: 768px) {
    .txt-block {
    margin-top: -100px;
    }
  }
</style>
<body>
    <div class="container">
      <div class="row">
        <div class="col-12 col-md-7">
          <div class="pic">
            <img src="https://picsum.photos/300/200/?random=10" class="w-100">
          </div>
        </div>
        <div class="col-12 col-md-7 offset-md-5 txt-block">
          <div class="text">
            <h2>simon learning bootstrap</h2>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
          </div>
        </div>
        <div class="col-12 col-md-7 offset-md-5 mt-5">
          <div class="pic">
            <img src="https://picsum.photos/300/200/?random=10" class="w-100">
          </div>
        </div>
        <div class="col-12 col-md-7 txt-block">
          <div class="text">
            <h2>simon learning bootstrap</h2>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
          </div>
        </div>
      </div>
    </div>
</body>
</html>
```

#### 图片

img-fluid 最大不会超过容器的边界，但是最小则是按照图片的解析度

其它的还是[查看文档](https://getbootstrap.com/docs/5.1/content/images/)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>

    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-4">
                <div class="item">
                    <img src="https://picsum.photos/300/200/?random=10" class="img-fluid">
                    <h3>simon learning bootstrap5!</h3>
                    <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
                </div>
            </div>
            <div class="col-12 col-md-4">
                <div class="item">
                    <img src="https://picsum.photos/300/200/?random=10" class="w-100">
                    <h3>simon learning bootstrap5!</h3>
                    <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
                </div>
            </div>
            <div class="col-12 col-md-4">
                <div class="item">
                    <img src="https://picsum.photos/300/200/?random=10">
                    <h3>simon learning bootstrap5!</h3>
                    <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

## Utilities

### margin和padding

|                               | margin | padding |
| ----------------------------- | ------ | ------- |
| top                           | mt     | pt      |
| bottom                        | mb     | pb      |
| left(文字阅读习惯从左往右读)  | ms     | ps      |
| right(文字阅读习惯从左往右读) | me     | pe      |
| left and right                | mx     | px      |
| top and bottom                | my     | py      |
| 四周                          | m      | p       |

size的范围 0-5与auto

padding不可以使用负值，margin需要手动启动

[文档](https://getbootstrap.com/docs/5.1/utilities/spacing/)

![image-20220104224021582](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104224021582.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>
        .text {
            background-color: #ffa;
        }
        @media screen and (min-width: 768px) {
            .pic-card .col-12:last-child {
            margin-top: -100px;
            }
        }
    </style>
</head>
<body>
    <div class="container pic-card">
        <div class="row">
            <div class="col-12 col-md-7 mb-3 mb-md-0">
                <div class="pic">
                    <img src="https://picsum.photos/300/150/?random=10" class="w-100 img-thumbnail">
                </div>
            </div>
            <div class="col-12 col-md-7 ms-auto">
                <div class="text p-4">
                    <h3>simon learning bootstrap5!</h3>
                    <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

### [display](https://getbootstrap.com/docs/5.1/utilities/display/)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <!-- md以下消失 -->
    <h1 class="d-none d-md-block">Hello, world!</h1>
    <!-- md以下显示 -->
    <p class="d-block d-md-none">Hello, world!</p>

    <!-- 
        手机显示
        平板直向消失
        平板横向显示
     -->
     <h1 class="d-block d-md-none d-lg-block">simon learning bootstrap5!</h1>
</body>
</html>
```

### [flex](https://getbootstrap.com/docs/5.1/utilities/flex/)

主要内容是排列，可以根据屏幕大小调整排序方式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="d-flex flex-column flex-md-row">
        <div class='item m-4'>
            <img src="https://picsum.photos/300/200/?random=10">
            <h3>simon learning bootstrap5!</h3>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
        </div>
        <div class='item m-4'>
            <img src="https://picsum.photos/300/200/?random=10">
            <h3>simon learning bootstrap5!</h3>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
        </div>
        <div class='item m-4'>
            <img src="https://picsum.photos/300/200/?random=10">
            <h3>simon learning bootstrap5!</h3>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
        </div>
        <div class='item m-4'>
            <img src="https://picsum.photos/300/200/?random=10">
            <h3>simon learning bootstrap5!</h3>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
        </div>
        <div class='item m-4'>
            <img src="https://picsum.photos/300/200/?random=10">
            <h3>simon learning bootstrap5!</h3>
            <p>Learn how to modify columns with a handful of options for alignment, ordering, and offsetting thanks to our flexbox grid system. Plus, see how to use column classes to manage widths of non-grid elements.</p>
        </div>
    </div>
</body>
</html>
```

### [Colors](https://getbootstrap.com/docs/5.1/utilities/colors/)

![image-20220105200227311](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105200227311.png)

### [background](https://getbootstrap.com/docs/5.1/utilities/background/)

![image-20220105201031790](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105201031790.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-gradient bg-success mb-3">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
    </nav>
    <h1 class="bg-primary bg-gradient p-4">Hello, world!</h1>
    <p class="text-primary">.text-primary</p>
    <p class="text-secondary">.text-secondary</p>
    <p class="text-success">.text-success</p>
    <p class="text-danger">.text-danger</p>
    <p class="text-warning bg-dark">.text-warning</p>
    <p class="text-info bg-dark">.text-info</p>
    <p class="text-light bg-dark">.text-light</p>
    <p class="text-dark">.text-dark</p>
    <p class="text-body">.text-body</p>
    <p class="text-muted">.text-muted</p>
    <p class="text-white bg-dark">.text-white</p>
    <p class="text-black-50">.text-black-50</p>
    <p class="text-white-50 bg-dark">.text-white-50</p>
</body>
</html>
```

### [溢出](https://getbootstrap.com/docs/5.1/utilities/overflow/)

![image-20220105202129348](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105202129348.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>
        .text {
            height: 200px;
            width: 200px;
            background-color: #aaa;
        }
        .pic {
            height: 200px;
            width: 200px;
            border-radius: 50%;
        }
        .pic img {
            object-fit: cover;
        }
    </style>
</head>
<body>
    <div class="text overflow-auto">
        <p>Adjust the overflow property on the fly with four default values and classes. These classes are not responsive by default.Adjust the overflow property on the fly with four default values and classes. These classes are not responsive by default.Adjust the overflow property on the fly with four default values and classes. These classes are not responsive by default.</p>
    </div>
    <div class="pic overflow-hidden">
        <img src="https://picsum.photos/200/300/?random=10">
    </div>
</body>
</html>
```



## Components

### [卡片组件](https://getbootstrap.com/docs/5.1/components/card)

![image-20220104230602502](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104230602502.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>
        .simon-card-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <div class="container mb-4">
        <div class="row">
            <div class="col-12 col-md-3">
                <div class="card">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-3">
                <div class="card">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-3">
                <div class="card">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-3">
                <div class="card">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6">
                <div class="card mb-3" style="max-width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="https://picsum.photos/300/200/?random=10" class="img-fluid rounded-start simon-card-img">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">Card title</h5>
                                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6">
                <div class="card mb-3" style="max-width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="https://picsum.photos/300/200/?random=10" class="img-fluid rounded-start simon-card-img">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">Card title</h5>
                                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

#### [Card layout](https://getbootstrap.com/docs/5.1/components/card/#card-layout)

##### [Card groups](https://getbootstrap.com/docs/5.1/components/card/#card-groups)

适用于栏数不多的情况

栏数过多示例：

![image-20220104231216826](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104231216826.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="card-group">
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=11" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=12" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=13" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=14" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=15" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
            <div class="card">
                <img src="https://picsum.photos/300/200/?random=16" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
            </div>
          </div>    
    </div>
</body>
</html>
```

##### [Grid cards](https://getbootstrap.com/docs/5.1/components/card/#grid-cards)

h-100用来控制每个栏长度一致

![image-20220104233541253](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104233541253.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="row row-cols-1 row-cols-md-3 row-cols-lg-4 g-4">
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=11" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=12" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=13" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
                </div>
            </div>
          </div>
    </div>
</body>
</html>
```

### [清单群组(list-group)](https://getbootstrap.com/docs/5.1/components/list-group/)

active	选中的样式

disabled	不可选的样式

#### [文字型清单群组](https://getbootstrap.com/docs/5.1/components/list-group/#basic-example)

```html
    <ul class="list-group">
        <li class="list-group-item">An item</li>
        <li class="list-group-item active">A second item</li>
        <li class="list-group-item disabled">A third item</li>
        <li class="list-group-item">A fourth item</li>
        <li class="list-group-item">And a fifth one</li>
      </ul>
```

#### [超链接](https://getbootstrap.com/docs/5.1/components/list-group/#links-and-buttons)

list-group-item-action	鼠标移到按钮后，白色背景变灰色背景

```html
<div class="list-group">
  <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
    The current link item
  </a>
  <a href="#" class="list-group-item list-group-item-action">A second link item</a>
  <a href="#" class="list-group-item list-group-item-action">A third link item</a>
  <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
  <a class="list-group-item list-group-item-action disabled">A disabled link item</a>
</div>
```

#### [flush](https://getbootstrap.com/docs/5.1/components/list-group/#flush)

用来移除容器外围的圆角和边框

![image-20220104234920436](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220104234920436.png)

```html
<ul class="list-group list-group-flush">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
  <li class="list-group-item">A fourth item</li>
  <li class="list-group-item">And a fifth one</li>
</ul>
```

完整html代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <ul class="list-group mb-5">
            <li class="list-group-item">An item</li>
            <li class="list-group-item active">A second item</li>
            <li class="list-group-item disabled">A third item</li>
            <li class="list-group-item">A fourth item</li>
            <li class="list-group-item">And a fifth one</li>
        </ul>
    
        <div class="list-group mb-5">
            <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
              The current link item
            </a>
            <a href="#" class="list-group-item list-group-item-action">A second link item</a>
            <a href="#" class="list-group-item list-group-item-action">A third link item</a>
            <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
            <a class="list-group-item list-group-item-action disabled">A disabled link item</a>
        </div>
        
        <ul class="list-group list-group-flush">
            <li class="list-group-item">An item</li>
            <li class="list-group-item">A second item</li>
            <li class="list-group-item">A third item</li>
            <li class="list-group-item">A fourth item</li>
            <li class="list-group-item">And a fifth one</li>
        </ul>
    </div>
</body>
</html>
```

flush与卡片结合

![image-20220105000209925](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105000209925.png)

```html
    <div class="container">
        <div class="row row-cols-1 row-cols-md-4">
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Plan 1</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">An item</li>
                        <li class="list-group-item">A second item</li>
                        <li class="list-group-item">A third item</li>
                        <li class="list-group-item">A fourth item</li>
                        <li class="list-group-item">And a fifth one</li>
                    </ul>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Plan 2</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">An item</li>
                        <li class="list-group-item">A second item</li>
                        <li class="list-group-item">A third item</li>
                        <li class="list-group-item">A fourth item</li>
                        <li class="list-group-item">And a fifth one</li>
                    </ul>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Plan 3</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">An item</li>
                        <li class="list-group-item">A second item</li>
                        <li class="list-group-item">A third item</li>
                        <li class="list-group-item">A fourth item</li>
                        <li class="list-group-item">And a fifth one</li>
                    </ul>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">Plan 4</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">An item</li>
                        <li class="list-group-item">A second item</li>
                        <li class="list-group-item">A third item</li>
                        <li class="list-group-item">A fourth item</li>
                        <li class="list-group-item">And a fifth one</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
```

### [面包屑(breadcrumb)](https://getbootstrap.com/docs/5.1/components/breadcrumb/)

![image-20220105033910231](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105033910231.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>
        .path {
            background-color: #aaa;
        }
        .breadcrumb {
            background-color: transparent;
            padding-top: 1%;
            padding-bottom: 1%;
        }
        .breadcrumb-item a {
            color: #000;
            text-decoration: none;
        }
        .breadcrumb-item.active {
            color: gray;
        }
    </style>
</head>
<body>
    <div class="path">
        <div class="container">
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb align-content-center">
                  <li class="breadcrumb-item"><a href="#">首页</a></li>
                  <li class="breadcrumb-item"><a href="#">Simon学Bootstrap5</a></li>
                  <li class="breadcrumb-item active" aria-current="page">面包屑</li>
                </ol>
            </nav>
        </div>
    </div>
</body>
</html>
```

### [分页(pagination)](https://getbootstrap.com/docs/5.1/components/pagination/)

![image-20220105040727321](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105040727321.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>
        .pagination .page-item {
            margin: 0 5px;
        }
        .pagination .page-item .page-link {
            border: none;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
    </nav>
    <div class="banner">
        <img src="https://picsum.photos/1300/200/?random=10" class="w-100">
    </div>
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb align-content-center">
          <li class="breadcrumb-item"><a href="#">首页</a></li>
          <li class="breadcrumb-item"><a href="#">Simon学Bootstrap5</a></li>
          <li class="breadcrumb-item active" aria-current="page">面包屑</li>
        </ol>
    </nav>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-3">
                <div class="list-group">
                    <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
                      The current link item
                    </a>
                    <a href="#" class="list-group-item list-group-item-action">A second link item</a>
                    <a href="#" class="list-group-item list-group-item-action">A third link item</a>
                    <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
                    <a class="list-group-item list-group-item-action disabled">A disabled link item</a>
                </div>
            </div>
            <div class="col-12 col-md-9">
                <div class="row row-cols-1 row-cols-md-3 row-cols-lg-4">
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card">
                            <img src="https://picsum.photos/300/200/?random=10" class="card-img-top">
                            <div class="card-body">
                              <h5 class="card-title">Card title</h5>
                              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                              <a href="#" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col pt-5">
                    <nav aria-label="Page navigation example">
                        <ul class="pagination justify-content-center">
                          <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                          <li class="page-item"><a class="page-link" href="#">1</a></li>
                          <li class="page-item"><a class="page-link" href="#">2</a></li>
                          <li class="page-item"><a class="page-link" href="#">3</a></li>
                          <li class="page-item"><a class="page-link" href="#">Next</a></li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

### [轮播图(carousel)](https://getbootstrap.com/docs/5.1/components/carousel/)

一个页面想要同时存在多组轮播图，每一组轮播图里如：`data-bs-target="#carouselExampleCaptions"`，#carouselExampleCaptions都必须要不一样

![image-20220105060900115](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105060900115.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="https://picsum.photos/1300/400/?random=10" class="d-block w-100">
            <div class="carousel-caption d-none d-md-block">
              <h5>First slide label</h5>
              <p>Some representative placeholder content for the first slide.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="https://picsum.photos/1300/400/?random=11" class="d-block w-100">
            <div class="carousel-caption d-none d-md-block">
              <h5>Second slide label</h5>
              <p>Some representative placeholder content for the second slide.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="https://picsum.photos/1300/400/?random=12" class="d-block w-100">
            <div class="carousel-caption d-none d-md-block">
              <h5>Third slide label</h5>
              <p>Some representative placeholder content for the third slide.</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
</body>
</html>
```

### [互动视窗(modal)](https://getbootstrap.com/docs/5.1/components/modal/)

激活modal的动作除了button，也可以是a，如果想要让a标签也能使用弹框，在class中添加`data-bs-toggle="modal" data-bs-target="#exampleModal"`

弹框默认是在屏幕上方中央，也可以让其位于屏幕中央，在`<div class="modal-dialog">`添加`modal-dialog-centered`。如果弹框内容是长文本，如xx法律许可之类的，可以添加`modal-dialog-centered modal-dialog-scrollable`

想要同时共存多个modal，需要指定不同modal的id如：`id="exampleModal2"`，然后引用的时候data-bs-target用id选择器选中对应的id如：`data-bs-target="#exampleModal2"`

满版的样式也同样在`modal-dialog`后面加

| class                        | Availability   |
| ---------------------------- | -------------- |
| `.modal-fullscreen`          | Always         |
| `.modal-fullscreen-sm-down`  | Below `576px`  |
| `.modal-fullscreen-md-down`  | Below `768px`  |
| `.modal-fullscreen-lg-down`  | Below `992px`  |
| `.modal-fullscreen-xl-down`  | Below `1200px` |
| `.modal-fullscreen-xxl-down` | Below `1400px` |

![image-20220105064530593](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105064530593.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">登入</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal2">一段长文本</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
    </nav>

    <!-- Button trigger modal -->
    <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Launch demo modal
    </button> -->
  
  <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
      <!-- Modal2 -->
      <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-fullscreen-lg-down">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                    <p>Below is a static modal example (meaning its position and display have been overridden). Included are the modal header, modal body (required for padding), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
```

### [Tooltips](https://getbootstrap.com/docs/5.1/components/tooltips/)

要使用前，需要先初始化

```html
    <script>
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        })
    </script>
```

鼠标指向按钮就会有提示

指定提示框显示方向`data-bs-placement='right'`(注意，如果空间不足，提示框会自动显示在空余的地方)

![image-20220105070826285](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105070826285.png)

### [Popovers](https://getbootstrap.com/docs/5.1/components/popovers/)

要使用前，需要先初始化

```js
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
```

鼠标点击按钮就会有提示

指定提示框显示方向`data-bs-placement='right'`(注意，如果空间不足，提示框会自动显示在空余的地方)

![image-20220105071010616](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105071010616.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <h1>Hello, world!</h1>
    <button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="top" title="simon learning bootstrap5!">
        Tooltip on bottom
    </button>
    <button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" data-bs-placement="top" title="simon learning bootstrap5" data-bs-content="And here's some amazing content. It's very engaging. Right?">Click to toggle popover</button>
</body>
<script>
    // ToolTips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
    // Popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
</script>
</html>
```

### [折叠](https://getbootstrap.com/docs/5.1/components/collapse/)

折叠有两种制作方式：

方式一为用a标签的href属性`href="#collapseExample"`(相当于锚点指向折叠内容的id)；

方式二为button标签，添加`data-bs-target="#collapseExample"`(指向折叠内容的id)属性。

### [手风琴](https://bootstrap5.hexschool.com/docs/5.1/components/accordion/)

可以用来做折叠的导航栏

多个折叠或手风琴共存需要修改对应的id与id选择器的值

手风琴除了修改`data-bs-target`,还要修改`data-bs-parent`

![image-20220105195442475](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220105195442475.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <h1>Hello, world!</h1>
    <div class="container">
        <div  data-bs-toggle="collapse" href="#collapseExample">simon学bootstrap</div>
        <p>
            <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
              Link with href
            </a>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
              Button with data-bs-target
            </button>
          </p>
          <div class="collapse" id="collapseExample">
            <div class="card card-body">
              Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
            </div>
          </div>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-4">
                <div class="accordion" id="accordionExample1">
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="headingOne">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne1" aria-expanded="true" aria-controls="collapseOne">
                          Accordion Item #1
                        </button>
                      </h2>
                      <div id="collapseOne1" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample1">
                        <div class="accordion-body">
                          <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                      </div>
                    </div>
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="headingTwo">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo2" aria-expanded="false" aria-controls="collapseTwo">
                          Accordion Item #2
                        </button>
                      </h2>
                      <div id="collapseTwo2" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample1">
                        <div class="accordion-body">
                          <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                      </div>
                    </div>
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="headingThree">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree3" aria-expanded="false" aria-controls="collapseThree">
                          Accordion Item #3
                        </button>
                      </h2>
                      <div id="collapseThree3" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample1">
                        <div class="accordion-body">
                          <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                      </div>
                    </div>
                </div>
            </div>
            <div class="col-8">
                <div class="accordion" id="accordionExample">
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="headingOne">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                          Accordion Item #1
                        </button>
                      </h2>
                      <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                          <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                      </div>
                    </div>
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="headingTwo">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                          Accordion Item #2
                        </button>
                      </h2>
                      <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                          <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                      </div>
                    </div>
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="headingThree">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                          Accordion Item #3
                        </button>
                      </h2>
                      <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                          <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                      </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

## [Forms](https://getbootstrap.com/docs/5.1/forms/overview/)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center my-5">
            <div class="col-6 ">
                <form>
                    <div class="mb-3">
                      <label for="exampleInputEmail1" class="form-label">Email address</label>
                      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                      <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleColorInput" class="form-label">Color picker</label>
                        <input type="color" class="form-control form-control-color" id="exampleColorInput" value="#563d7c" title="Choose your color">
                    </div>
                    <div class="mb-3">
                      <label for="exampleInputPassword1" class="form-label">Password</label>
                      <input type="password" class="form-control" id="exampleInputPassword1">
                    </div>
                    <div class="mb-3 form-check">
                      <input type="checkbox" class="form-check-input" id="exampleCheck1">
                      <label class="form-check-label" for="exampleCheck1">Check me out</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                  </form>
            </div>
        </div>
    </div>
</body>
</html>
```

![image-20220106020612036](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220106020612036.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-6 mx-auto my-5">
                <select class="form-select" aria-label="Default select example">
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                </select>

                <div class="mb-3">
                    <label for="formFile" class="form-label"></label>
                    <input class="form-control" type="file" id="formFile">
                  </div>
            </div>
        </div>
    </div>
</body>
</html>
```

![image-20220106022300476](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220106022300476.png)

### [input group](https://getbootstrap.com/docs/5.1/forms/input-group/)

![image-20220106024037865](bootstrap5%E7%AC%94%E8%AE%B0.assets/image-20220106024037865.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, world!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-6 mx-auto my-5">
                <div class="input-group mb-3">
                    <span class="input-group-text">信箱</span>
                    <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
                    <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
                    <span class="input-group-text">@gmail.com</span>
                    <button type="button" class="btn btn-info">送出</button>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-6 mx-auto my-5">
                <div class="input-group">
                    <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon">
                      <option selected>Choose...</option>
                      <option value="1">One</option>
                      <option value="2">Two</option>
                      <option value="3">Three</option>
                    </select>
                    <button class="btn btn-outline-secondary" type="button">Button</button>
                  </div>
            </div>
        </div>
        <div class="row">
            <div class="col-6 mx-auto my-5">
                <div class="input-group mb-3">
                    <input type="file" class="form-control" id="inputGroupFile02">
                    <label class="input-group-text" for="inputGroupFile02">Upload</label>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
```

