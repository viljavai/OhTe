from turtle import Screen, Turtle
import turtle
#from datetime import datetime
#from PIL import Image

class Plotting(Turtle):
    # Visualisaattorin asetukset

    def __init__(self,color,background):
        super().__init__(visible=False)
        self.hideturtle()
        screen = Screen()
        screen.setup(2560,1440)
        screen.title("Collatz conjecture")
        screen.bgcolor(background)
        self.penup()
        self.goto(-600,-480)
        self.pendown()
        self.getscreen()
        self.pensize(2)
        self.color(color)
        self.speed(0)

    def plot(self,superlist):
        turtle.tracer(0,0)
        for jono in superlist:
            #colors = ["red","orange","yellow","green","cyan",
            #"blue","blueviolet","crimson","pink","darkgreen","hotpink",
            #"indogo","lawngreen","midnightblue","salmon"]
            self.penup()
            self.goto(-500,-480)
            self.setheading(90)
            self.pendown()
            for i in range(len(jono)-2,0,-1):
                if jono[i] % 2 == 0:
                    self.right(10)
                    self.forward(10)
                else:
                    self.left(18)
                    self.forward(10)
        turtle.update()

        # Kuvana tallennus
        #date = (datetime.now()).strftime("%m/%d/%Y,%H:%M:%S")
        #filename = "my_collatz" + date
        #canvas = self.screen.getcanvas()
        #canvas.postscript(file= filename+".eps",width=2560,height=1440)
        #img = Image.open(filename+".eps")
        #img.save(filename+".jpg")
        #print("saved!")

        turtle.exitonclick()
    