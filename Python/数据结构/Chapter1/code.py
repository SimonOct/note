# 1.5.3
def ourSum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result


ourSum(1, 4)

# 1.9 编程项目
# 1.编写一个程序,使之能够接收球体的半径(浮点数),并且可以输出球体的直径、周长、表面积以及体积.


def sphere(radius):
    diameter = radius * 2
    #题目的周长我理解是以这个球体为中心点,半径相同的圆的周长
    import math

    circumference = 2 * math.pi * radius
    surface_area = 4 * math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3
    print(
        f"diameter was {diameter},\ncircumference was {circumference},\nsphere surface area was {surface_area},\nvolume was {volume}"
    )


sphere(3.14)
# 2.员工的周工资等于小时工资乘以正常的总工作时间再加上加班工资。加班工资等于总加班时间乘以小时工资的1.5倍. 编写一个程序,让用户可以输入小时工资、正常的总工作时间以及加班总时间, 然后显示出员工的周工资.


def salaryCount(preSalary, hours, overtimeHours=0):
    salarySum = preSalary * hours + overtimeHours * preSalary * 1.5
    return float(salarySum)


print(salaryCount(17, 8, 4))
# 有一个标准的科学实验: 扔一个球, 看看它能反弹多高. 一旦确定了球的"反弹高度", 这个比值就给出了相应的反弹度指数. 例如, 如果从10ft高出掉落的球可以反弹到6ft高,那么相应的反弹指数就是0.6; 
# 在一次反弹之后, 球的总行进距离是16ft. 接下来, 球继续弹跳, 那么两次弹跳后的总距离应该是: 10ft + 6ft + 6ft + 3.6ft = 25.6ft.
# 可以看到,每次连续弹跳所经过的距离是: 球到地面的距离, 加上这个距离乘以0.6, 这是球又弹回来了. 编写一个程序,可以让用户输入球的初始高度和允许球弹跳的次数.并输出球所经过的总距离.

def bounceDistance(height, bounces=1):
    distanceSum = height + height * 0.6
    if bounces > 1:
        for i in range(2, bounces+1):
            distanceSum += 

