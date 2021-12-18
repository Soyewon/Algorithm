# 평균은 넘겠지

n=int(input())

for i in range(n):
    arr=list(map(int,input().split()))
    st_num=arr[0]
    arr=arr[1:]
    avg=sum(arr)/st_num
    cnt=0
    for score in arr:
        if score>avg:
            cnt+=1
    per = (cnt/st_num)*100
    print('%.3f' %per + '%')