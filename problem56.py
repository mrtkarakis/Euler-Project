import time
st = time.time()
sonuc = 0
for a in range(1,100):

    for b in range(1,100):

        sayi = 0

        for i in str(a**b):
            sayi+=int(i)
        if sayi > sonuc:
            sonuc = sayi
        else:
            continue


print(sonuc)
print(time.time()-st)

#972     0.15057873725891113