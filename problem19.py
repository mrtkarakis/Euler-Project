import time
st = time.time()

months = (31,28,31,30,31,30,31,31,30,31,30,31)

day = (366-(365//7)*7)

counter = 0

for i in range(1901,2001):

    for x in months:

        day+=x
        if x == 28 and (i%4==0 or i%100==0 and i%400==0):
            day+=1

        if day%7==0:
            counter+=1

print(counter)

print(time.time()-st)

#171  0.000987781753540039