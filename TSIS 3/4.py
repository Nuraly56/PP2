x = input().split()
for i in reversed(range(len(x))):
    if x[i] == '0':
        x.append(x.pop(i))
print(*x)