import random



number = random.randint(1,45)

usrInput = int(input("로또 몇개를 만들까요?"))

for j in range(usrInput):
    lotto = []
    for i in range(6):
        while len(lotto) !=6:
            if number not in lotto:
                lotto.append(number)
            else:
                number = random.randint(1,45)
    lotto.sort()
    print("{} 로또 번호는 : {}".format(j+1,lotto))
