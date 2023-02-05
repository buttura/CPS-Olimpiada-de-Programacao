from sys import exit
a = list()
ta = list()
try:
    anm = str(input()).split()
    if len(anm) == 1 and "0" in anm:
        exit()
    if len(anm) == 3 and 2 <= int(anm[0]) <= 100 and 1 <= int(anm[1]) <= 100 and 1 <= int(anm[2]) <= 100:
        for _ in range(int(anm[1])):
            n = str(input()).split()
            if len(n) == int(anm[2]):
                for i in range(len(n)):
                    if 0 <= int(n[i]) <= 1:
                        a.append(int(n[i]))
                ta.append(a.copy())
                a.clear()
    else:
        exit()
    for totalassentos in range(len(ta)):
        if ta[-totalassentos].count(0) == int(anm[0]):
            print(totalassentos)
            exit()
    print("-1")
except:
    exit()
exit()