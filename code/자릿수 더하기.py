def solution(n):
    n=[int(i) for i in str(n)]
    return sum(n)
    #숫자 n을 문자열로 바꾸고 한 자리씩 int로 리스트에 저장함. 저장된 값을 sum(n) 으로 n 안에 다 더한값을 저장
