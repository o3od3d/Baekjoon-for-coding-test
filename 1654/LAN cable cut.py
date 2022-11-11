K, N = map(int,input().split())
cable = []
for _ in range(K):
    cable.append(int(input()))
start,end = 1, max(cable)
lan = 0
while start <= end:
    mid = (start + end) // 2
    lan2 = 0
    for m in cable:
        while m >= mid:
            lan2 += 1
            m -= mid
    if lan2 >= N:
        if lan < mid:
            lan = mid
        start = mid + 1
    else:
        end = mid - 1
print(lan)