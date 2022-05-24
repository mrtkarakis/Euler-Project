import time
st = time.time()
def isPrime(sayi):
    for i in range(2, int(sayi ** 0.5) + 2):
        if sayi % i == 0:
            return False
    return True


def isPrimeS(sayi):
    for i in range(2, sayi // 2 + 1):
        if sayi % i == 0:
            return False
    return True


a = int(input("En büyük asal böleni bulunacak sayıyı giriniz : "))
if a < 100000:
    if a == 4:
        iki = 2
        print(iki)
    else:
        y = int(a // 2)
        b = []

        for i in range(2, y):
            if a % i == 0 and isPrimeS(i):
                b.append(i)
        try:
            print(b[-1])
        except:
            print(a)
else:
    y = int(a ** 0.5) + 2
    b = []

    for i in range(2, y):
        if a % i == 0 and isPrime(i):
            b.append(i)
    try:
        print(b[-1])
    except:
        print(a)

print(time.time()-st)
print("***********pratik çözümü*****************")


import time
ss= time.time()

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    if i ==2:
        i+=1
    else:
        i +=2
print(int(n))
print(time.time()-ss)

# 6857    0.11268901824951172   0.0
