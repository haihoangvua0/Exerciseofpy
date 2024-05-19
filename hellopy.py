import turtle
t = turtle.Turtle()
t.pu()
t.goto(-90, 90)
t.pd()
def hinh_chu_nhat(v):
    for i in range(2):
        t.fd(v)
        t.rt(90)
        t.fd(v+50)
        t.rt(90)

def hinh_chu_nhat_2(v):
    for i in range(2):
        t.fd(v+50)
        t.lt(90)
        t.fd(v)
        t.left(90)

hinh_chu_nhat(100)
t.fd(100)
hinh_chu_nhat(100)
t.backward(100)
t.rt(90)
t.fd(150)
hinh_chu_nhat_2(100)
t.lt(90)
t.fd(100)
t.rt(90)
hinh_chu_nhat_2(100)
t.fd(100+50)
t.lt(90)
t.fd(100)
for i in range(2):
    t.fd(100)
    t.left(90)
    t.fd(150)
    t.left(90)
turtle.done()