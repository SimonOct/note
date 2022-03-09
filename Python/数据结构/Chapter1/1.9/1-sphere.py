# 1.编写一个程序,使之能够接收球体的半径(浮点数),并且可以输出球体的直径、周长、表面积以及体积.
import math

def sphere():
    # 题目的周长我理解是以这个球体为中心点,半径相同的圆的周长
    try:
        radius = float(input("Enter a number: "))
    except ValueError:
        print("Invaild input! Please try again")
        return sphere()
    diameter = radius * 2
    circumference = 2 * math.pi * radius
    surface_area = 4 * math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3
    print(
        f"diameter was {diameter},\ncircumference was {circumference},\nsphere surface area was {surface_area},\nvolume was {volume}"
    )
if __name__ == "__main__":
    while True:
        sphere()
        prompt = input("Do you want to try again(y/n)?: ").lower()
        if prompt == "y" or prompt == "yes":
            pass
        else:
            print("Exited!")
            break