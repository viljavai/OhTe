from collatz import Conjecture
from visualisazion import Initial, Plotting

def main():
    n = int(input("Syötä arvo n: "))
    collatz = Conjecture(n)
    lista = collatz.traverse()
    bg = input("Taustaväri: (englanniksi)")
    color = input("Piirtoväri: (englanniksi)")
    speed = int(input("Piirtonopeus: (10 on hyvä) "))
    init = Initial(bg)
    plott = Plotting(color,speed,bg)
    plott.plot(lista)

if __name__ == "__main__":
    main()