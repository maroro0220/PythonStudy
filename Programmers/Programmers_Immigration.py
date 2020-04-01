def solution(n, times):
    #answer = 0
    
    #left=min(times)*n
    left=0
    right=max(times)*n
    answer=right
    while(left<=right):
        mid=(left+right)//2
        sum=0
        for i in times:
            sum+=mid//i
        if sum>=n:
            if answer>mid:
                answer=mid
            right=mid-1
        elif sum<n:
            left=mid+1
        '''
        else:
            #if answer>=mid:
            answer=mid
            right=mid-1
            #break
        '''
    print(answer)
    return answer
#solution(6, [7,10]) #: 28
#solution(6, [6,10]) #: 24
#solution(6, [8,10]) #: 30
solution(6, [4,10]) #: 20
#solution(11, [3,4,10]) #: 18
#solution(5, [1,1,10]) #: 3