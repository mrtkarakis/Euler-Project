import time
st = time.time()
liste1=[]
a = 0
b = 1
while a+b < 4000000:
    if (a+b)%2==0:
        liste1.append(a+b)
        c=b
        b=a+b
        a=c
    else:
        c=b
        b=a+b
        a=c
toplam = 0
for i in liste1:
    toplam+=i
print(toplam)
print(time.time()-st)


# 4613732    0.0