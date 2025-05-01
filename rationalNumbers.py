class Rational (object):
    """A class for rational numbers that takes a numerator and denominator. Will throw an AttributeError is the object given is not a valid rational number"""

    def __init__(self, numerator, denominator=1):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self._reduce()  # _ at start to make it private to this class

    def _reduce(self):
        # Find the GCD of two numbers, then divide both numbers by that.
        x, y = self.numerator, self.denominator
        while y != 0:
            x, y = y, x % y
        # x is the GCD
        self.numerator //= x
        self.denominator //= x

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __float__(self):
        return float(self.numerator / self.denominator)

    def __add__(self, other):
        newNumerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)

    def __mul__(self, other):
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)


x, y = Rational(3, 5), Rational(7, 11)

print(x*y)
