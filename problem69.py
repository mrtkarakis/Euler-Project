import time
st =time.time()

sayilar = [0,0]
i = 10
a = 10

while i < 1000001:
    bölensayilar = set()
    for q in range(1,i//2):
        bölensayilar.add(q*2)
    for x in range(3,int(i**0.5),2):
        if i%x==0:
            for j in range(1,i//x,2):
                bölensayilar.add(j*x)

    if sayilar[1] < i/(i-len(bölensayilar)-1) and i%10 ==0 :
        sayilar.clear()
        sayilar.append(i)
        sayilar.append(i/(i-len(bölensayilar)-1))
        a = i//2

    i+= a

print(sayilar)
print(time.time()-st)

#510510    1.696836519241333