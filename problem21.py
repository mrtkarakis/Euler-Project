import time
qq = time.time()
toplam = 0
def bolunenenler(i):
    bolunenler = 0
    for j in range(1,i//2+1):
        if i%j==0:
            bolunenler += j
    return bolunenler
lst = {0:0,}
for i in range(10001):
    lst[i] = bolunenenler(i)
for x in lst:
    try:
        if lst[lst[x]] == x and lst[x]!=x :
            toplam += x
        else:
            pass
    except:
        pass
print(toplam)
print(time.time()-qq)

#31626      1.1267091274261475