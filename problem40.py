import time
st = time.time()
sayi = ""
for i in range(1000001):
    sayi+=str(i)
carpim = 1
carpim = int(sayi[1]) * int(sayi[10]) * int(sayi[100]) * int(sayi[1000]) * int(sayi[10000]) * int(sayi[100000]) * int(sayi[1000000])

print(carpim)
print(time.time()-st)
#210     1.5269479751586914