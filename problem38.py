import time
st=time.time()

sayilar = list()

for i in range(10000):
    if str(i)[0] == "9" and str(i).count("0") ==0 :
        sayi1 = str(i * 1) + str(i * 2) + str(i * 3) + str(i * 4) + str(i * 5) + str(i * 6)
        sayi2 = str(i * 1) + str(i * 2) + str(i * 3) + str(i * 4) + str(i * 5)
        sayi3 = str(i * 1) + str(i * 2) + str(i * 3) + str(i * 4)
        sayi4 = str(i * 1) + str(i * 2) + str(i * 3)
        sayi5 = str(i * 1) + str(i * 2)

        if sayi1.count("0") == 0 and sayi1.count("1") == 1 and sayi1.count("2") == 1 and sayi1.count("2") == 1 and sayi1.count("3") == 1 and sayi1.count("4") == 1 and sayi1.count("5") == 1 and sayi1.count("6") == 1 and sayi1.count("7") == 1 and sayi1.count("8") == 1 and sayi1.count("9") == 1:
            sayilar.append(sayi1)

        if sayi2.count("0") == 0 and sayi2.count("1") == 1 and sayi2.count("2") == 1 and sayi2.count("2") == 1 and sayi2.count("3") == 1 and sayi2.count("4") == 1 and sayi2.count("5") == 1 and sayi2.count("6") == 1 and sayi2.count("7") == 1 and sayi2.count("8") == 1 and sayi2.count("9") == 1:
            sayilar.append(sayi2)

        if sayi3.count("0") == 0 and sayi3.count("1") == 1 and sayi3.count("2") == 1 and sayi3.count("2") == 1 and sayi3.count("3") == 1 and sayi3.count("4") == 1 and sayi3.count("5") == 1 and sayi3.count("6") == 1 and sayi3.count("7") == 1 and sayi3.count("8") == 1 and sayi3.count("9") == 1:
            sayilar.append(sayi3)

        if sayi4.count("0") == 0 and sayi4.count("1") == 1 and sayi4.count("2") == 1 and sayi4.count("2") == 1 and sayi4.count("3") == 1 and sayi4.count("4") == 1 and sayi4.count("5") == 1 and sayi4.count("6") == 1 and sayi4.count("7") == 1 and sayi4.count("8") == 1 and sayi4.count("9") == 1:
            sayilar.append(sayi4)

        if sayi5.count("0") == 0 and sayi5.count("1") == 1 and sayi5.count("2") == 1 and sayi5.count("2") == 1 and sayi5.count("3") == 1 and sayi5.count("4") == 1 and sayi5.count("5") == 1 and sayi5.count("6") == 1 and sayi5.count("7") == 1 and sayi5.count("8") == 1 and sayi5.count("9") == 1:
            sayilar.append(sayi5)


        else:
            pass
print(max(sayilar))
print(time.time()-st)

#932718654  0.009570019149780273