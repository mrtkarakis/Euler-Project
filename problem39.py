import time
st =time.time()
adet = {1 : 1}

for i in range(1,500):
    for j in range(1,i+1):
        if (((i**2)+(j**2))**0.5) == int((((i**2)+(j**2))**0.5)) and i+j+int((((i**2)+(j**2))**0.5))<1000:
            try:
                if adet[i+j+int((((i**2)+(j**2))**0.5))]:
                    adet[i + j + int((((i ** 2) + (j ** 2)) ** 0.5))]+=1
            except:
                adet.setdefault(int((((i**2)+(j**2))**0.5))+i+j, 1)
        else:
            continue
liste = []
for i in adet.values():
    liste.append(i)
for i in range(1,1001):
    try:
        if adet[i] == max(liste):
            print(i)
    except:
        pass
print(time.time()-st)

#840  0.17955987510681152