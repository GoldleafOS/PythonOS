
import subprocess
import os
print("""
      Game.py 贪吃蛇游戏    1
      WWW.py  浏览器       2 
      bombom.py 枪战游戏[beta开发中---AI开发的] 3
      
      
      
      
      
      """)
api = input("数字开启:")
#我懒得写注释,因为我的代码很浅显易懂
if api == "1":
    subprocess.run(["python3", "game.py"])

if api == "2":
    subprocess.run(["python3", "www.py"])
if api == "3":
    subprocess.run(["python3", "bombom.py"])
else:
    print("回到系统")
    sysos = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'PythonOSsys', 'kernel.py')
    subprocess.run(["python3", sysos])


#App_api开发者示例
#if api == "x(数字)":
    #subprocess.run(["python3", "yourapps.py"])
