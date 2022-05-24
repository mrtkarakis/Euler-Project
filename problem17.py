import time
st = time.time()
birler = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
onlar = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
toplam = 0
toplamHarf = 0
for i in range(1,1001):
    if 0 < i < 10:
        toplamHarf += birler[i % 10]

    elif 9 < i < 20:
        toplamHarf += onlar[i % 10]

    elif 19 < i < 40 or 79 < i < 100:
        toplamHarf += birler[i % 10] + 6

    elif 39 < i < 70:
        toplamHarf += birler[i % 10] +5

    elif 69 < i < 80:
        toplamHarf += birler[i % 10] + 7

    elif i == 1000:
        toplam+=11

    elif 99 < i < 101:
        toplam = toplam + 300*13 + 3*toplamHarf - 9

    elif 299 < i < 301:
        toplam = toplam + 300*15 + 3*toplamHarf - 9

    elif 399 < i < 401:
        toplam = toplam + 300*14 + 3*toplamHarf - 9
toplam+=toplamHarf
print(toplam)
print(time.time()-st)

# 21124     0.0