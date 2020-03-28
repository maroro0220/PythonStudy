def solution(k, room_number):
    answer = []
    m=dict()
    for i in room_number:
        if(not i in m):
            answer.append(i)
            m[i]=True
        else:
            for j in range(i+1,k):
                if(not j in m):
                    answer.append(j)
                    m[j]=True
                    break
            
    return answer
print(solution(10, [1,3,4,1,3,1]))