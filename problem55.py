import time
st =time.time()
def palindromic(i):
    if str(i) == str(i)[::-1]:
        return True
    else:
        return False

toplam = 0

for i in range(1,10001):
    sayi = int(i)+int(str(i)[::-1])
    for j in range(50):
        if palindromic(sayi):
            toplam+=1

            break
        else:
            sayi = sayi+int(str(sayi)[::-1])
print(10000-toplam)
print(time.time()-st)

#249    0.04983591079711914