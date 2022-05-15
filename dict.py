import random
engWord = { #순서의 개념이 없음.
    "사자":"lion",
    "호랑이": "tiger",
    "바나나":"banana",
    "쥐" : "mouse"
}
words = []

for i in engWord:
    words.append(i) #키를 담고
    random.shuffle(words) #섞음

chance = 3

for i in range(0,len(words)):
    ans = words[i] 
    for j in range(0,3):
        answer = str(input("{} 의 뜻을 적어 주세요: ".format(ans)))
        if answer.strip().lower() == engWord[ans].lower():
            print("정답입니다.")
            break
        else:
            print("{}번 실패하셨습니다. {}의 이름을 다시 적어주세요".format(j+1,ans))

    if engWord[ans].lower() != answer:
        print("정답은 {} 입니다.".format(ans))       
        
           

