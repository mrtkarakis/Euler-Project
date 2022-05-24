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

primes = [2]

for i in range(3,1001,2):
    if isPrime(i):
        primes.append(i)
one = []
for i in primes:
    for x in primes:
        if isPrime(int(str(i)+str(x))) and isPrime(int(str(x)+str(i))):
            one.append((i,x))
two=one.copy()
four = []
for i in range(len(one)):
    for x in range(i+1,len(one)):
        if one[i][0]!= two[x][0] and one[i][0]!= two[x][1] and one[i][1]!= two[x][0] and one[i][1]!= two[x][1] and isPrime(int(str(one[i][0])+str(two[x][0]))) and isPrime(int(str(two[x][0])+str(one[i][0]))) and isPrime(int(str(one[i][1])+str(two[x][0]))) and isPrime(int(str(two[x][0])+str(one[i][1]))) and isPrime(int(str(one[i][1])+str(two[x][1]))) and isPrime(int(str(two[x][1])+str(one[i][1]))):
            four.append((one[i][0],one[i][1],two[x][0],two[x][1]))
f = []
print(len(f))
for i in range(len(four)):
    for x in primes:


        if x!=four[i][0] and x!=four[i][1] and x!=four[i][2] and x!=four[i][3] and isPrime(int(str(x)+str(four[i][0]))) and isPrime(int(str(four[i][0])+str(x))) and isPrime(int(str(x)+str(four[i][1]))) and isPrime(int(str(four[i][1])+str(x))) and isPrime(int(str(x)+str(four[i][2]))) and isPrime(int(str(four[i][2])+str(x))) and isPrime(int(str(x)+str(four[i][3]))) and isPrime(int(str(four[i][3])+str(x))):
            print(f"x {x}  f0 {four[i][0]}   f1 {four[i][1]}   f2 {four[i][2]}   f3 {four[i][3]}")
            f.append((x,four[i][0],four[i][1],four[i][2],four[i][3]))
print(f)