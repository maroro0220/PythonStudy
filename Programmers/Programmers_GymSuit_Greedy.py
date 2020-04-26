def solution(n, lost, reserve):
    answer = 0
    chk=[1 for _ in range(0,n+1)]
    for i in reserve:
        chk[i]+=1
    for j in lost:
        chk[j]-=1
    for i in range(1,n+1):
        if(i>1 and chk[i-1]==0 and chk[i]==2):
            chk[i]-=1
            chk[i-1]+=1
        if(i<n and chk[i+1]==0 and chk[i]==2):
            chk[i]-=1
            chk[i+1]+=1

    for i in range(1,n+1):
        if chk[i]>0:
            answer+=1

    print(answer)
    return answer

solution(5,[2,4],[1,3,5])#5
solution(5,[2,4],[3])#4
solution(3,[3],[1])#2
solution(5,[1,2],[2,3])#4