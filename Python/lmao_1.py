import turtle
# draw no draw
# restrict to 50 times

s = turtle.getscreen()
t = turtle.Turtle()

# t.fd(90)
# t.up()
# t.fd(90)
# t.down()
# t.fd(90)

for i in range (50):
    t.fd(5)
    t.up()
    t.fd(5)
    t.down()
    
     

s.mainloop()



