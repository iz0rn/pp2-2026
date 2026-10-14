# 작성자: 김민재
# 작성일: 2026.10.13

import random


class Dice:
    def roll(self):
        return random.randint(1, 6)


class FraudDice(Dice):
    def roll(self):
        number = super().roll()

        while number < 3:
            number = super().roll()

        return number


d = Dice()
f = FraudDice()

print("일반 주사위:", d.roll())
print("가짜 주사위:", f.roll())