import time
"""
st = time.time()
sayilar = []
sayi = 0
"""
def denetle(x):
    x=str(x)
    if int(x[1]+x[2]+x[3])%2==0 and int(x[2]+x[3]+x[4])%3==0 and int(x[3]+x[4]+x[5])%5==0 and int(x[4]+x[5]+x[6])%7==0 and int(x[5]+x[6]+x[7])%11==0 and int(x[6]+x[7]+x[8])%13==0 and int(x[7]+x[8]+x[9])%17==0:
        return True
    else:
        return False
"""
for i in range(1023456789,6000000000,9):
    i=str(i)
    if i.count("1")==1 and i.count("2")==1 and i.count("3")==1 and i.count("4")==1 and i.count("5")==1 and i.count("6")==1 and i.count("7")==1 and i.count("8")==1 and i.count("9")==1 and i.count("0")==1 :
        if denetle(i):
            sayi+=int(i)
            print(sayi)
        else:
            continue
    else:
        continue


print(sayi)
print(time.time()-st)
"""
st = time.time()
sayi = 0
for a in range(1,10):
    for b in range(10):
        if b != a:
            for c in range(10):
                if c != b and c!=a:
                    for d in range(10):
                        if d !=c and d!=c and d !=a:
                            for e in range(10):
                                if e != d and c!=e and e !=a and e!=b:
                                    for f in range(10):
                                        if f != e and f!=c and f !=a and f!=b and f !=d:
                                            for g in range(10):
                                                if g!=f and f!=c and f !=a and d!=f and f !=b and e !=f:
                                                    for h in range(10):
                                                        if h!=g and h!=c and h !=a and d!=h and h !=b  and h!=e and h !=f:
                                                            for i in range(10):
                                                                if i !=h and i!=c and i !=a and d!=i and i !=b and i!=e and i !=f and i!=g and i !=h:
                                                                    for j in range(10):
                                                                        if j != i and j !=a and d!=j and j !=b and j!=e and j !=f and j!=g and j !=h and j!=c:
                                                                            x = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j))
                                                                            x = str(x)
                                                                            if x.count("1") == 1 and x.count("2") == 1 and x.count("3") == 1 and x.count("4") == 1 and x.count("5") == 1 and x.count("6") == 1 and x.count("7") == 1 and x.count("8") == 1 and x.count("9") == 1 and x.count("0") == 1 and denetle(x):
                                                                                x = int(x)
                                                                                sayi+=x
                                                                                print(x,sayi)
print(time.time()-st)



from itertools import permutations
sol = 0
per = permutations("0123456789")
for i in per:
    if int(''.join(i[1:4])) % 2 == 0 and int(''.join(i[2:5])) % 3 == 0 and int(''.join(i[3:6])) % 5 == 0 and int(''.join(i[4:7])) % 7 == 0 and int(''.join(i[5:8])) % 11 == 0 and int(''.join(i[6:9])) % 13 == 0 and int(''.join(i[7:10])) % 17 == 0:
        sol+=int(''.join(i))
print(sol)
print(time.time()-st)

#16695334890   2.94236421585083