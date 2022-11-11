
N = int(input())
budget = list(map(int,input().split()))
totalBudget = int(input())
totalAsk = sum(budget)
if totalBudget >= totalAsk:
    print(max(budget))
else:
    start,end = 0,max(budget)
    while start <= end:
        tmpBudget = totalBudget
        mid = (start + end) // 2
        for b in budget:
            if b <= mid:
                tmpBudget -= b
            else:
                tmpBudget -= mid
        if tmpBudget < 0:
            end = mid - 1
        else:
            start = mid + 1
    print(end)