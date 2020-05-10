'''
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]

new_list = list(map(list, zip(*mylist)))
for i,j,k in zip(*mylist):
    print(i,j,k)
print(new_list)

'''
sum=0
for i in range(1,150):
    sum+=i
    if(sum>=10000):
        print(i)
        print(sum)
        break
