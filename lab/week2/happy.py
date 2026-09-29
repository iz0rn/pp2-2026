def print_msg(name):
    print("안녕하세요?")
    print(name+"님의 생일을 축하드립니다.")

print_msg("김민재")
print_msg("윤완")
print_msg("임정아")
print_msg("송영준")

def test_happy_birthday():
    print_msg("김민재")
    print_msg("윤완")
    print_msg("임정아")
    print_msg("송영준")

if __name__ == "__main__":
    test_happy_birthday()

def test_happy_birthday2():
    test_happy_birthday2()
    names = ["김민재", "윤완", "임정아", "송영준"]
    for name in names:
        print_msg(name)

if __name__ == "__main__":
    test_happy_birthday2()

def test_happy_birthday3():
    test_happy_birthday3("3.141592")
    test_happy_birthday3(100)
    test_happy_birthday3([1, 2, 3])

if __name__ == "__main__":
    test_happy_birthday3()
    
