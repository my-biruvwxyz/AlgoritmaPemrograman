import math
import turtle as t

# fungsi parametris hati
def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return (12 * math.cos(k) 
            - 5 * math.cos(2*k) 
            - 2 * math.cos(3*k) 
            - math.cos(4*k))

# setup layar
t.speed(0)
t.bgcolor("black")
t.color("#f73487")

# mulai gambar
t.penup()

# loop menggambar
k = 0
while k < 2 * math.pi:
    x = hearta(k) * 20
    y = heartb(k) * 20
    t.goto(x, y)
    t.pendown()
    k += 0.01

t.done()