def Sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if(arr[j+1]<arr[j]):
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
    return arr

def solution(array, commands):
    answer = []
    for i in commands:
        slic=array[i[0]-1:i[1]]
        slic=Sort(slic)
        answer.append(slic[i[2]-1])
    
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))