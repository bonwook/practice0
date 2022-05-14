import random
numbers = []
number = str(random.randint(0,9))

for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)
print(numbers)


while 1:
    strike = ball = 0
    userInput = str(input("3자리 숫자를 입력하세요."))
    for i in range(0,3):
        for j in range(0,3):
            if userInput[i] == numbers[j] and i==j:
                strike +=1
            elif userInput[i] == numbers[j] and i!=j:
                ball +=1
    if strike == 0 & ball == 0:
        print("3 out")
    elif strike ==3:
        print("맞추셨습니다.")
        break
    else:
        print("{} strike {} ball".format(strike,ball))
    
    
