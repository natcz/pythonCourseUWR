from turtle import *

tracer(1, 0)
BOK = 10


def trojkat(bok):
    for i in range(3):
        fd(bok)
        rt(120)


def piramida(bok, n):
    if (n == 1):
        trojkat(bok)
        return
    else:
        piramida(bok / 2, n - 1)
        pu()
        fd(bok / 2)
        rt(90)
        fd(bok / 4)
        lt(90)
        pd()
        piramida(bok / 2, n - 1)
        pu()
        bk(bok / 2)
        rt(90)
        fd(bok / 4)
        lt(90)
        pd()
        piramida(bok / 2, n - 1)
        pu()
        lt(90)
        fd(bok / 2)
        rt(90)
        pd()


lt(90)
piramida(300, 7)
input()
