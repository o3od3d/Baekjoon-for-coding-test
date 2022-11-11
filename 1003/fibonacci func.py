T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))

cnt1 = 0
cnt2 = 0
def fibonacci(n):
    global cnt1,cnt2
    if n == 0:
        cnt1 += 1
        return 0
    elif n == 1:
        cnt2 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(T):
    cnt1,cnt2 = 0,0
    tmp = fibonacci(N[i])
    print(cnt1,cnt2)