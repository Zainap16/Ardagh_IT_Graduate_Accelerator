import tkinter as tk
# class
class Square():
    def get_x(self):
        print('x1: '+ str(self.x1))
        print('x2: '+ str(self.x2))
    
    def get_y(self):
        print('y1: '+ str(self.y1))
        print('y2: '+ str(self.y2))
    
# object
s1 = Square()
s1.x1 = 105 
s1.x2 = 180

s1.y1 = 150
s1.y2 = 250

s1.get_x()
s1.get_y()

 
# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(window, bg = "blue")
canvas.pack()

            # left,top,right,bottom
            # (x1,y1,x2,y2)
canvas.create_rectangle((s1.x1,s1.y1,s1.x2,s1.y2), fill = 'black')

# run
window.mainloop()

        
        
