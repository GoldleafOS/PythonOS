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

print('############################')
print('#          DebugOS         #')
print('#     GNU Open Project     #')
print('# you can input to system  #')
print('#xingzhuolii528@outlook.com#')
print("#      GITHUBVersion       #")
print("#        Debug mode        #")
print('############################')

while count < 3: 
    user = input("Enter to Debug(usermode): ")

    if user == "Debug":
        while count < 3:
            passwd = getpass.getpass("Enter to Debug(passwdmode): ")
            passwd = "debugpasswd"
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
                if bash == "time":
                    now = datetime.datetime.now()
                    other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
                    print(other_StyleTime)
                if bash == "repasswd":
                        stpasswd = input("Input new password: ")
               
                if bash == "clear":
                        i = os.system("cls")
                    

                if bash == 'help':
                        print('repasswd 重新设置密码')
                        print('dir 查看文件系统')
                if bash == 'exit':
                        break
                

else:
    print("error") 