import time
st = time.time()
x =1
sayi = 1
sayisayac = 1
while x<500:
    sayac=2
    for i in range(2,int(sayi**0.5)+1):
        if sayi%i==0:
            sayac+=2
        else:
            pass
    if sayac>=500:
        x = sayac
    else:
        sayisayac+=1
        sayi += sayisayac
print(sayi)
ft = time.time()
print(ft-st)

#76576500     4.082080364227295