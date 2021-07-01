x = list(map(int, input().split()))
n = int(input())
lst = x[-n:] + x[:-n]
print(*lst)