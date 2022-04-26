from collatz import Conjecture
from visualisazion import Plotting
import tkinter as tk

def main():
#-------------------------------------------------------
    integer = int(input("Syötä arvo n: "))
    background = input("Taustaväri: (englanniksi)")
    if background == "":
        background = "white"
    color = input("Piirtoväri: (englanniksi)")
    if color == "":
        color = "black"
#-------------------------------------------------------
    collatz = Conjecture(integer)
    superlist = collatz.tree()
    root = tk.Tk()
    plott = Plotting(root,color,background)
#-------------------------------------------------------
    plott.plot(superlist)
#-------------------------------------------------------
if __name__ == "__main__":
    main()
#-------------------------------------------------------
