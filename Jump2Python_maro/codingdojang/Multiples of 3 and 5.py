'''
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.

1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

'''

sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        sum+=i

print(sum)
#a=int(input("A"))
#b=int(input("B"))
num=int(input())

print(num[0]+num[1])