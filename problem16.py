import time
st =time.time()
sayi = 2**1000
sayi = str(sayi)
toplam = 0
for i in sayi:
    toplam+=int(i)
print(toplam)
print(time.time()-st)
# 1366    0.0