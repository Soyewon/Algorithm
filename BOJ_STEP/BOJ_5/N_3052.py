# 나머지

arr=[]
arr2=[]
for i in range(10):
    n=int(input())
    arr.append(n%42)

arr2=set(arr)
print(len(arr2))