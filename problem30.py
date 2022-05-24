import time
st = time.time()
def us(i):
    sayi = 0
    for j in str(i):
        sayi+= int(j)**5
    if sayi == i:
        return True

sayi = 0

for i in range(2,300000):
    if us(i):
        sayi+=i
print(sayi)
print(time.time()-st)
# 443839      0.6791574954986572
