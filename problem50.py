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

asallar = [2]
sonuc = { 2 : 1  }
for i in range(3,4000,2):
    if isPrime(i):
        asallar.append(i)
while len(asallar) > 1:
    toplam = 0
    sayac = 0
    for i in asallar:
        toplam+=i
        sayac+=1
        if (not toplam in sonuc  or sonuc[toplam] <= sayac) and isPrime(toplam) and toplam < 1000000:
            sonuc[toplam] = sayac
    asallar.pop(0)

sonuckey = []
for x in sonuc.keys():
    sonuckey.append(x)
for i in sonuckey:
    if  max(list(sonuc.values())) != sonuc[i]:
        sonuc.pop(i)
    else:
        continue

print(sonuc)
print(time.time()-st)


#{997651: 543}    1.9013128280639648