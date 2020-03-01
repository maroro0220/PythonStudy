'''

입력
입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. ( 0 ≤ x < y < 231)

출력
각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 회수를 출력한다.

예제 입력 1 
3
0 3
1 5
45 50
예제 출력 1 
3
3
4
'''
import math
T=int(input())

while T:
    x,y=map(int,input().split())
    dist=y-x
    i=1
    while i*i<=dist:
        i+=1
    i-=1
    #print(i)
    #print(dist)
    dif=dist-(i*i)
    #print(dif/i)
    #dif_cnt=round(dif/i +0.1)
    dif_cnt=math.ceil(dif/i)
    #print(dif_cnt)
    print(2*i-1+dif_cnt)
    T-=1



