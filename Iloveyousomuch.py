
import turtle as t
import random

def makeHeart(size):
    t.forward(size)
    t.circle(size/2, 180)
    t.right(90)
    t.circle(size/2, 180)
    t.forward(size)
    t.left(90)

def ILoveMyGirlfriend(size, length, depth):

    if depth == 0:
        return
    ILoveMyGirlfriend(size*1.5, length, depth-1)
    counter = 360
    while counter > 0:
        heartColor = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        t.color(heartColor)
        t.fillcolor(heartColor)
        t.begin_fill()
        makeHeart(size)
        t.end_fill()
        t.left(45)
        counter = counter -45

def main():
    t.speed(0)
    t.colormode(255)

    ILoveMyGirlfriend(20,0,8)
    t.back(100)
    t.color("black")
    t.write("I love you", move=False, align="left", font=("Courier New", 24, "bold"))
    t.done()

main()