import time
st = time.time()
liste=[]
liste1 = []
liste2 = []
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        sayi = i*j
        for x in str(sayi):
            liste1.append(x)
            liste2.append(x)
        liste2.reverse()
        if liste1 == liste2:
            liste.append(i*j)
        else:
            liste1.clear()
            liste2.clear()
            pass
liste.sort()
print(liste[-1])
print(time.time()-st)

# 906609   1.213745355606079

print("***********pratik************")
n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                 n = a * b
print(n)