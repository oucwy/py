import turtle as t
t.color("red")
for i in range(270):
    t.forward(3*i) # move forward by i steps
    # t.left(60) # rotate 60 degrees, 六边形
    t.left(110) # rotate 59 degrees, 五边形
t.done()