
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# 设置屏幕
wn = turtle.Screen()
wn.title("太空与球")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # 关闭屏幕更新

# 创建蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# 创建蛇食
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# 分数板
score_board = turtle.Turtle()
score_board.speed(0)
score_board.shape("square")
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("得分: 0  最高分: 0", align="center", font=("Courier", 24, "normal"))

# 定义函数
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 键盘绑定
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# 主游戏循环
while True:
    wn.update()

    # 检查碰撞边界
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # 隐藏段
        for segment in segments:
            segment.goto(1000, 1000) # 移出屏幕
        segments.clear()

        # 重置分数
        score = 0
        score_board.clear()
        score_board.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 检查碰撞食物
    if head.distance(food) < 20:
        # 移动食物到随机位置
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # 添加一个段
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # 增加分数
        score += 10
        if score > high_score:
            high_score = score
        score_board.clear()
        score_board.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 移动蛇身体
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # 检查头部与身体碰撞
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # 隐藏段
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # 重置分数
            score = 0
            score_board.clear()
            score_board.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
