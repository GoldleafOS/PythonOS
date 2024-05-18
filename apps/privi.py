import os
import subprocess
print("""
ppppp   rrrrr   iiii  v   v  iiii
p   p   r   r    ii   v   v   ii
ppppp   rrrrr    ii   v   v   ii
p       r  r     ii    v v    ii
p       r   r   iiii    v    iiii
#######################################
#the PythonOS s vim---vim for pythonos#
#######################################
""")

pyos_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps', 'app_api.py')




def simple_vim():
    print("PRINT VIM V1.0   PythonOS重写版VIM")
    print("只能保存txt和sh文件")
    filename = input("请输入文件名（包含扩展名）: ")
    if not (filename.endswith('.txt') or filename.endswith('.sh')):
        print("错误1：文件扩展名必须是.txt或.sh")
        return
    
    print("现在您可以开始输入内容。输入':wq'以保存并退出，输入':q!'以不保存退出。")
    lines = []
    while True:
        line = input()
        if line == ':wq':
            with open(filename, 'w') as file:
                file.write('\n'.join(lines))
            print(f"文件已保存：{filename}")
            #回到app
            pyos_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps', 'app_api.py')
            subprocess.run(["python3", pyos_path])

        elif line == ':q!':
            print("退出未保存。")
            #回到app
            pyos_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps', 'app_api.py')
            subprocess.run(["python3", pyos_path])
        else:
            lines.append(line)

simple_vim()