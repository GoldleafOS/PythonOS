import pygame
import os
import subprocess
minecraft_logo = """
███╗   ███╗██╗███╗   ██╗███████╗███████╗██████╗ ███████╗
████╗ ████║██║████╗  ██║██╔════╝██╔════╝██╔══██╗██╔════╝
██╔████╔██║██║██╔██╗ ██║███████╗█████╗  ██████╔╝███████╗
██║╚██╔╝██║██║██║╚██╗██║╚════██║██╔══╝  ██╔══██╗╚════██║
██║ ╚═╝ ██║██║██║ ╚████║███████║███████╗██║  ██║███████║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
==========================================================
为PythonOS专门重写的Minecraft
"""
print(minecraft_logo)
import sys

import pygame
import sys

import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("我的世界")

# 设置颜色
white = (255, 255, 255)
green = (0, 255, 0)

# 设置方块的初始位置和大小
block_size = 50
x = window_size[0] // 2 - block_size // 2
y = window_size[1] // 2 - block_size // 2

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 检测按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # 填充背景色
    screen.fill(white)

    # 绘制方块
    pygame.draw.rect(screen, green, [x, y, block_size, block_size])

    # 更新屏幕显示
    pygame.display.flip()

    # 在终端询问是否退出
    exit_command = input("要退出游戏吗？输入'ok'退出: ")
    if exit_command.lower() == "ok":
        pyos_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps', 'app_api.py')
        subprocess.run(["python3", pyos_path])

# 退出pygame
pygame.quit()
sys.exit()























































