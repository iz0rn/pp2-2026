# 작성자: 김민재
# 작성일: 2026.10.13

import math


class Function:
    def value(self, x):
        pass


class Quadratic(Function):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def get_roots(self):
        d = self.b ** 2 - 4 * self.a * self.c

        if d < 0:
            return None

        x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
        x2 = (-self.b - math.sqrt(d)) / (2 * self.a)

        return x1, x2


q = Quadratic(1, -3, 2)

print(q.value(2))
print(q.get_roots())