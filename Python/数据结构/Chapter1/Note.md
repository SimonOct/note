# 1.5.2 递归函数

在学习的时候看到这样的示例代码

```python
def ourSum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result =  lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
ourSum(1, 4)
```

它的运行结果是: 

```bash
 1 4
     2 4
         3 4
             4 4
                 5 4
                 0
             4
         7
     9
 10
```

我一开始都没明白为什么这段代码运行的结果会是这么奇特, 后来在[Python Tutor](https://pythontutor.com)的帮助下得出我的理解

首先将结果以"5 4" "0"的中间为界一分为二. 

**第一部分**

- 第一次执行

把 lower=1, upper=4传入到ourSum(), 接着`print(blanks, lower, upper)`将" 1 4"打印出来

| lower | upper | margin |
| ----- | ----- | ------ |
| 1     | 4     | 0      |

此时因为 lower < upper, 则执行 `result = lower + ourSum(lower + 1, upper, margin + 4)`, 在第一部分中, lower这个变量无作用, 删掉也不会造成影响. 

因为有`ourSum(lower + 1, upper, margin + 4)`这个的存在, 将lower=2, upper=4, margin=4传入到ourSum()

等待

- 第二次执行

| lower | upper | margin |
| ----- | ----- | ------ |
| 2     | 4     | 4      |

将"     2 4"打印出来

此时因为 lower < upper, 则执行 `result = lower + ourSum(lower + 1, upper, margin + 4)`

将lower=3, upper=4, margin=8传入到ourSum()

等待

- 第三次执行

| lower | upper | margin |
| ----- | ----- | ------ |
| 3     | 4     | 8      |

将"         3 4"打印出来

此时因为 lower < upper, 则执行 `result = lower + ourSum(lower + 1, upper, margin + 4)`

将lower=4, upper=4, margin=12传入到ourSum()

等待

- 第四次执行

| lower | upper | margin |
| ----- | ----- | ------ |
| 4     | 4     | 12     |

将"             4 4"打印出来

此时因为 lower < upper, 则执行 `result = lower + ourSum(lower + 1, upper, margin + 4)`

将lower=5, upper=4, margin=16传入到ourSum()

等待

- 第五次执行

| lower | upper | margin |
| ----- | ----- | ------ |
| 5     | 4     | 16     |

将"                 5 4"打印出来

**第二部分**

此时因为 lower > upper, 则执行 `print(blanks, 0)`将"                 0"打印出来

执行 `return 0`, 此时第四次执行的 `result =  lower + ourSum(lower + 1, upper, margin + 4)`有了结果

第四次执行的`ourSum(lower + 1, upper, margin + 4)`输出的结果为0

- 第四次执行继续


| lower | upper | margin |
| ----- | ----- | ------ |
| 4     | 4     | 12     |

`result = 4 + 0`

`print("            ", 4)`

输出"             4"
- 第三次执行继续


| lower | upper | margin |
| ----- | ----- | ------ |
| 3     | 4     | 8      |

`result = 3 +              4`

`print("        ", 7)`

输出"         7"
- 第二次执行继续


| lower | upper | margin |
| ----- | ----- | ------ |
| 2     | 4     | 4      |

`result = 2 +          7`

`print("    ", 9)`

输出"     9"
- 第一次执行继续


| lower | upper | margin |
| ----- | ----- | ------ |
| 1     | 4     | 0      |

`result = 1 +      9`

`print("", 10)`

输出" 10"

`ourSum(1, 4)`运行结束

也不知道这样理解对不对, 毕竟能解释为什么会出现这样的情况
