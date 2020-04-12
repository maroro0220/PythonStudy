
def Prime(n):
    pri=[]
    chk=[0]*(n+1)
    for i in range(2,n+1):
        if chk[i]==0:
            pri.append(i)
        for j in range(i+i,n+1,i):
            chk[j]=1
    return pri
stret=[]
def DFS(arr,chk,idx, cnt, length,tmp):#num string, check array, now index, now cnt, target length
    if(length==cnt):
        #if(int(tmp) not in stret):
        stret.append(int(tmp))
        return
    for i in range(len(arr)):
        if chk[i]:
            continue
        chk[i]=1
        tmp+=arr[i]
        DFS(arr,chk,i,cnt+1,length,tmp)
        tmp=tmp[0:-1]
        chk[i]=0
    
def solution(numbers):
    answer = 0
    num=[]
    stret.clear()
    for i in range(1,len(numbers)+1):
        for j in range(len(numbers)):
            DFS(numbers,[0]*len(numbers),j,0,i,"")
    Pr=Prime(max(set(stret))+1)
    
    for s in set(stret):
        if s in Pr:
            answer+=1
    #print(answer)
    return answer
solution("17")
solution("011")