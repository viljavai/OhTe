from visualisazion import Plotting

class Conjecture:

    def __init__(self, integer, master, canvas, angle, numvar):
        """Sovelluslogiikan laskennallinen ydin

        Args:
            integer (int): käyttäjäsyöte
            master: tkinter-olio
            canvas: tkinter canvas
            angle: käyttäjäsyöte
            numvar: Boolean
        """
        self.integer = integer
        self.angle = angle
        self.numvar = numvar
        self.superlist = []
        self.jono = []
        self.master = master
        self.canvas = canvas

    def oper(self):
        """yksittäiselle lukujonon luvulle tehtävä operaatio

        Returns:
            self.integer: seuraava luku lukujonossa
        """
        if self.integer % 2 == 0:
            self.integer = self.integer // 2
            return self.integer

        self.integer = self.integer * 3 + 1
        return self.integer

    def traverse(self):
        """Luodaan yksittäinen lukujono

        Returns:
            self.jono: lukujono
        """
        self.jono = [self.integer]
        while self.integer != 1:
            self.oper()
            self.jono.append(self.integer)
        self.superlist.append(self.jono)
        return self.jono

    def tree(self):
        """Luodaan lista lukujonoja välillä (integer,..1)

        Returns:
            self.superlist: lista lukujonoja
        """
        for self.integer in range(self.integer,1,-1):
            self.traverse()
        print(self.superlist[0])
        plot_instance = Plotting(self.master, self.canvas)
        plot_instance.plot(self.superlist, self.angle, self.numvar)
        return self.superlist
