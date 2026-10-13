# 작성자: 김민재
# 작성일: 2026.10.13

class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)


class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)


class Contact(Address, Person):
    def __init__(self, street, city, name, email, phone):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)
        self.phone = str(phone)

    def show(self):
        print("이름:", self.name)
        print("이메일:", self.email)
        print("주소:", self.street, self.city)
        print("전화번호:", self.phone)


c = Contact("중앙로", "청주", "홍길동", "hong@example.com", "010-1234-5678")
c.show()