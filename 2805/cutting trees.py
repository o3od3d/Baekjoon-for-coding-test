N,M = map(int,input().split())
treeinfos = list(map(int,input().split()))
start,end  = 1, max(treeinfos)
while start <= end:
    mid = (start + end) // 2
    log = 0
    for i in treeinfos:
        if mid < i:
            log += (i - mid)

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
