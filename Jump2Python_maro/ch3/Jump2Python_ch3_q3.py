'''
while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

*
**
***
****
*****
'''
n=5
i=0
while i<n:
    j=0
    while j<=i:
        print('*',end='')
        j+=1
    print('')    
    i+=1
'''
i=1
while i<=n:
    print('*'*i)
    i+=1
'''