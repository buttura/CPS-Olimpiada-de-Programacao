from sys import exit

try:
    cdt = str(input()).split()
    if len(cdt) == 1 and cdt[0] == "0":
        exit()
    else:
        if 1 <= int(cdt[0]) <= 50 and 1 <= int(cdt[1]) <= 1000 and 0 <= int(cdt[2]) <= 100:
            qc = int(cdt[1]) / int(cdt[0]) - int(cdt[2])
            if qc <= 0:
                print(f"{0:.1f}")
            else:
                print(f"{qc:.1f}")
except:
    exit()
exit()