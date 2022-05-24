import time
st = time.time()
triangel = []
pentagonal = []
hexagonal = []
i = 1
stop = 0
while stop <3:
    triangel.append(int((i*(i+1))/2))
    pentagonal.append(int((i*(3*i-1))/2))
    hexagonal.append(int((i*(2*i-1)))),
    if triangel[i-1] in pentagonal and triangel[i-1] in hexagonal:
        stop+=1
        i+=1
    else:
        i+=1

print(triangel[-1])
print(time.time()-st)

#1533776805       18.92543053627014