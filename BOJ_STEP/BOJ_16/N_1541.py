# 잃어버린 괄호
#55-50+40-40+30

cal=input().split("-") # 55/-/50+40/-/40+30
cal_split=[]
sum=0 # +로 묶인 숫자들을 합치기 위한 변수
sum2=0 # 첫번째 - 등장 이후 나오는 +들의 값을 뺴주기 위한 변수

for i in cal[0].split("+"):
    sum += int(i)

for i in cal[1:]:
    cal_split=i.split("+")
    for j in cal_split:
        sum2+=int(j)
        cal_split=[0]

print(sum-sum2)