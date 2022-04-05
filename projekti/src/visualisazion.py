from collatz import Conjecture
import turtle

class Initial:
    # Alustetaan turtle-ruutu
    def __init__(self,color):
        screen = turtle.Screen()
        screen.setup(1900,1000)
        screen.title("Collatz conjecture")
        screen.bgcolor(color)

class Plotting(turtle.Turtle):
    # Visualisaattorin asetukset

    def __init__(self,color,speed,bg):
        super().__init__(visible=False)
        self.getscreen()
        self.penup()
        self.goto(0,-450)
        self.pendown()
        self.color(color)
        self.pensize(2)
        self.speed(speed)
        self.showturtle()
        

    def plot(self,jono):
        m = len(jono)
        for i in range(m-1,0,-1):
            if jono[i] % 2 == 0 or jono[i] == 1:
                self.right(7)
                self.backward(12)
            else:
                self.left(8)
                self.backward(12)
