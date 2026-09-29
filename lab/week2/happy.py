#
# 생일 축하 함수
#

def print_message(name:str) -> None:
    print(f"안녕하세요, {name}님!")
    print( f"{name}님, 생일 축하합니다!")
    return None

def test_print_message() -> None:
    print_message("윤완")
    print_message("임정아")
    print_message("송영준")

def test_print_message2() -> None:
    names = ["윤완", "임정아", "송영준"]
    for name in names:
        print_message(name)

def test_print_message3() -> None:
    print_message(int(1000))
    print_message(float(2.134))
    print_message([1, 2, 3])

if __name__ == "__main__":
    #test_print_message()
    #test_print_message2()
    test_print_message3()
    
