#사칙연산 우선순위와 관계없이 순차적으로 계산하는 calculator
# string 형식으로 만들고 5 + 5 * 5 operator를 기준으로 나누어 리스트에 저장 후 순차적 계산 실행
import os
oper = ["+", "-", "*", "/", "="]
def usrCal(usrInput, showHistory=False):
    strList = []
    endPos =0

    if usrInput[-1] not in oper: # operator 기준으로 값을 저장할때 마지막 operator 뒤의 숫자는 저장이 안되고 
        usrInput += "="                             # for문이 끝나버리기 때문에  등호를 붙여 처리를 해준다.



    for index, s in enumerate(usrInput):
    # enumerate() 함수는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게 해주는 반복자(iterator)
        if s in oper:
            if usrInput[endPos:index].strip() !="":
                strList.append(usrInput[endPos:index])
                strList.append(s)
                endPos = index+1
    strList = strList[:-1] # 아까 추가한 =을 빼주기 위해서 처음부터 맨 마지막 글자전까지 저장

    #리스트에서 3개씩 묶어서 계산후 리스트에 덮어쓰는 방식으로 사용
    pos = 0
    while True:
        if len(strList)==1:
            break
        if len(strList) > pos+1 and strList[pos] in oper:
            tmp = strList[pos-1] + strList[pos] + strList[pos+1]
            del strList[0:3] # 리스트 앞쪽 3개의 값을 지우고 tmp로 덮어쓰는 과정
            strList.insert(0, str(eval(tmp))) # str 형으로 값을 만들고 계산은 귀찮으니까 eval함수를 사용 후 대입
            pos = 0
            if showHistory==True:
                print(strList)
        pos+=1

    if len(strList) >0:
        result = float(strList[0])

    return round(result,4)

while True: 
    os.system("cls")
    usrInput = input("계산식을 적어주세요. q를 누르면 종료됩니다.")
    if usrInput.lower() == 'q':
        break
    print("결과는 : {}".format(usrCal(usrInput,showHistory=True)))
    os.system("pause")





