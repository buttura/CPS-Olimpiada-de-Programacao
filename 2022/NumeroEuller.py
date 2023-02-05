from sys import exit
try:
    n = int(input())
    if n >= 0 and 0 <= n <= 10000:
        print(f"{(1 + 1/n)**n:.24f}")
    else:
        exit()
except:
    exit()
exit()