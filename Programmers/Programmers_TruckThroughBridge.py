def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[0]*bridge_length
    sum=0
    while bridge:
        answer+=1
        #if not len(bridge):
        #    break
        sum-=bridge[0]
        bridge.pop(0)
        if truck_weights:
            if sum+truck_weights[0]<=weight:
                sum+=truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        '''
        if(not len(on) and not len(truck_weights)):
            break
        answer+=1
        if(len(on)):
            onsum=0
            for i in range(0,len(on),bridge_length):
                onsum+=on[i]
        if(not len(truck_weights) and len(on)):
            gone.append(on.pop(0))
            #answer+=1
        elif(len(on) and len(truck_weights)):
            gone.append(on.pop(0))
            
            if(len(on)):
                onsum=0
                for i in range(0,len(on),bridge_length):
                    onsum+=on[i]
            else:
                onsum=0
            if(onsum+truck_weights[0]<=weight):
                t=truck_weights.pop(0)
                if(not len(on)):
                    for i in range(0,bridge_length-len(on)):
                        on.append(t)
                else:
                    on.append(t)
        elif(not len(on) and len(truck_weights)):
                t=truck_weights.pop(0)
                for i in range(0,bridge_length-len(on)):
                    on.append(t)                
        elif(len(on) and not len(truck_weights)):
            gone.append(on.pop(0))
            #if(len(gone) and not len(gone)%bridge_length):
                #onsum-=gone[len(gone)//bridge_length]
        #answer+=1
        '''

    return answer

#print(solution(2,10,[7,4,5,6]))
#print(solution(100,100,[10]))
#print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
#print(solution(1,2,[1,1,1]))#4
#print(solution(1,1,[1,1,1]))#4
print(solution(4,2,[1, 1, 1, 1]))#10`
#print(solution(3,3,[1, 1, 1 ]))#6
#print(solution(3,1,[1, 1, 1 ]))#10
print(solution(5,5,[1, 1, 1,1,1,2,2 ]))#14
print(solution(7,7,[1, 1, 1,1,1,3,3 ]))#18
print(solution(5,5,[1, 1, 1,1,1,2,2,2,2 ]))#19
print(solution(5,5,[2,2,2,2,1,1,1,1,1 ]))#19