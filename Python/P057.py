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
    def __radd__(self,other):
        if isinstance(other,int):
            return Fraction(self.q * other + self.p,self.q)
        m = self.lcm(self.q,other.q)
        return Fraction(self.p * m // self.q + other.p * m // other.q,m)
    #
    #
    #
    def __mul__(self,other):
        if isinstance(other,int):
            return Fraction(other * self.p,self.q)
        return Fraction(self.p * other.p,self.q * other.q)
    #
    #
    #
    def __rmul__(self,other):
        if isinstance(other,int):
            return Fraction(other * self.p,self.q)
        return Fraction(self.p * other.p,self.q * other.q)    
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
    def __rtruediv__(self,other):
        if isinstance(other,int):
            return Fraction(other * self.q,self.p)
        return Fraction(self.q * other.p,self.p * other.q)


    def denominator(self):
        return f"{self.q}"

    def numerator(self):
        return f"{self.p}"


def NextFraction(n):
    return 1 + 1 / (1 + n)

n = Fraction(3,2)
sol = 0

for i in range(2, 1000):
    n = NextFraction(n)
    if len(str(n.numerator())) > len(str(n.denominator())):
        sol += 1

print(sol)


