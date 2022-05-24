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
asallar = [2]
x = 3
while x<1050000:
    if isPrime(x) and len(asallar)<10001:
        asallar.append(x)
        x+=2
    elif len(asallar)<10001:
        x+=2
    else:
        break
print(asallar[-1])
ft = time.time()
print(ft-st)

# 104743     0.09873414039611816
