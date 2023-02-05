from sys import exit

while True:
    cpf = None
    try:
        cpf = str(input()).strip()
    except:
        exit()
    if cpf.count(cpf[0]) == 11:
        print("Nao")
    if len(cpf) == 1 and cpf[0] == "0":
        exit()
    else:
        if len(cpf) == 11 and cpf.isnumeric():
            s = 0
            for i in range(10, 1, -1):
                s += int(cpf[abs(i-10)]) * i
            p = 0
            if s * 10 % 11 == int(cpf[-2]) or s * 10 % 11 >= 10:
                p += 1
                s = 0
                for i in range(11, 1, -1):
                    s += int(cpf[abs(i-11)]) * i
                if s * 10 % 11 == int(cpf[-1]) or s * 10 % 11 >= 10:
                    p += 1
                if p == 2:
                    print("Sim")
            else:
                print("Nao")
        else:
            print("Nao")
