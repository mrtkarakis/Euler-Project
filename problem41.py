import time
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

for i in range(7654321,333,-1):     #9+8+7+6+5+4+3+2+1 = 45    45%3 = 0 , 8+7+6+5+4+3+2+1 = 36   36%3 = 0 ,7+6+5+4+3+2+1 = 28%3 = 1
    if isPrime(i):
        if len(str(i)) == 9:
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 and str(i).count("4") == 1 and str(i).count("5") == 1 and str(i).count("6") == 1 and str(i).count("7") == 1 and str(i).count("8") == 1 and str(i).count("9") == 1:
                print(i)
                break
            else:
                continue
        elif len(str(i)) == 8 :
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 and str(i).count("4") == 1 and str(i).count("5") == 1 and str(i).count("6") == 1 and str(i).count("7") == 1 and str(i).count("8") == 1 :
                print(i)
                break
            else:
                continue
        elif len(str(i)) == 7 :
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 and str(i).count("4") == 1 and str(i).count("5") == 1 and str(i).count("6") == 1 and str(i).count("7") == 1 :
                print(i)
                break
            else:
                continue
        elif len(str(i)) == 6 :
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 and str(i).count("4") == 1 and str(i).count("5") == 1 and str(i).count("6") == 1 :
                print(i)
                break
            else:
                continue
        elif len(str(i)) == 5 :
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 and str(i).count("4") == 1 and str(i).count("5") == 1 :
                print(i)
                break
            else:
                continue
        elif len(str(i)) == 4 :
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 and str(i).count("4") == 1:
                print(i)
                break
            else:
                continue
        elif len(str(i)) == 3 :
            if str(i).count("1") == 1 and str(i).count("2") == 1 and str(i).count("3") == 1 :
                print(i)
                break
            else:
                continue
    else:
        continue
print(time.time()-st)

# 7652413    0.013965129852294922