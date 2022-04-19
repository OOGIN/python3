def solution(a, d):
    answer = []
    #for문을 돌면서 a(array)의 요소들이 d(divisor)로 나누어 떨어지면 answer 리스트에 append 로 추가
    for i in range(len(a)) :
        if a[i] % d == 0 :
            answer.append(a[i])
    #for문에서 나온 후 answer가 비어있으면 -1을 그렇지 않으면 answer를 정렬해서 반환
    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
    return answer


#문제 설명: a(array)의 각 요소(element) 중 d(divisor)로 나누어 떨어지는 값을 오름차순으로 
# 정렬한 배열을 반환하는 함수, solution을 작성해주세요. 
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.