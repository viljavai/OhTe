import turtle
from datetime import datetime
import os
import tkinter as tk
from collatz import Conjecture

class Plotting:
    # Visualisaattorin asetukset

    def __init__(self,master,color,background):
        # tkinter alustus
        self.master = master
        self.color = color
    
        self.master.title("Collatz conjecture")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=1500, height=1000)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor(background)
        
        self.savebutton = tk.Button(self.master, text="Save graph", command=self.save_image)
        self.savebutton.config(bg="black",fg="white")
        self.savebutton.pack()

        self.integerfield = tk.Entry(self.master)
        self.canvas.create_window(200,140,window=self.integerfield)
        self.integerfield.pack()

        self.integerbutton = tk.Button(text="Create graph", command=Conjecture)
        self.integerbutton.config(bg="black",fg="white")
        self.integerbutton.pack()

        self.t = turtle.RawTurtle(self.screen)
        self.t.color(color)
    
    def press(self):
        pass
 
    def plot(self,superlist):
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(-600,-480)
        self.t.pendown()
        self.t.pensize(1)
        self.t.color(self.color)
        self.t.speed(0)
        self.screen.tracer(0,0)
        for jono in superlist:
            self.t.penup()
            self.t.goto(-500,-480)
            self.t.setheading(90)
            self.t.pendown()
            for i in range(len(jono)-2,0,-1):
                if jono[i] % 2 == 0:
                    # 10
                    self.t.right(int(10))
                    self.t.forward(8)
                else:
                    # 18
                    self.t.left(int(18))
                    self.t.forward(8)
        self.screen.update() 
        turtle.done()
        
    def save_image(self):
        # Kuvana tallennus
        date = (datetime.now()).strftime("%m.%d.%Y-%H:%M:%S")
        filename = os.environ["HOME"] + "/my_collatz-" + date
        print(filename)
        img = self.t.getscreen() 
        img.getcanvas().postscript(file=filename, width=1920, height=1080)
        self.t.write("Image saved to home directory!", "right", font=("Verdana", 15, "normal"))
        return filename