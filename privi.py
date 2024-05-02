import os

def simple_vim():
    print("简易Vim编辑器启动。支持保存txt和sh文件。")
    filename = input("请输入文件名（包含.txt或.sh扩展名）: ")
    if not (filename.endswith('.txt') or filename.endswith('.sh')):
        print("错误：文件扩展名必须是.txt或.sh")
        return
    
    print("现在您可以开始输入内容。输入':wq'以保存并退出，输入':q!'以不保存退出。")
    lines = []
    while True:
        line = input()
        if line == ':wq':
            with open(filename, 'w') as file:
                file.write('\n'.join(lines))
            print(f"文件已保存：{filename}")
            break
        elif line == ':q!':
            print("退出未保存。")
            break
        else:
            lines.append(line)

simple_vim()
