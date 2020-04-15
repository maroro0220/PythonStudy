import heapq
def solution(scoville, K):
    answer = 0
    heap=[]
    heapq.heapify(scoville)
    while scoville:
        top=heapq.heappop(scoville)
        if top>=K:
            break
        if len(scoville)<=1:
            return -1
        second=heapq.heappop(scoville)
        heapq.heappush(scoville,top+second*2)
        answer+=1

    return answer

print(solution([1, 2, 3, 9, 10, 12]	,7))