# 주유소
#5 /-2-/2/-3-/4/-1-/1

N=int(input()) # 도시의 개수
dis=list(map(int,input().split())) # 도로의 길이(왼쪽부터)
price=list(map(int,input().split())) # 주유소 리터당 가격(왼쪽 도시부터)

cost=0
min=price[0]

for i in range(0,N-1):
    if min<=price[i]:
        cost+=min*dis[i]
    else:
        min=price[i]
        cost+=min*dis[i]

print(cost)