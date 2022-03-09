# 员工的周工资等于小时工资乘以正常的总工作时间再加上加班工资。加班工资等于总加班时间乘以小时工资的1.5倍. 编写一个程序,让用户可以输入小时工资、正常的总工作时间以及加班总时间, 然后显示出员工的周工资.

def salaryCount(preSalary, hours, overtimeHours=0):
    salarySum = preSalary * hours + overtimeHours * preSalary * 1.5
    return float(salarySum)


print(salaryCount(17, 8, 4))