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

134
def asal_bolen(sayi):
    sayilar = set()
    for i in primes:
        while sayi%i==0:
            sayi=sayi/i
            sayilar.add(i)
    if len(sayilar) ==4 :
        return True
    else:
        return False

primes = [2]
for i in range(3,750,2):
    if isPrime(i):
        primes.append(i)
    else:
        continue

for i in range(1000,200000):
    if asal_bolen(i) and asal_bolen(i+1) and  asal_bolen(i+2) and asal_bolen(i+3):
        print(i)
        break
    else:
        continue
print(time.time()-st)

#134043   1.3452860355377197