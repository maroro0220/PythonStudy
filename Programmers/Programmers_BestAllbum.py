def solution(genres, plays):
    answer = []
    m=dict()#{genre:[[plays,idx]]}
    for i in range(len(genres)):
        if(genres[i] in m):
            #m.update({genres[i]:m[genres[i]].append([plays[i],i])})
            m[genres[i]].append([plays[i],i])
        else:
            m.update({genres[i]:[[plays[i],i]]})
            #m[genres[i]].append([plays[i],i])
    print(m.items())
    lis=list()
    for i in m.keys():
        sum=0
        for j in range(len(m[i])):
            sum+=m[i][j][0]
            #print(m[i][j])
        lis.append([sum,i])
    lis.sort(reverse=True)#sum genres plays
    for i in range(len(lis)):
        #print(lis[i][1])
        #print(type(m[lis[i][1]]))
        m[lis[i][1]].sort(reverse=True)
        
        m[lis[i][1]].sort(key=lambda x: [-x[0],x[1]] )
        print(m.items())
        tmp=list()
        if(len(m[lis[i][1]])==1):
            tmp.append(m[lis[i][1]][0][1])
        else:
            for j in range(2):
                tmp.append(m[lis[i][1]][j][1])
     
        for b in range(len(tmp)):
            answer.append(tmp[b])
            #print(m[lis[i][1]][j][1])    
    for i in answer:
        print(i)
    return answer


solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])#[4,1,3,0]
solution(["classic", "pop", "classic", "classic", "pop"],[400, 400, 400, 400, 400])#

