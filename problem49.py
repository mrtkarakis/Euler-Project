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

asallar = []
sayilar = []
for i in range(3341,999,-2):
    if isPrime(i):
        asallar.append(i)
for i in asallar:
    if isPrime(i+3330) and isPrime(i+6660):
        a = []
        b = []
        c = []
        for x in range(i,i+6661,3330):
            if x<i+1:
                for j in str(x):
                    a.append(j)
            elif x < i+3331:
                for j in str(x):
                    b.append(j)
            elif x < i+6661:
                for j in str(x):
                    c.append(j)
        a.sort()
        b.sort()
        c.sort()
        if a == b and a == c and c == b:
            sayilar.append(i)
            sayilar.append(i+3330)
            sayilar.append(i+6660)
            break
        continue
    continue

sonuc = ""
for i in sayilar:
    for j in str(i) :
        sonuc+=j

print(sonuc)
print(time.time()-st)

# 296962999629    0.0009980201721191406