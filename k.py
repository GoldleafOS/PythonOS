#当本程序开始时,内核部分
print("[OKAY]BOOT OK")
#加载
import turtle
import time as tm
import getpass
import datetime
import calendar
import os

# 创建一个新窗口
#win = turtle.Screen()
#win.bgcolor("white")

# 创建一个新的海龟
#load_turtle = turtle.Turtle()
#load_turtle.speed(1)

# 创建一个进度条的海龟
#progress_turtle = turtle.Turtle()
#progress_turtle.penup()
#progress_turtle.hideturtle()
#progress_turtle.goto(-150, -200)  # 设置进度条的位置

# 创建一个"加载中"的动画
#for i in range(36):
#    load_turtle.forward(100)
#    load_turtle.right(170)
#    time.sleep(0.1)  # 暂停0.1秒

    # 更新进度条
#    progress_turtle.clear()
#    progress_turtle.write(f"进度: {i+1}/36", align="left", font=("Arial", 10, "normal"))

# 隐藏海龟
#load_turtle.hideturtle()

# 保持窗口打开
#turtle.done()
#本来想做一个文件系统的#Sdi = home 
print("#   MOLINUX V1.0 #")
print("# GNU xingzhuolii#")
print("#you can input   #")
print("#to system       #")
#passwd mode
count = 0
stpasswd = "adminpasswd"
#log in

while count < 3:
    user = input("Login: ")
    if user == "root":
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
#进度条部分,在bbcos的开源上https://blog.csdn.net/qq_62293794/article/details/128476017

                tm.sleep(1.5)
                while count < 3:
                    bash = input("~# ")
                    if bash == "ls" or bash == "dir":
                        print("Downloads  Documents  Music  Pictures")
                    elif bash == "ver" or bash == "version" or bash == "-v" or bash == "-ver" or bash == "-version":
                        print("MOLinux is v:1.0.23.12.10.Dev on OpenBBC OS (R) Core Open Source System 1.2 ")
                    elif bash == "coverter":
                        print("File Covert\nCovert .lpap/.lpcu/.bbc to .umm")
                        input("Input file's path:\n")
                        print("Coverting [____________________] 0%")
                        tm.sleep(0.3)
                        print("Coverting [######______________] 30%")
                        tm.sleep(0.3)
                        print("Coverting [############________] 60%")
                        tm.sleep(0.3)
                        print("Coverting [################____] 80%")
                        tm.sleep(0.3)
                        print("Coverting [####################] 100%")
                        tm.sleep(0.09)
                        print("Covert Complete.")
                    elif bash == "time" or bash:
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
                    elif bash == "repasswd":
                        stpasswd = input("Input new password: ")
                    elif bash == "calendar" or bash == "日历" :
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(calendar.month(yy, mm))
                    elif bash == "calc" or bash == "计算器":
                        try:
                            formula = input("Enter the formula to be calculated:\n")
                            print(formula + "=", eval(formula))
                        except Exception as e:
                            print("Input error.")
                    elif bash == "clear":
                        i = os.system("cls")
                    else:
                        print("Error password! Please retry") 
 


