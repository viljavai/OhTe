from collatz import Conjecture
from visualisazion import Plotting


def main():
#-------------------------------------------------------
    integer = int(input("Syötä arvo n: "))
    background = input("Taustaväri: (englanniksi)")
    if background == "":
        background = "black"
    color = input("Piirtoväri: (englanniksi)")
    if color == "":
        color = "white"
#-------------------------------------------------------
    collatz = Conjecture(integer)
    superlist = collatz.tree()
    plott = Plotting(color,background)
#-------------------------------------------------------
    plott.plot(superlist)
#-------------------------------------------------------
if __name__ == "__main__":
    main()
#-------------------------------------------------------
