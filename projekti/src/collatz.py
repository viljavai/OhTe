from visualisazion import Plotting

class Conjecture:

    def __init__(self, integer, master):
        self.integer = integer
        self.superlist = []
        self.master = master

    def oper(self, integer):
        if self.integer % 2 == 0:
            self.integer = self.integer // 2
            return self.integer
        if self.integer % 2 != 0:
            self.integer = self.integer * 3 + 1
            return self.integer

    def traverse(self, integer):
        self.jono = [self.integer]
        while self.integer != 1:
            self.oper(self.integer)
            self.jono.append(self.integer)
        self.superlist.append(self.jono)
        return self.jono

    """ Luodaan kaikki lukujonot luvuille (integer,..,1)
    """
    def tree(self, integer, master):
        for self.integer in range(self.integer,1,-1):
            self.traverse(self.integer)
        print(self.superlist[0])
        plot_instance = Plotting(self.master)
        plot_instance.plot(self.superlist)
        return self.superlist
