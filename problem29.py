import time
st=time.time()
sayilar = {4}
for i in range(2,101):
    for j in range(2,101):
        sayilar.add(i**j)
print(len(sayilar))
print(time.time()-st)
# 9183      0.008967161178588867