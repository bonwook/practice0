import random
import os

chance = 10
random = random.randint(1,99)
os.system("cls")
def input_check(msg,casting=int):
    while 1:
        try:
            userInput =casting(input(msg))
            return userInput
        except:
            print("숫자를 입력하세요")
            continue


while chance:
    chance -=1
    userInput =input_check("0부터99까지의 숫자를 입력하세요")
    if(random == userInput):
        break
    elif random > userInput:
        print("{}보다 큰 숫자입니다.".format(userInput))
    else:
        print("{}보다 작은 숫자입니다.".format(userInput))
   

if random == userInput:
    print("정답입니다. {}번째 만에 맞추셨습니다.".format(10-chance))
else:
    print("틀렸습니다. 정답은 {} 입니다.".format(random))
