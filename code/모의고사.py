def solution(answers):
    A=[1,2,3,4,5]
    B=[2, 1, 2, 3, 2, 4, 2, 5]
    C=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score =[0,0,0]
    result =[]

    for i,j in enumerate(answers):
        if j == A[i%len(A)]:
            score[0]+=1
        if j == B[i%len(B)]:
            score[1]+=1
        if j == C[i%len(C)]:
            score[2]+=1

    for j,s in enumerate(score):
        if s == max(score):
            result.append(j+1)

    return result