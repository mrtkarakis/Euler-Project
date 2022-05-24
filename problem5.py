import time
st = time.time()
sayac,sayi = 0,0

for i in range(96996900,1000000000000,20):
    if not sayi:
        for j in range(20,10,-1):
            if i%j!=0:
                sayac = 0
                break
            if i%j == 0:
                sayac += 1
            if sayac == 10:
                sayi = i
    else:
        break
print(sayi)

print(time.time()-st)

#232792560    3.532226905822754
