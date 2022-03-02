# Ajax

## 原生Ajax

### GET

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>get</title>
    <style>
        #result{
            width: 200px;
            height: 100px;
            border: solid 1px #99c;
        }
    </style>
</head>
<body>
    <button>点击发送请求</button>
    <div id="result"></div>

    <script>
        // 获取button元素
        const btn = document.getElementsByTagName('button')[0];
        const result = document.getElementById('result');
        // 绑定事件
        btn.onclick = function() {
            // 创建对象
            const xhr = new XMLHttpRequest();
            // 初始化
            xhr.open('GET', 'http://localhost:3000/server?a=100&b=200&c=300')
            // 发送
            xhr.send();
            // 事件绑定 处理服务器返回的结果
            // on when 当......时候
            // readystate 是xhr对象中的属性，表示状态 0(初始) 1(open结束) 2(send结束) 3(服务端返回部分结果) 4(服务端返回所有结果)
            // change 改变
            xhr.onreadystatechange = function() {
                // 判断(服务端返回了所有的结果)
                if (xhr.readyState === 4) {
                    // 判断响应状态码
                    if (xhr.status >= 200 && xhr.status < 300) {
                        // 处理结果 行 头 空行 体
                        // 响应行
                        // console.log(xhr.status); // 状态码
                        // console.log(xhr.statusText); // 状态字符串
                        // console.log(xhr.getAllResponseHeaders); // 所有响应头
                        // // 响应体
                        // console.log(xhr.response);

                        // 设置result的文本
                        result.innerHTML = xhr.response;
                    } else {

                    }
                }
            }
        }
    </script>
</body>
</html>
```

### POST

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POST</title>
    <style>
        #result {
            width: 200px;
            height: 100px;
            border: solid 1px #903;
        }
    </style>
</head>
<body>
    <div id="result"></div>
    <script>
        // 获取元素对象
        const result = document.getElementById('result');
        // 绑定事件
        result.addEventListener('mouseover', function () {
            // 创建对象
            const xhr = new XMLHttpRequest();
            // 初始化 设置类型与url
            xhr.open('POST', 'http://localhost:3000/server');
            // 发送
            xhr.send('a=100&b=200&c=300');
            // 事件绑定
            xhr.onreadystatechange = function () { 
                if (xhr.readyState === 4) {
                    if (xhr.status >= 200 && xhr.status < 300) {
                        // 处理服务端返回的结果
                        result.innerHTML = xhr.response;
                    }
                }
            }
        })
    </script>
</body>
</html>
```

### 请求头

 设置请求头

`xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')`

响应头, 此处需要服务器设置 `'Access-Control-Allow-Headers', '*'`

 `xhr.setRequestHeader('name', 'simon')`

### JSON

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #result {
            width: 200px;
            height: 100px;
            border: solid 1px #903;
        }
    </style>
</head>
<body>
    <div id="result"></div>
    <script>
        const result = document.getElementById('result');
        // 绑定键盘按下事件
        window.onkeydown = function () {
            // 发送请求
            const xhr = new XMLHttpRequest();
            // 设置响应体数据的类型
            xhr.responseType = 'json';
            xhr.open('GET', 'http://localhost:3000/json-server');
            // 发送
            xhr.send();
            // 事件绑定
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status >= 200 && xhr.status < 300) {
                        
                        // console.log(xhr.response);
                        // result.innerHTML = xhr.response;
                        // 手动对数据转化
                        // let data = JSON.parse(xhr.response);
                        // console.log(data);
                        // result.innerHTML = data.name;
                        // 自动转换 设置响应体数据的类型
                        console.log(xhr.response);
                        result.innerHTML = xhr.response.name;
                    }
                }
            }
        }
    </script>
</body>
</html>
```

### 异常

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>异常</title>
    <style>
        #result{
            width: 200px;
            height: 100px;
            border: solid 1px #99c;
        }
    </style>
</head>
<body>
    <button>点击发送请求</button>
    <div id="result"></div>

    <script>
        // 获取button元素
        const btn = document.getElementsByTagName('button')[0];
        const result = document.getElementById('result');
        // 绑定事件
        btn.addEventListener('click', function() {
            const xhr = new XMLHttpRequest();
            // 超时设置
            xhr.timeout = 2000;
            // 超时回调
            xhr.ontimeout = function() {
                alert('网络异常, 请稍后重试!')
            }
            // 网络异常回调
            xhr.onerror = () => {
                alert('你的网络似乎出现了一些问题')
            }
            xhr.open('GET', 'http://localhost:3000/delay')
            xhr.send();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status >= 200 && xhr.status < 300) {
                        result.innerHTML = xhr.response;
                    } else {

                    }
                }
            }
        })
    </script>
</body>
</html>
```

### 取消

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>取消</title>
</head>
<body>
    <button>点击发送</button>
    <button>点击取消</button>
    <script>
        // 获取元素对象
        const btns = document.querySelectorAll('button')
        let x = null;
        btns[0].onclick = () => {
            x = new XMLHttpRequest();
            x.open('GET', 'http://localhost:3000/delay')
            x.send();
        }
        // abort
        btns[1].onclick = () => {
            x.abort()
        }
    </script>
</body>
</html>
```

### 重复发送

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>取消</title>
</head>
<body>
    <button>点击发送</button>
    <script>
        // 获取元素对象
        const btns = document.querySelectorAll('button')
        let x = null;
        let isSending = false; // 是否正在发送Ajax请求
        btns[0].onclick = () => {
            if (isSending) {
                return;
            }
            x = new XMLHttpRequest();
            // 修改表示变量的值
            isSending = true;
            x.open('GET', 'http://localhost:3000/delay')
            x.send();
            x.onreadystatechange = () => {
                if (x.readyState === 4) {
                    // 不需要判断status, 如果遇到失败的请求, 那么isSending将永远不会变成false
                    isSending = false;
                }
            }
        }
        // abort
        btns[1].onclick = () => {
            x.abort()
        }
    </script>
</body>
</html>
```

