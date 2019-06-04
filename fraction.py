class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def sum(self, other):
        newdenominator = self.denominator * other.denominator
        newnumerator = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(newnumerator, newdenominator)
    def __str__(self):
        return str(self.numerator) + " / " + str(self.denominator)

def main():
        f1 = Fraction(2,3)
        f2 = Fraction(3,4)
        f3 = f1.sum(f2)
        print(f3)

if __name__ == '__main__':
    main()
