import turtle

s = turtle.Screen()

t = turtle.Turtle()

# for _ in range(3):
#     t.fd(90)
#     t.rt(90)
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        t.fd(100)
        t.rt(angle)
        
for shape_side_n in range(3,11):
    draw_shape(shape_side_n)        


s.mainloop()
