class Conjecture:
    #Määritellään collatzin konjektuuri

    def __init__(self,n):
        self.n = n

    def traverse(self):
        res = [self.n]
        while self.n != 1:
            if self.n % 2 == 0:
                self.n = self.n // 2
            else:
                self.n = self.n * 3 + 1
            
            res.append(self.n)
        return res


def main():
    n = int(input("Syötä arvo n: "))
    collatz = Conjecture(n)
    nums = collatz.traverse()
    print(nums)

if __name__ == "__main__":
    main()