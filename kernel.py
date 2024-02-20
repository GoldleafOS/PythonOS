#当本程序开始时,内核部分
import os
print("[OKAY]BOOT OK")
print("[OKAY]Python3:su")
print("[inp]system")
import sys
print("[OKAY]SYSok")
print("[inp]time")
import time as tm
print("[OKAY]time_BY_TM")
print("[inp]Graphics")
import turtle
print("[OKAY]Graphics_BY_TTLE")
import getpass
import datetime
import calendar
print("[OKAY]Plugin_OK")
import subprocess
print("[OKAY]app")

print("##---------------- 12%")
import openai
print("########-----------48%")
import mlx
print("################---96%")
print("##################100%")
Dev = "yes"
yes = "ok"
int_ = "boot"
print("[OKAY]boot OKAY")

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
print("""
              #########
            ##         ##
           #             #
          #      ###      #
          #      #  #     #
          #      ###      #
           #     #       #
            ##         ##
              #########
""")
print('############################')
print('#        PythonOS V1.3     #')
print('#     GNU Open Project     #')
print('# you can inputto system   #')
print('#xingzhuolii528@outlook.com#')
print("#      GITHUBVersion       #")
print("#        Dev   开发版       #")
print('############################')



#passwd mode
count = 0
stpasswd = "passwd"
#log in

while count < 3:
    user = input("Login: ")
    if user == "admin":
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
            
#进度条部分,在bbcos的开源上https://blog.csdn.net/qq_62293794/article/details/128476017

                tm.sleep(1.5)
                while count < 3:
                    bash = input("MOLinux-sudo@mx ~ $ ")
                    if bash == "ls" or bash == "dir":
                        print("Downloads  Documents  Music  Pictures")
                    if bash == "ver" or bash == "version" or bash == "-v" or bash == "-ver" or bash == "-version":
                        print("MOLinux is v:1.0.23.12.10.Dev on OpenBBC OS (R) Core Open Source System 1.2 ")
                    if bash == "coverter":
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
                    if bash == "time" or bash:
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
                    if bash == "repasswd":
                        stpasswd = input("Input new password: ")
                    if bash == "calendar" or bash == "日历" :
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(calendar.month(yy, mm))
                    if bash == "calc" or bash == "计算器":
                        try:
                            formula = input("Enter the formula to be calculated:\n")
                            print(formula + "=", eval(formula))
                        except Exception as e:
                            print("Input error.")
                    if bash == "clear":
                        i = os.system("cls")

                    if bash == "vim":
                        # 使用subprocess模块执行Python脚本
                        subprocess.run(["python3", "privi.py"])
                    if bash == "app":
                        subprocess.run(["python", "app.py"])


                    if bash == 'help':
                        print('ver 查看系统版本')
                        print('time 设定时间')
                        print('repasswd 重新设置密码')
                        print('dir 查看文件系统')
                        print('calendar 日历功能')
                        print('calc 计算器')
                        print('exit 退出')
                        print('coverter ???')
                        print('app 启动应用程序')
                        print('vim 启动vim')
                        
                    if bash == 'exit':
                        break
                    
                        print("Error password! Please retry") 
 


