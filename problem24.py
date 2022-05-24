import time
st = time.time()
a = [0,1,2,3,4,5,6,7,8,9]
sayi =[]
fak=1
x = 1000000
t = 0
while t < 10:
    fak=1
    for i in range(1,len(a)):
        fak*=i
    sayac=0
    while x-fak > 0:
        x -= fak
        sayac+=1
    sayi.append(a[sayac])
    a.remove(sayi[-1])
    t+=1
print(f"{sayi[0]}{sayi[1]}{sayi[2]}{sayi[3]}{sayi[4]}{sayi[5]}{sayi[6]}{sayi[7]}{sayi[8]}{sayi[9]}")
print(time.time()-st)
# 2783915460    0.0