import time
st =time.time()

def cont(x):
    x2 = str(x*2)
    x3 = str(x*3)
    x4 = str(x*4)
    x5 = str(x*5)
    x6 = str(x*6)
    x = str(x)
    if len(x) == len(x2) and len(x2) == len(x3) and len(x3) == len(x4) and len(x4) == len(x5) and len(x5) == len(x6):
        if len(x) == 6:
            if x2.count(x[0]) == 1 and x2.count(x[1]) == 1 and x2.count(x[2]) == 1 and x2.count(x[3]) == 1 and x2.count(x[4]) == 1 and x2.count(x[5]) == 1 and x3.count(x[0]) == 1 and x3.count(x[1]) == 1 and x3.count(x[2]) == 1 and x3.count(x[3]) == 1 and x3.count(x[4]) == 1 and x3.count(x[5]) == 1 and x4.count(x[0]) == 1 and x4.count(x[1]) == 1 and x4.count(x[2]) == 1 and x4.count(x[3]) == 1 and x4.count(x[4]) == 1 and x4.count(x[5]) == 1 and x5.count(x[0]) == 1 and x5.count(x[1]) == 1 and x5.count(x[2]) == 1 and x5.count(x[3]) == 1 and x5.count(x[4]) == 1 and x5.count(x[5]) == 1 and x6.count(x[0]) == 1 and x6.count(x[1]) == 1 and x6.count(x[2]) == 1 and x6.count(x[3]) == 1 and x6.count(x[4]) == 1 and x6.count(x[5]) == 1:
                return True
            return False

for i in range(100000,99999999999):
    if cont(i):
        print(i)
        break
print(time.time()-st)

#142857   0.07973540496826172