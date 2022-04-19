from multiprocessing.connection import answer_challenge


def solution(n,lost,reserve):
    #1.set 을 만든다
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    #2. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다
    for reserve in reserve_only:
        front = reserve - 1 
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    return n-len(lost_only)