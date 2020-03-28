cnt=0
chk=list()
tmp=list()
ttmp=list()
def dfs(uid,bid,c):
    global cnt
    global chk
    global tmp
    global ttmp
    if(c==len(bid)):
        if len(ttmp):
            for i in range(len(ttmp)):
                print(ttmp)
                if not (set(ttmp[i])-set(tmp)):
                    cnt+=1
                    ttmp.append(tmp)
        else: ttmp.append(tmp)
        return
    for i in range(c,len(bid)):
        for j in range(len(uid)):
            if(chk[j]==1): continue
            else:
                if(Chk(uid[j],bid[i])):
                    chk[j]=1
                    tmp.append(uid[j])
                    dfs(uid,bid,c+1)
                    tmp.remove(uid[j])
                    chk[j]=0

def Chk(a, b):
    if(len(a)==len(b)):
        for i in range(len(a)):
            if(b[i]=='*'): continue
            if(a[i]!=b[i]):
                return False
        print(a,end=' ') 
        print(b)
        return True

        
    
def solution(user_id, banned_id):
    answer = 0
    global cnt
    global chk
    chk=[0 for _ in range(len(user_id))]
    cnt=0
    dfs(user_id,banned_id,0)
    answer=cnt
    '''
    for s in banned_id:
        for ss in user_id:
            if(len(s)==len(ss)):
                chk=True
                for i in range(len(ss)):
                    if(s[i]=='*'): continue
                    if(s[i]!=ss[i]):
                        chk=False
                        break
                if chk: 
                    answer+=1
                    break
    '''
    return answer

#a=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])#2
#print(a)
#a=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])#2
#print(a)
a=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])#3
print(a)
