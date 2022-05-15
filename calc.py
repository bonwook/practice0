import os 

while True:
    os.system("cls")
    s = input("계산식 입력> ")
    print("결과: {}".format(eval(s))) #eval 함수는 사칙연산 우선순위에 따라 계산해줌 계산식을 input에 적으면됨 
    os.system("pause")                #ex)  5+5*10