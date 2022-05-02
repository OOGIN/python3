def solution(N, stages):
    People = len(stages)
    faillist = []
    for i in range(1, N + 1):
        faillist.append(stages.count(i) / People)
        if stages.count(i) / People > 0:
            People -= stages.count(i)

    print(faillist)


A = 5
B = [2, 1, 2, 6, 2, 4, 3, 3]
solution(A, B)
