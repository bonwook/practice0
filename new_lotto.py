'''
1. 특정 숫자 포함하여 로또 번호 생성하는 기능
2. 특정 숫자를 제외하여 생성
3. 정해진 자릿수 만큼 연속 숫자를 포함하는 번호 
'''
# *args 인자를 몇개 받아야할지 모를 때 튜플형태로 저장
# **kwargs 딕셔너리 형태로 저장, 파라미터명을 같이 보낼 수 있음
import numpy as np

def makeLottoNumber(**kwargs): #키워드형 arguments 사용자가 옵션을 줄수도 안줄수도 있음.
    randNum = np.random.choice(range(1,45),6,replace=False) #중복제거 리스트 형태로 담김
    randNum.sort()

    lotto = [] #최종 로또 번호
    if kwargs.get("include"): #include 옵션이 있는경우
        include = kwargs.get("include")
        lotto.extend(include) #리스트안에 리스트가 들어가지 않고 숫자만 확장되는 extend
        cnt_make = 6 - len(lotto)
        for _ in range(cnt_make):
            for j in randNum:
                if lotto.count(j)==0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(randNum)  



    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude)) #집합으로 중복허용x, 차집합까지
        
        while len(lotto) !=6:
            for _ in range(6-len(lotto)):
                randNum = np.random.choice(range(1,45),6,replace=False)
                randNum.sort()

                for j in randNum:
                    if lotto.count(j) ==0 and j not in exclude:
                        lotto.append(j)
                        break
                

    #로또 리스트에 6개가 담겨있을거임.
    if kwargs.get("con"):
        con = kwargs.get("con")
        startNum = np.random.choice(lotto,1) #로또 리스트에 있는 값 하나를 사용
        #배열 출력
        
        seqNum = []
        for i in range(startNum[0], startNum[0]+con):
            seqNum.append(i)
            seqNum.sort()
            cnt_make = 6 - len(seqNum)
            lotto.clear()
            lotto.extend(seqNum)

            while len(lotto) !=6:
                for _ in range( 6-len(lotto)):
                    randNum = np.random.choice(range(1,45),6,replace=False) #중복제거 리스트 형태로 담김
                    randNum.sort()

                    for j in randNum:
                        if lotto.count(j) == 0 and j not in seqNum:
                            lotto.append(j)
                            break
                            
                    lotto = list(set(lotto))


    lotto.sort()
    return lotto    

count = int(input("로또 번호를 몇개 생성할까요"))
for j in range(count):
    print(makeLottoNumber())

