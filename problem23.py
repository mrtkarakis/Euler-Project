import time
from math import sqrt
st = time.time()
def isPrime(sayi):
    if sayi == 0:
        return False
    elif sayi == 1:
        return False
    elif sayi == 2 :
        return True
    else:
        if sayi %2==0:
            return False
        else:
            for i in range(3,int((sayi**0.5)+1),2):
                if sayi%i==0:
                    return False
            return True

def Pnumber(x):
    number = {1}
    if not isPrime(x):
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                number.add(i)
                number.add(x/i)




        if x < sum(number):
            numbers.append(x)

total = []
numbers = []
for i in range(12,28123):
    Pnumber(i)



for i in range(28123):
    total.append(i)


for i in range(len(numbers)):
    for x in range(i,len(numbers)):
        if numbers[i]+numbers[x] < 28123:
            total[numbers[i]+numbers[x]] = 0
        else:
            break

print(sum(total))
print(time.time()-st)

#4179871  3.009605979919434