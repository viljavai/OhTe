class Conjecture:
    #Määritellään collatzin konjektuuri

    def __init__(self,integer):
        self.integer = integer
        self.superlist = []

    # Operaatiot yksittäiselle luvulle
    def oper(self):
        if self.integer % 2 == 0:
            self.integer = self.integer // 2
            return self.integer
        if self.integer % 2 != 0:
            self.integer = self.integer * 3 + 1
            return self.integer

    # Generoidaan lukujono
    def traverse(self):
        self.jono = [self.integer]
        while self.integer != 1:
            self.oper()
            self.jono.append(self.integer)
        self.superlist.append(self.jono)
        return self.jono
 
    # Luodaan kaikki lukujonot luvuille (n,..,1)
    def tree(self):
        for self.integer in range(self.integer,1,-1):
            self.traverse()
        print(self.superlist[0])
        return self.superlist
