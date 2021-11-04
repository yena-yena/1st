#7.7
import math as m
for i in range(1,301,30):  #for i in range(1,301):
    m.log(i)
    print('log',i,'= {}'.format(m.log(i)))
#    i=i+30 왜 안되는지??

#7.11
import turtle as t
#(1)
t.penup()
t.goto(-100,100)
t.pendown()
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.done()