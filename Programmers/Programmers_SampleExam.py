def solution(answers):
    answer = []
    p1=[1,2,3,4,5]#5
    p2=[2,1,2,3,2,4,2,5]#8
    p3=[3,3,1,1,2,2,4,4,5,5]#10
    #p1_a=0
    #p2_a=0
    #p3_a=0
    ans=[0,0,0]
    for i,answ in enumerate(answers):
        if answ==p1[i%len(p1)]:
            ans[0]+=1
        if answ==p2[i%len(p2)]:
            ans[1]+=1
        if answ==p3[i%len(p3)]:
            ans[2]+=1
    for i, score in enumerate(ans):
        if score==max(ans):
            answer.append(i+1)
    '''
    for i in range(len(answers)):
        if answers[i]==p1[i%5]:
            p1_a+=1
        if answers[i]==p2[i%8]:
            p2_a+=1
        if answers[i]==p3[i%10]:
            p3_a+=1
    maxi=max(p1_a,p2_a,p3_a)
    if(p1_a==maxi):
        answer.append(1)
    if(p2_a==maxi):
        answer.append(2)
    if(p3_a==maxi):
        answer.append(3)
    '''
    return answer

solution([1,2,3,4,5])
solution([1,3,2,4,2])