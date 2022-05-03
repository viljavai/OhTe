from visualisazion import Plotting

class Conjecture:

    def __init__(self, integer, master):
        """Sovelluslogiikan laskennallinen ydin

        Args:
            integer (int): käyttäjäsyöte
            master: tkinter-olio
        """
        self.integer = integer
        self.superlist = []
        self.master = master

    def oper(self, integer):
        """yksittäiselle lukujonon luvulle tehtävä operaatio

        Args:
            integer (int): luku lukujonossa

        Returns:
            self.integer: seuraava luku lukujonossa
        """
        if self.integer % 2 == 0:
            self.integer = self.integer // 2
            return self.integer
        if self.integer % 2 != 0:
            self.integer = self.integer * 3 + 1
            return self.integer

    def traverse(self, integer):
        """Luodaan yksittäinen lukujono

        Args:
            integer (int): käyttäjäsyöte

        Returns:
            self.jono: lukujono
        """
        self.jono = [self.integer]
        while self.integer != 1:
            self.oper(self.integer)
            self.jono.append(self.integer)
        self.superlist.append(self.jono)
        return self.jono

    def tree(self, integer, master):
        """Luodaan lista lukujonoja välillä (integer,..1)

        Args:
            integer (int): käyttäjäsyöte 
            master: tkinter olio

        Returns:
            self.superlist: lista lukujonoja
        """
        for self.integer in range(self.integer,1,-1):
            self.traverse(self.integer)
        print(self.superlist[0])
        plot_instance = Plotting(self.master)
        plot_instance.plot(self.superlist)
        return self.superlist
