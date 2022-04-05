class Conjecture:
    #Määritellään collatzin konjektuuri

    def __init__(self,n):
        self.n = n
        self.jono = [n]

    def oper(self):
        if self.n % 2 == 0:
            self.n = self.n // 2
            return self.n
        else:
            self.n = self.n * 3 + 1
            return self.n
    
    def traverse(self):
        while self.n != 1:
            self.oper()
            self.jono.append(self.n)
        print(self.jono)
        return self.jono
    
