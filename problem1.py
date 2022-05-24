import time
st =time.time()
sayilar ={3,5}
for i in range(1,1000):
    if i %3 ==0:
        sayilar.add(i)
    elif i % 5 == 0:
        sayilar.add(i)
    else:
        continue
toplam = 0
for i in sayilar:
    toplam+=i
print((toplam))
print(time.time()-st)

# 233168    0.0