
print("[Fastboot]booting")
import subprocess
fastboot = input("Bash and GUI:")#"Bash"        
if fastboot == "GUI":
    subprocess.run(["python", "GUI.py"])
if fastboot == "Bash":
    subprocess.run(["python3", "kernel.py"])
if fastboot == "Debug":
    print("""if fastboot == "Debug":
    import os
    import sys
    import getpass
import datetime
import calendar
import time as tm
count = 0
stpasswd = "adminpasswd"
#log in
import datetime
import calendar
import time as tm
count = 0  # Move this line outside and before any if statements
stpasswd = "debugpasswd"
while count < 3:
    user = input("Login: ")
    if user == "Debug":
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                bash = input("MOLinux-root@mx ~ # ")
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
                        #now = datetime.datetime.now()
                        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
                if bash == "repasswd":
                        stpasswd = input("Input new password: ")
               
                if bash == "clear":
                        i = os.system("cls")
                    

                if bash == 'help':
                        print('repasswd 重新设置密码')
                        print('dir 查看文件系统')
                if bash == 'exit':
                        break
                """)

else:
    print("error") 
