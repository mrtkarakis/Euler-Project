import time
st=time.time()
def palindrom(i):
    x = str(i)[::-1]
    if int(x) ==i:
        return True
    else:
        return False
def binpalindrom(i):
    bsayi = bin(i)
    bsayi = bsayi.lstrip("0b")
    if palindrom(int(bsayi)):
        return True
    else:
        return False

toplam = 0
for i in range(1,1000002):
    if binpalindrom(i) and palindrom(i):
        toplam+=i
    else:
        pass
print(toplam)
print(time.time()-st)

#872187   0.9872056770324707