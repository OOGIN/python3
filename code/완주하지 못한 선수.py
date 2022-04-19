import collections

def solution(participant, completion):
    #participant 와 completion 를 Counter 로 갯수를 구하고 그 둘의 차를 구한다
    #둘의 차를 구하여 정답만 남아있는 Counter 변환
    answer = collections.Counter(participant) - collections.Counter(completion)
    #예시()
    #counter의 key값을 반환한다
    #return list(answer.keys())[0]
    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]));