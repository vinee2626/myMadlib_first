import turtle
import random


def heart():
    count = 0
    turtle.left(45)
    turtle.forward(130)
    while(count < 200):
        turtle.left(1)
        turtle.forward(1)
        count += 1
    turtle.right(130)
    count = 0
    while(count < 200):
        turtle.left(1)
        turtle.forward(1)
        count += 1

    turtle.forward(130)


a = ["loves", "No love"]
love = random.choice(a)
if love == a[0]:
    print("I loves Watermelon")
    print(heart())
else:
    print("I don't love watermelon")
