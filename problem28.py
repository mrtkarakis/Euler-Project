import time
st = time.time()
sayi,sayac = 1 , 1
for i in range(1,1002,2):
    if i !=1:
        sayi = sayi + (((i**2)+(i**2-(sayac*6)))*2)
        print(sayi)
        sayac+=1
    else:
        continue
print(sayi)
print(time.time() - st )
# 669171001     0.0