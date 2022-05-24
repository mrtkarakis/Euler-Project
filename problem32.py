import time
st = time.time()
sayilar = {0}
for i in range(1,2000):
    for j in range(1,2000):
        sayac = 0
        sayi = 0
        i=str(i)
        j=str(j)
        for j in i:
            if  j == i[sayi]:
                sayac+=1
                sayi+=1
                break
            else:
                sayi+=1
                continue
        if sayac ==0 :
            j = str(j)
            i =int(i)
            print("j",j,"i",i)
            sayi = i*j
            sonuc = str(sayi) + str(j) + str(i)
            liste = []
            for x in sonuc:
                liste.append(x)
            if liste.count("1") == 1 and liste.count("2") == 1 and liste.count("3") == 1 and liste.count("4") == 1 and liste.count("5") == 1 and liste.count("6") == 1 and liste.count("7") == 1 and liste.count("8") == 1 and liste.count("9") == 1:
                sayilar.add(i*j)
            else:
                continue
        else:
            i =int(i)
            continue
toplam = 0
for i in sayilar:
    toplam+=i
print(toplam)
print(time.time()-st)