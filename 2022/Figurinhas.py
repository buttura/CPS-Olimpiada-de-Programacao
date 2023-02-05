import sys
while True:
    n = int(input())
    if 1 <= n <= 100:
        break
    else:
        sys.exit()
while True:
    m = int(input())
    if 1 <= m <= 300:
        break
l = list()
for _ in range(m):
    x = 0
    try:
        x = int(input())
    except:
        sys.exit()
    if 1 <= x <= n:
        if x not in l:
            l.append(x)
print(n - len(l))
sys.exit()