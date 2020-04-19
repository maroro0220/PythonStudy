def solution(clothes):
    answer = 0
    cl=dict()
    for c,t in clothes:
        if(t in cl):
            cl[t]=cl[t]+','+c
        else:
            cl[t]=c
    ans=1
    for val in cl.values():
        ans*=((len(val.split(',')))+1)
    return ans-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])