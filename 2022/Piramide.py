from sys import exit
from math import ceil

def pyramid(n):
    l = list()
    ll = list()
    for i in range(n):
        for x in range(n):
            l.append(1)
        ll.append(l.copy())
        l.clear()
    altura = ceil(n / 2)
    for k in range(altura + 1):
        for i in range(len(ll)):
            for x in range(len(ll[i])):
                if i >= k-1 and i <= len(ll)-k and x >= k-1 and x <= len(ll[i])-k:
                    ll[i][x] = k
    return ll
try:
    n = int(input())
    if 1 <= n <= 100:
        for list in pyramid(n):
            for value in list:
                print(value, end="")
            print()
    else:
        exit()
except:
    exit()
exit()