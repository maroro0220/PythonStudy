'''
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정합니다.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정합니다. 
   상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정합니다. 
'''
def solution(budgets, M):
    answer = 0
    #left=min(budgets)
    left=0
    right=max(budgets)
    while(left<=right):
        mid=(left+right)//2
        sum=0
        for i in budgets:
            if i>mid: sum+=mid
            else: sum+=i
        if sum>M:
            right=mid-1
        elif sum<M:
            if answer<mid: answer=mid
            left=mid+1
        else : 
            answer=mid
            break

    print(answer)
    return answer

solution([120,110,140,150],485)
solution([120,120,120,120],480)