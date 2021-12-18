# ATM

N=int(input()) # 사람 수
P = [] # 사람마다 돈 인출하는데 걸리는 시간 P
add = [] # 중간계산을 위한 저장용 배열
tmp=0 # 중간계산을 위한 저장용 임시 변수
result=0

P = list(map(int, input().split()))
P.sort()

for i in P:
    tmp += i
    result += tmp

print(result)