def solution(priorities, location):
    answer = 0
    lis=[]
    for i in range(len(priorities)):
        lis.append([priorities[i],i])
    printq=[]
    while lis:
        max_p=max(lis)
        if lis[0][0]>=max_p[0]:
            printq.append(lis.pop(0))
        else:
            lis.append(lis.pop(0))
    c=0
    for i in printq:
        if i[1]==location:
            return c+1
        c+=1
    return answer

print(solution([2,1,3,2],2))#1
print(solution([1,1,9,1,1,1],0))#5
print(solution([1,2,3],0))#3