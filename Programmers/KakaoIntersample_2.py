def solution(s):
    answer = []

    liss=list()
    for i in range(1,len(s)-1):
        lis=list()
        if(s[i]=='{'):
            sti=i+1
            for j in range(i+1,len(s)-1):
                if(s[j]==','):
                    lis.append(int(s[sti:j]))
                    sti=j+1
                if(s[j]=='}'): 
                    lis.append(int(s[sti:j]))
                    break
        if(len(lis)):
            liss.append(lis)
    lissor=list()
    for i in range(len(liss)):
        for j in liss:
            if (len(j)==i+1):
                s1=set(j)
                s2=set(lissor)
                a=s1-s2
                a1=list(a)
                lissor.append(a1[0])                
    #print(lissor)
    answer=lissor
    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")