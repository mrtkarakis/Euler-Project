import time

st =time.time()
def combination(i,x):
    perI = 1
    perX = 1
    perIX = 1
    for l in range(1,i+1):
        perI *= l
    for l in range(1,x+1):
        perX *= l
    for l in range(1, (i - x) + 1):
        perIX *= l


    return int((perI/perX) / perIX)
counter = 0
for i in range(10,101):
    for x in range(i//2,3,-1):
        if combination(i,x) > 1000000:
            if i%2 == 0 and x == i//2:
                counter+=1
            else:
                counter+=2
        elif combination(i,x) < 1000000:
            break

print(counter)
print(time.time()-st)

#4075   0.020099163055419922
