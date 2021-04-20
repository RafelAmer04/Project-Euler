class Fraction:
    def __init__(self,p,q):
        m = self.gcd(p,q)
        self.p = p // m
        self.q = q // m
    #
    #
    #
    def gcd(self,a,b):
        if b == 0:
            return 0
        while b != 0:
            a, b = b, a % b
        return a
    #
    #
    #
    def lcm(self,a,b):
        return a * b // self.gcd(a,b)
    #
    #
    #
    def __str__(self):
        if self.q == 1:
            return f"{self.p}"
        return f"{self.p}/{self.q}"
    #
    #
    #
    def __add__(self,other):
        m = self.lcm(self.q,other.q)
        return Fraction(self.p * m // self.q + other.p * m // other.q,m)
    #
    #
    #
    def __truediv__(self,other):
        if isinstance(other,int):
            return Fraction(self.p,self.q * other)
        return Fraction(self.p * other.q,self.q * other.p)
    #
    #
    #
    def invert(self):
        return Fraction(self.q,self.p)

    def denominator(self):
        return f"{self.q}"

    def numerator(self):
        return f"{self.p}"


def NextFraction(n):
    one = Fraction(1,1)
    return one + (one + n).invert()

n = Fraction(3,2)
sol = 0

for i in range(2, 1000):
    n = NextFraction(n)
    if len(str(n.numerator())) > len(str(n.denominator())):
        sol += 1

print(sol)


