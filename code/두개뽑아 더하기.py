def solution(numbers):
    answer = []
    #numb..안에 숫자를 
    for i in range(len(numbers)):
        #num...안에서 i 보다 하나 앞쪽 숫자를 뽑는다
        for j in range(i+1,len(numbers)):
            #i 와 j 를 더하고 그 값을 answer 로 저장
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()            
    return answer
print(solution([2,1,3,4,1]))