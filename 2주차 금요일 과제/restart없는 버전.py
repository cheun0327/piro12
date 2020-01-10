import turtle
import random
import math

turtle.bgcolor('black')
turtle.setup( width = 650, height = 650, startx = None, starty = None)

class ball:
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.radius = args[2]
        self.color = args[3]
balls = []
me = ball(-300, -300, 10, 'white')
def distance(a,b):
    return math.sqrt(math.pow(a.x-b.x,2) + math.pow(a.y-b.y,2))
def inside(point):
    return -310 <= point.x < 310 and -310 <= point.y < 310
def random_draw():
    for i in range(20):
        turtle.speed(0)
        turtle.hideturtle()
        x=random.randint(-280, 300)
        y=random.randint(-280, 300)
        radius=random.randint(20,50)
        c=random.choice(['green', 'yellow', 'blue', 'pink', 'violet'])
        balls.append(ball(x,y,radius,c))
        turtle.up()
        turtle.goto(x,y)
        turtle.tracer(False)
        turtle.dot(radius, c)

def draw(alive):
    turtle.clear()
    for ball in balls:
        turtle.speed(0)
        turtle.tracer(False)
        turtle.up()
        turtle.goto(ball.x, ball.y)
        turtle.dot(ball.radius, ball.color)
    turtle.goto(me.x, me.y)
    if alive:
        turtle.dot(me.radius, me.color)
        turtle.goto(300, 300)
        turtle.color('white')
        turtle.write("goal", move=False, align="center", font=("Arial", 12, "bold"))
        if 290 <= me.x <= 310 and 290 <= me.y <= 310:
            turtle.clear()
            turtle.bgcolor("blue")
            turtle.goto(-70, 0)
            turtle.write("WIN!", font=("Arial", 40, "normal"))
            turtle.goto(-180, -55)
            turtle.write("If yo want to go to next stage,", font=("Arial", 20, "normal"))
            turtle.goto(-180, -110)
            turtle.write("Please click the gamescreen", font=("Arial", 20, "normal"))
            turtle.mainloop()
    else:
        turtle.dot(me.radius, 'red')
    turtle.update()

def moveball():
    countE = 0
    countO = 0
    while True:
        whitemove()
        for i in range(len(balls)):
            if i % 2 == 0:
                if countE < 4:
                    balls[i].x += 70
                    countE += 1
                elif 4 <= countE < 8:
                    balls[i].x -= 70
                    countE += 1
                else:
                    countE = 0
            else:
                if countO < 4:
                    balls[i].y -= 70
                    countO += 1
                elif 4 <= countE < 8:
                    balls[i].y += 70
                    countO += 1
                else:
                    countO = 0
            if abs(distance(me,balls[i]) < (me.radius+balls[i].radius)/2) or not inside(me):
                draw(False)
                return
            else:
                draw(True)
def up():
    me.y += 5
def down():
    me.y -= 5
def left():
    me.x -= 5
def right():
    me.x += 5
def whitemove():
    turtle.listen()
    turtle.onkey(up, "Up")
    turtle.onkeypress(up, "Up")
    turtle.onkey(down, "Down")
    turtle.onkeypress(down, "Down")
    turtle.onkey(left, "Left")
    turtle.onkeypress(left, "Left")
    turtle.onkey(right, "Right")
    turtle.onkeypress(right, "Right")

def gameover():
    turtle.clear()
    turtle.bgcolor("red")
    turtle.goto(-100, 0)
    turtle.write("You Lose", font=("Arial", 40, "bold"))
    turtle.goto(-55, -55)
    turtle.write("try again", font=("Arial", 20, "normal"))

def game():
    start = True
    restart = True
    while start and restart:
        turtle.clear()
        random_draw()
        moveball()
        gameover()
        s = input('다시시작하려면 re를 입력하세요: ')
        if s != 're':
            restart = False
            return print("gameover")
        else:
            me.x = -300
            me.y = -300
            turtle.bgcolor('black')
            continue

game()
turtle.mainloop()
