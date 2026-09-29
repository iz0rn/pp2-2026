#
# bmi 계산 함수
# Body Mass Index (BMI) 계산 함수
#

def get_bmi(weight_kg:float, height_m:float) -> float:
   bmi =weight_kg / (height_m ** 2)
   return bmi

def test_get_bmi():
    weight = 80.0
    height = 1.77
    B = get_bmi(weight, height)
    print(f"키{height} 몸무게{weight} BMI는 BMI:{B}입니다")

if __name__ == "__main__":
    test_get_bmi()
   

def func(x,y):
    return x+y

func(2,3)

funhc = lamda x 