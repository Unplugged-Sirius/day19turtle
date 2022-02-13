from turtle import Turtle,Screen
import random
def posi(y):
    if(y==500):
        return y
    else:
        return
stg=Turtle()
spoo=Turtle()
pra=Turtle()
niya=Turtle()
akh=Turtle()
kumu=Turtle()
screen=Screen()
screen.setup(width=500, height= 400)
choice=screen.textinput("place ur bet","who is gona win")
spoo.penup()
spoo.sety(20)

pra.penup()
pra.sety(40)
niya.penup()
niya.sety(60)
akh.penup()
akh.sety(80)
kumu.penup()
kumu.sety(100)
stg.penup()
stg.sety(0)
for i in range (0,50):
    stg.speed(random.randint(2,10))
    spoo.speed(random.randint(2,10))
    pra.speed(random.randint(2,10))
    niya.speed(random.randint(2,10))
    akh.speed(random.randint(2,10))
    kumu.speed(random.randint(2,10))
    stg.fd(random.randint(2,10))
    print(stg.pos)
    if (stg.pos() == (500, 0)):
        print(stg.pos)
        print("stg won")

    kumu.fd(random.randint(2,10))
    if(kumu.pos()==(500,100)):
        print("kummu won")
    akh.fd(random.randint(2, 10))
    if (akh.pos() == (500, 80)):
        print("ahh won")

    niya.fd(random.randint(2,10))
    if (niya.pos() == (500, 60)):
        print("niya won")

    pra.fd(random.randint(2,10))
    if (kumu.pos() == (500, 40)):
        print("pra won")

    spoo.fd(random.randint(2,10))
    if (spoo.pos() == (500, 20)):
        print("spoo won")

screen.exitonclick()

