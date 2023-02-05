from sys import exit
try:
    l = list()
    lc = str(input()).strip().split()
    if 1 <= int(lc[0]) <= 100 and 1 <= int(lc[1]) <= 100:
        for i in range(int(lc[0])):
            pc = str(input()).strip().split()
            if len(pc) == int(lc[1]):
                l.append(pc.copy())
            else:
                exit()
        s = 0
        sum = list()
        for x in range(len(l[0])):
            for i in range(len(l)):
                s += int(l[i][x])
            sum.append(s)
            s = 0
        upper = 0
        for e, v in enumerate(sum):
            if e == 0:
                upper = v
            elif v > upper:
                upper = v
        print(upper)
    else:
        exit()
except:
    exit()
exit()