N = int(input())
arrN = list(map(int,input().split()))
M = int(input())
arrM = list(map(int,input().split()))
start = 0
end = N-1
arrN.sort()
for i in range(M):
    start = 0
    end = N - 1
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if arrM[i] > arrN[mid]:
            start = mid + 1
        elif arrM[i] < arrN[mid]:
            end = mid - 1
        else:
            ans = 1
            break
    print(ans)