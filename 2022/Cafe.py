import sys
while True:
    try:
        a1 = int(input())
    except:
        sys.exit()
    if 1 <= a1 <= 1000:
        break
    else:
        sys.exit()
while True:
    try:
        a2 = int(input())
    except:
        sys.exit()
    if 1 <= a2 <= 1000:
        break
    else:
        sys.exit()
while True:
    try:
        a3 = int(input())
    except:
        sys.exit()
    if 1 <= a3 <= 1000:
        break
    else:
        sys.exit()
if a3 > a2 < a1 > a3:
    print(a2*2 + a3*4)
if a3 > a1 < a2 > a3:
    print(a1*2 + a3*2)
if a2 > a1 < a3 > a2:
    print(a1*4 + a2*2)
if a3 < a1 > a2 > a3:
    print(a2*2 + a3*4)
if a1 > a3 < a2 > a1:
    print(a1*2 + a3*2)
if a2 < a1 < a3 > a2:
    print(a1*4 + a2*2)
sys.exit()