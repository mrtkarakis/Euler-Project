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

toplam = 2

x = 3

while x<2000000:
    if isPrime(x):
        toplam+=x
        x+=2
    else:
        x+=2
print(toplam)
print(time.time()-st)

# 142913828922      4.655710506439209