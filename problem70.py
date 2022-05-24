import time
from itertools import permutations
st =time.time()
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

for i in range(87109,87110):
    nispeten = set()
    bolensayilar = set()
    if not isPrime(i):
        for q in range(2,int(i**0.5)+2):
            if i%q == 0:
                bolensayilar.add(q)
                for l in range(2,i//q):
                    bolensayilar.add(q*l)
        for z in range(1,i):
            if z not in bolensayilar:
                nispeten.add(z)
    else:
        for z in range(1,i):
            if z not in bolensayilar:
                nispeten.add(z)

    if len(i) == 5:
        for t in list(permutations(str(i))):
            if t in nispeten:
                print(i,int(t[0]+t[1]+t[2]+t[3]+t[4])