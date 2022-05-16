import time
import random
import os

WORD_LIST = [
    "삶이 있는 한 희망은 있다.",
    "산다는것 그것은 치열한 전투이다.",
    "하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다.",
    "언제나 현재에 집중할수 있다면 행복할것이다.",
    "진정으로 웃으려면 고통을 참아야하며 , 나아가 고통을 즐길 줄 알아야 해",
    "직업에서 행복을 찾아라. 아니면 행복이 무엇인지 절대 모를 것이다.",
    "신은 용기있는자를 결코 버리지 않는다.",
    "피할수 없으면 즐겨라"
]
for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    usrInput = str(input(q+'\n')).strip() #input안에 따라쳐야 할 값, str로 캐스팅, 공백 제거까지
    end_time = time.time()-start_time

    if usrInput == "/exit":
        break

    correct = 0
    for index, a in enumerate(usrInput): # enumerate로 index값도 출력
        if index>=len(q): #문제의 문자열보다 길어질 경우 나오기 위함
            break 
        if a == q[index]:
            correct +=1
    
    totLen = len(q)
    cor = correct / totLen * 100
    err = (totLen - correct)/totLen * 100
    speed = (correct / end_time) * 60

    print("속도 : {:0.2f}타 정확도: {:0.2f}% 오타 {:0.2f}".format(speed,cor, err))
    os.system("pause")

    
