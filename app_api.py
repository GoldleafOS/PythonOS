print("[OKAY]开启应用转接模块")
import subprocess
print("为了安全,所以以后的应用,都会在这里打开")
print("PyApps适配内核3.xx(python3)")
print("""现在可使用:
      Game.py 贪吃蛇游戏    1
      WWW.py  浏览器       2 
      bombom.py 枪战游戏[beta开发中---AI开发的] 3
      
      
      
      
      
      """)
api = input("按数字编号开启:")
#我懒得写注释,因为我的代码很浅显易懂
if api == "1":
    subprocess.run(["python3", "game.py"])

if api == "2":
    subprocess.run(["python3", "WWW.py"])
if api == "3":
    subprocess.run(["python3", "bombom.py"])
else:
    print("回到系统")
    subprocess.run(["python3", "kernel.py"])

