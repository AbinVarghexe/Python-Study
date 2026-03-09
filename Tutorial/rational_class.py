class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        self._numerator = numerator
        self._denominator = denominator
        self._reduce()

    @staticmethod
    def _gcd(a, b):
        a = abs(a)
        b = abs(b)
        while b != 0:
            a, b = b, a % b
        return a if a != 0 else 1

    def _reduce(self):
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1

        gcd_value = self._gcd(self._numerator, self._denominator)
        self._numerator //= gcd_value
        self._denominator //= gcd_value

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        numerator = self._numerator * other._denominator + other._numerator * self._denominator
        denominator = self._denominator * other._denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        numerator = self._numerator * other._denominator - other._numerator * self._denominator
        denominator = self._denominator * other._denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        numerator = self._numerator * other._numerator
        denominator = self._denominator * other._denominator
        return Rational(numerator, denominator)

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return (
            self._numerator == other._numerator
            and self._denominator == other._denominator
        )

    def __lt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator * other._denominator > other._numerator * self._denominator


def main():
    r1 = Rational(2, 4)
    r2 = Rational(3, 5)

    print("r1 =", r1)
    print("r2 =", r2)
    print("r1 + r2 =", r1 + r2)
    print("r1 - r2 =", r1 - r2)
    print("r1 * r2 =", r1 * r2)
    print("r1 == r2:", r1 == r2)
    print("r1 < r2:", r1 < r2)
    print("r1 > r2:", r1 > r2)


if __name__ == "__main__":
    main()
