import turtle as flog
import math

wn = flog.Screen()
wn.setup(640,480)
wn.title("O'zbekiston bayrog'i || JASUR_0606")

def rectangle(color):
    flog.begin_fill()
    flog.fillcolor(color)
    for i in range(2):
        flog.forward(400)
        flog.rt(90)
        flog.fd(100)
        flog.rt(90)
    flog.end_fill()

flog.up()
flog.goto(0,-300)
flog.down()
flog.goto(0,300)
rectangle('blue')
flog.up()
flog.goto(400,200)
flog.down()
flog.rt(90)
flog.color("blue")
def rectangle(color):
    flog.begin_fill()
    flog.fillcolor(color)
    for i in range(2):
        flog.fd(10)
        flog.rt(90)
        flog.fd(400)
        flog.rt(90)
    flog.end_fill()
flog.color('red')
rectangle('red')
flog.fd(100)
flog.rt(90)
flog.fd(400)
flog.lt(90)
flog.color('black','red')
flog.begin_fill()
flog.fd(10)
flog.lt(90)
flog.fd(400)
flog.lt(90)
flog.fd(10)
flog.end_fill()
flog.rt(180)
flog.fd(10)
flog.color('green','green')
flog.begin_fill()
for i in range(2):
    flog.fd(100)
    flog.rt(90)
    flog.fd(400)
    flog.rt(90)
flog.end_fill()
for i in range(2):
    flog.fd(100)
    flog.rt(90)
    flog.fd(400)
    flog.rt(90)
flog.end_fill()
flog.up()
flog.lt(180)
flog.fd(200)
flog.lt(90)
flog.fd(370)
flog.down()


flog.color('blue','white')
flog.begin_fill()
for i in range(360):
    flog.fd(0.4)
    flog.lt(1)
flog.end_fill()
flog.lt(180)
flog.fd(10)
flog.rt(180)
flog.color('blue','blue')
flog.begin_fill()
for i in range(360):
    flog.fd(0.4)
    flog.lt(1)
flog.end_fill()
flog.color('black')
flog.lt(180)
flog.up()
flog.fd(50)
flog.rt(90)
flog.fd(10)
flog.lt(90)
flog.down()

flog.color('white','white')
flog.begin_fill()
for i in range(3):
    flog.lt(72)
    flog.fd(15)
    for i in range(4):
        flog.rt(144)
        flog.fd(15)
    flog.lt(144)
    flog.up()
    flog.fd(20)
    flog.down()
flog.end_fill()

flog.rt(90)
flog.up()
flog.fd(20)
flog.rt(90)
flog.fd(80)
flog.rt(180)
flog.color('white','white')
flog.begin_fill()

for i in range(4):
    flog.lt(72)
    flog.fd(15)
    for i in range(4):
        flog.rt(144)
        flog.fd(15)
    flog.lt(144)
    flog.up()
    flog.fd(20)
    flog.down()
flog.end_fill()

flog.rt(90)
flog.up()
flog.fd(20)
flog.rt(90)
flog.fd(100)
flog.rt(180)

flog.color('white','white')
flog.begin_fill()
for i in range(5):
    flog.lt(72)
    flog.fd(15)
    for i in range(4):
        flog.rt(144)
        flog.fd(15)
    flog.lt(144)
    flog.up()
    flog.fd(20)
    flog.down()
flog.end_fill()

flog.up()
flog.rt(180)
flog.fd(150)
flog.lt(90)
flog.fd(540)
# flog.color('red')
flog.down()
flog.color('black','black')
flog.begin_fill()
for i in range(2):
    for i in range(2):
        flog.rt(90)
        flog.fd(5)
        flog.rt(90)
        flog.fd(600)
flog.end_fill()



wn.mainloop()

