from sys import exit
while True:
    n = 0
    try:
        n = int(input())
    except:
        exit()
    if 0 <= n <= 15:
        if n == 0:
            exit()
        m = 0
        try:
            m = str(input()).strip().split()
            if len(m) == 1 and m[0] == "0":
                exit()
        except:
            exit()
        if len(m) == n**2:
            for i in range(len(m)):
                print(m[i], end="")
                if (i+1) % n == 0:
                    print()
            print("transposta")
            for x in range(n):
                for i in range(len(m)):
                    if (i+x) % n == 0:
                        print(m[i], end="")
                print()
    else:
        exit()
