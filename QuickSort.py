def Quick(arr,l,r):
    if l>r:
        return
    pivo=(l+r)//2
    #pivo=l
    left=l
    right=r
    
    while(left<=right):
        while(arr[left]<arr[pivo] ):
            left+=1
        while(arr[pivo]<arr[right] ):
            right-=1
        tmp=arr[left]
        arr[left]=arr[right]
        arr[right]=tmp
        left+=1
        right-=1
    #if(left<right):
    #    tmp=arr[pivo]
    #    arr[pivo]=arr[right]
    #    arr[right]=tmp
    Quick(arr,l,right)
    Quick(arr,left,r)
    return arr
array=[5,4,2,3,4,1]
print(Quick(array,0,len(array)-1))