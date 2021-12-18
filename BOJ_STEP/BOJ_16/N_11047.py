# 동전 0

# 문제 조건 유의-i ≥ 2인 경우에 Ai는 Ai-1의 배수

N, K = map(int, input().split())
coin=[] # 동전의 가치 넣을 배열
cnt=0

for i in range(N):
    coin.append(int(input()))

for i in range(N-1, -1, -1):
    cnt += (K // coin[i])
    K = (K % coin[i])

print(cnt)