import time
st = time.time()
kareleri = 0
toplamları =0
for i in range(1,101):
    kareleri = kareleri + (i**2)
for i in range(1,101):
    toplamları+=i
sonuc = (toplamları**2)-kareleri
print(sonuc)
print(time.time()-st)


# 25164150  0.0