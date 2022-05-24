import time
st = time.time()
for i in range (1,500):
    for j in range(i+1,500):
        a = ((i**2)+(j**2))**0.5
        if a + i + j  == 1000 and a == int(a):
            print(i*j*a)
print(time.time()-st)

# 31875000     0.0987033748626709