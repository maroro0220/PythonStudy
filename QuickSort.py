def Quick(arr,l,r):
    if l>r:
        return arr
    pivo=arr[(l+r)//2]
    #pivo=l
    left=l
    right=r
    
    while(left<=right):
        while(arr[left]<pivo ):
            left+=1
        while( pivo<arr[right] ):
            right-=1
        if(left<=right):
       # if True:
            tmp=arr[left]
            arr[left]=arr[right]
            arr[right]=tmp
            left+=1
            right-=1
    #if(left<right):
     #   tmp=arr[pivo]
     #   arr[pivo]=arr[right]
     #   arr[right]=tmp
    #if True:
        Quick(arr,l,right)
        Quick(arr,left,r)
    return arr
array=[5,4,6,3,4,1]
print(Quick(array,0,len(array)-1))