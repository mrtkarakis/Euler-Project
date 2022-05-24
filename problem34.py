import time
st = time.time()
def faktoriyel(x):
    sayi =1
    for i in range(1,x+1):
        sayi*=i
    return sayi
def basamaklar(y):
    sayi = 0
    y = str(y)
    for i in range(len(y)):
        sayi+=faktoriyel(int(y[i]))
    if sayi == int(y):
        return True
    else:
        pass
toplam = 0
for j in range(3,409113):
    if basamaklar(j):
        toplam+=j
    else:
        continue
print(toplam)
print(time.time()-st)

# 40730    1.395543556213379