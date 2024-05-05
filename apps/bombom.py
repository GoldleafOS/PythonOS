import pygame
import math

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置颜色
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# 设置游戏运行状态和时钟
running = True
clock = pygame.time.Clock()

# 玩家血量
health = 5

# 子弹列表
bullets = []

# 绘制血量
def draw_health():
    for i in range(health):
        pygame.draw.polygon(screen, yellow, [
            (screen_width - (i+1)*40 + 10, 10),
            (screen_width - (i+1)*40 + 20, 20),
            (screen_width - (i+1)*40 + 10, 30),
            (screen_width - (i+1)*40, 30),
            (screen_width - (i+1)*40 - 10, 20),
            (screen_width - (i+1)*40, 10),
        ])

# 玩家类
class Player:
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height - 100
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, white, (self.x, self.y, 40, 60))

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        if direction == "RIGHT" and self.x < screen_width - 40:
            self.x += self.speed

# 子弹类
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def draw(self):
        pygame.draw.circle(screen, white, (self.x, self.y), 5)

    def move(self):
        self.y -= self.speed

player = Player()

# 游戏主循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 发射子弹
                bullets.append(Bullet(player.x + 20, player.y))

    # 按键检测
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("LEFT")
    if keys[pygame.K_RIGHT]:
        player.move("RIGHT")

    # 更新游戏状态
    screen.fill(black)
    player.draw()
    for bullet in bullets:
        bullet.draw()
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)

    draw_health()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()                                
