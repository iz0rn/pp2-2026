# 작성자: 김민재
# 작성일: 2026.10.13

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


def get_oldest_cat(*args):
    return max(args, key=lambda cat: cat.age)


cat1 = Cat("나비", 3, "코리안숏헤어")
cat2 = Cat("모모", 7, "페르시안")
cat3 = Cat("루루", 5, "러시안블루")

oldest = get_oldest_cat(cat1, cat2, cat3)

print(f"가장 나이가 많은 고양이는 {oldest.age}살입니다.")