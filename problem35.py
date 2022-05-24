import time
st = time.time()
def isPrime(sayi):
    if sayi == 0:
        return False
    elif sayi == 1:
        return False
    elif sayi == 2 :
        return True
    else:
        if sayi %2==0:
            return False
        else:
            for i in range(3,int((sayi**0.5)+1),2):
                if sayi%i==0:
                    return False
            return True
def basamaklar(sayi):
    if sayi ==2:
        return True
    ciftler = ["0","2","4","6","8"]
    for i in str(sayi):
        if i in ciftler:
            return False
        else:
            pass
    return True
def dongu(x):
    x = str(x)
    for u in range(len(x)-1):
        x = x + x[0]
        x = str(int(x) - ((10**(len(x)-1))*int(x[-1])))
        if isPrime(int(x)):
            sayilar.append(int(x))
            pass
        else:
            return False
    return True
toplam = 1
sayilar = []
for i in range(3,1000001,2):
    if isPrime(i) and basamaklar(i) and not i in sayilar:
        if dongu(i):
            toplam+=len(str(i))
            if len(str(i))>1 and  str(i).count(str(i)[0]) == len(str(i)):
                toplam-=(len(str(i))-((len(str(i))-1)))
    else:
        continue
print(toplam)
print(time.time()-st)

print("**************************************************")

import time
st =time.time()
def isPrime(sayi):
    if sayi == 0:
        return False
    elif sayi == 1:
        return False
    elif sayi == 2 :
        return True
    else:
        if sayi %2==0:
            return False
        else:
            for i in range(3,int((sayi**0.5)+1),2):
                if sayi%i==0:
                    return False
            return True
def basamaklar(sayi):
    if sayi ==2:
        return True
    sayi = str(sayi)
    if sayi.count("0") or sayi.count("2") or sayi.count("4") or sayi.count("6") or sayi.count("8"):
        return False
    else:
        return True
def dongu(x):
    x = str(x)
    for u in range(len(x)-1):
        x = x + x[0]
        x = str(int(x) - ((10**(len(x)-1))*int(x[-1])))
        if isPrime(int(x)):
            sayilar.append(int(x))
            pass
        else:
            return False
    return True
toplam = 1
sayilar = []
for i in range(3,1000001,2):
    if isPrime(i) and basamaklar(i) and not i in sayilar:
        if dongu(i):
            toplam+=len(str(i))
            if len(str(i))>1 and  str(i).count(str(i)[0]) == len(str(i)):
                toplam-=(len(str(i))-((len(str(i))-1)))
    else:
        continue



print(toplam)
print(time.time()-st)

#55    2.0744290351867676