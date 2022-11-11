N = int(input())
arrN = list(map(int,input().split()))
M = int(input())
arrM = list(map(int,input().split()))
arrN.sort()
print(arrN)
for i in arrM:
    start, end = 0, (N-1)
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if i < arrN[mid]:
            end = mid - 1
        elif i > arrN[mid]:
            start = mid + 1
        else:
            cnt += 1
            end = mid -1
    print(cnt)
