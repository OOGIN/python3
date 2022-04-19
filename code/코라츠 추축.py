def solution(num):
    cnt = 0
    
    while True:
        if num == 1:
            break
        if cnt == 500:
            break
        if num %2 == 0:
            num //= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1
            
    return cnt if cnt != 500 else -1

#https://velog.io/@cosmos/Programmers%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%9C%EB%9D%BC%EC%B8%A0-%EC%B6%94%EC%B8%A1-python