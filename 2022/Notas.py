from sys import exit
def notas(n):
    cem = cinquenta = vinte = dez = 0
    while True:
        if n >= 100:
            n -= 100
            cem += 1
        elif n >= 50:
            n -= 50
            cinquenta += 1
        elif n >= 20:
            n -= 20
            vinte += 1
        elif n >= 10:
            n -= 10
            dez += 1
        elif n == 0:
            break
    return f"[{cem}, {cinquenta}, {vinte}, {dez}]"
try:
    n = int(input())
    if 1 <= n <= 10000:
        print(notas(n))
    else:
        exit()
except:
    exit()