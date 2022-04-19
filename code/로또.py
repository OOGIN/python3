import numbers
import random


lotto_num = [] # 빈 로또 번호 들어갈 리스트
def lotto():
    number = random.randint(1,45)
    return number

count = 0 #횟수 저장 변수 
#무한반복
while True:
    if count >5 :#횟수가 6번 이상이면 break 를 건다
        break
    random_number = lotto() #로또 번호 뽑는곳
    if random_number not in lotto_num: #만약 로또 번호 안에 렌덤 넘버가 없으면 추가해라
        lotto_num .append(random_number)
        count +=1 

print(lotto_num)
#렌덤으로뽑는것까진 성공했지만 추가로 1등과 최하위를 뽑는건을 구상이 안됬습니다.
#이후 영상을 찾아보고 코드를 보고 다른사람들이 푼걸 봤습니다.