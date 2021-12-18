# 최댓값

arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

m = max(arr)
p = arr.index(m) + 1

print(m)
print(p)