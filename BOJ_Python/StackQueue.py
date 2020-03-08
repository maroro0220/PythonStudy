class Stack:
    def __init__(self):
        self.li=[]
        self.idx=0
    def push(self, data):
        self.li.append(data)
        self.idx+=1
    def pop(self):
        self.ret=self.li[self.idx-1]
        self.idx-=1
        return self.ret
s=Stack()
s.push(1)
s.push(2)
for i in range(s.idx):
    print(s.li[i])

print(s.pop())
print(s.pop())


idx=0
li=[]
while(1):
    data=int(input())
    if(data==0):
        break
    elif(data==99):
        if(idx==0):
            print('empty')
        print(li[idx-1])
        idx-=1

    else:
        li.append(data)
        idx+=1
        for i in range(idx):
            print(li[i])
