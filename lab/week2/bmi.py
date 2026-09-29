#
#bmi 계산기
#
def calculate_bmi(weight: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "저체중"
    elif bmi < 25:
        return "정상"
    elif bmi < 30:
        return "과체중"
    else:
        return "비만"

def tast_calculate_bmi() -> None:
    weight = float(input("체중(kg): "))
    height_cm = float(input("키(cm): "))
    bmi = calculate_bmi(weight, height_cm)
    print(f"체중: {weight}kg, 키: {height_cm}cm, BMI: {bmi:.2f}, 분류: {classify_bmi(bmi)}")

if __name__ == "__main__":
    tast_calculate_bmi()
