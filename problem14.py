import time
st = time.time()
enUzunZincir = [0]
suankiZincir = []
zincir = {1 : 1}
for i in range(1,1000001):
    suankiZincir.clear
    x = i
    sayac = 1
    while i !=1:
        if i in zincir:
            sayac += zincir[i]
            break
        elif i % 2==0:
            i= i/2
            sayac+=1
        elif i % 2!=0:
            i = 3*i+1
            sayac+=1
    suankiZincir.append(sayac)
    zincir.setdefault(x,sayac)
    if suankiZincir[-1] > enUzunZincir[-1]:
        enUzunZincir.clear()
        enUzunZincir.append(x)
        enUzunZincir.append(sayac)
    else:
        continue
print(enUzunZincir)

print(time.time()-st)

#837799       2.5372142791748047