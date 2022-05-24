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

primes= [2]
for i in range(3,10000,2):
    if isPrime(i):
        primes.append(i)
karesi=[]
for i in range(1,1000):
    karesi.append((i**2)*2)
for i in range(1,9999,2):
    sayac = 0
    for x in karesi:
        if x<i-2 and (i-x) in primes:
            sayac += 1

        if x>i:
            break
    if 0 < sayac:
        continue
    elif not isPrime(i) and i != 1:
        print(i)
        break
print(time.time()-st)

#5777   1.4233574867248535