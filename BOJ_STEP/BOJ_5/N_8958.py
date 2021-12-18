# OX퀴즈

n=int(input())

for i in range(n):
    score=input()
    ans=list(score)
    total=0
    cnt=1
    for i in ans:
        if i=='O':
            total+=cnt
            cnt+=1
        else:
            cnt=1
    print(total)