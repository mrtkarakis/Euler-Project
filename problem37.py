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

def sag(sayi):
    for x in range(len(str(sayi))-1):
        sayi = sayi-(int(str(sayi)[0])*10**(len(str(sayi))-1))
        if isPrime(sayi):
            pass
        else:
            return False
    return True
def sol(sayi):
    for x in range(len(str(sayi))-1):
        sayi = sayi//10
        if isPrime(sayi):
            pass
        else:
            return False
    return True

toplam = 0

for i in range(11,1000001,2):
    if isPrime(i):
        if sag(i) and sol(i):
            toplam+=i
    else:
        continue
print(toplam)
print(time.time()-st)

#748317       1.993400001525879