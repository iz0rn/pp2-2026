#문제

#여러 학생들의 키와 몸무게를 리스트로 입력받아 bmi 리스트를 출력하는
#함수와 테스트하는 함수를 작성하시오
#bmi 함수는 지난 시간에 작성한 get_bmi() 함수를 이용하여 작성하세요
# 이름 키 몸무게

def get_bmi(weight: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def bmi(heights: list[float], weights: list[float]) -> list[float]:
    return [get_bmi(weight, height) for height, weight in zip(heights, weights)]


def test_bmi() -> None:
    heights = [175, 160]
    weights = [70, 50]
    result = bmi(heights, weights)
    expected = [get_bmi(70, 175), get_bmi(50, 160)]
    assert result == expected
    print("bmi 함수 테스트 통과")


if __name__ == "__main__":
    n = int(input("학생 수를 입력하세요: "))
    names = []
    heights = []
    weights = []

    for _ in range(n):
        names.append(input("이름을 입력하세요: "))
        heights.append(float(input("키를 입력하세요 (cm): ")))
        weights.append(float(input("몸무게를 입력하세요 (kg): ")))

    bmi_values = bmi(heights, weights)
    for name, bmi_value in zip(names, bmi_values):
        print(f"{name}의 BMI는 {bmi_value:.2f}입니다.")

    test_bmi()
