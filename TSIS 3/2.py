x = input().split()
sum = 1001
for i in range(len(x)):
    if i > 0 and i < sum:
        sum = i
print(sum)