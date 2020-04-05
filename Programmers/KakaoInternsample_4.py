def solution(k, room_number):
    answer = []
    m=dict()
    for i in room_number:
        if( i not in m.keys()):
            answer.append(i)
            m[i]=i+1;
             
        else:
            b=[]
            j=m[i]
            while j in m:
                b.append(j)
                j=m[j]
            for bb in b:# This is important. if input is [1,1,1,3,1,1,1], result after this function is m[3] = 6. So it sholud be update 
                m[bb]=j+1
            m[j]=j+1
            answer.append(j)
            
    return answer
print(solution(10, [1,3,4,1,3,1]))
#print(solution(10, [1, 2, 3, 1, 1]))