d = dict()
for _ in range(436):
    certo = False
    frase = str(input()).split(";")
    if int(frase[0]) == 0:
        break
    else:
        dia = int(frase[1].split("/")[0])
        mes = int(frase[1].split("/")[1])
        ano = int(frase[1].split("/")[2])
        if 1 <= int(frase[0]) <= 2135 and 2009 <= ano <= 2019 and 1 <= mes <= 12 and 1 <= dia <= 31 and 1 <= int(frase[2]) <= 5 and 729819.96 <= float(frase[5]) <= 205329753.89:
            if ano == 2009:
                if mes > 5 or mes == 5 and dia >= 27:
                    certo = True
            else:
                if ano == 2019:
                    if mes < 3 or mes == 3 and dia <= 30:
                        certo = True
                else:
                    certo = True
    if certo:
        f = f"{frase[3].title()} {frase[4].upper()}"
        if f not in d.keys():
            d[f] = float(frase[5])
        else:
            d[f] += float(frase[5])
sorted(d, reverse=True)

if len(d) > 3:
    d.pop(list(d.keys())[-1])
for k, v in d.items():
    print(f"{k} {v}")
