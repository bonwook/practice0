#unicode AC00 - 
#한글 = ((초성 *21) + 중성) * 28 + 종성 + 44032
# if "가" = (((0*21) + 0) *28 + 0 +44032 
# 초성 = ((x-44032) / 28 / 21)
# 중성 (x-44032) / 28 %21
# 종성 (x-44032) % 28 

import time
import random
import os

first = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
second = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
third = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]

def kor_function(string):
    word_list = list(string)
    new_list = []
    for k in word_list:
        if ord(k) >= ord("가") and ord(k)<= ord("힣"):
            char_index = ord(k)- ord("가") #유니코드상 몇번째 글자인지 인덱스 구함
            f = int((char_index/28)/21)
            new_list.append(first[f])
            s = int(char_index/28%21)
            new_list.append(second[s])
            t = int(char_index%28)

            if t >0:
                new_list.append(third[t])
        else:
            new_list.append(k)
    return new_list





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
    
    src = kor_function(q) #문제
    tar = kor_function(usrInput) #사용자 입력

    if usrInput == "/exit":
        break

    correct = 0
    for index, a in enumerate(tar): # enumerate로 index값도 출력
        if index>=len(src): #문제의 문자열보다 길어질 경우 나오기 위함
            break 
        if a == src[index]:
            correct +=1
    
    totLen = len(src)
    cor = correct / totLen * 100
    err = (totLen - correct)/totLen * 100
    speed = (correct / end_time) * 60

    print("속도 : {:0.2f}타 정확도: {:0.2f}% 오타 {:0.2f}".format(speed,cor, err))
    os.system("pause")

    
