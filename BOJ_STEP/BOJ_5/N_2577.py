# 숫자의 개수

A=int(input())
B=int(input())
C=int(input())

mul=A*B*C
arr=list(str(mul))

for i in range(10):
    print(arr.count(str(i)))