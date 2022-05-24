import time
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

sayac , i , asal , dongu = 0 , 1 , 1 , 1

while asal/dongu > 0.1 :
            i+=2
            sayac+=1
            dongu+=4

            if isPrime(i**2-(sayac*6)):
                asal+=1

            if isPrime(i**2-(sayac*4)):
                asal+=1

            if isPrime(i**2-(sayac*2)):
                asal+=1

            if sayac==1:
                asal-=1
                dongu-=1

            else:
                pass


print(i)
print(time.time()-st)

#26241     1.7833091640472412