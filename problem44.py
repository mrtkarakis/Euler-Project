import time
st = time.time()

def pentagonal(x):
    if (1+(24*x+1)**0.5) % 6 == 0:
        return True
    return False
def penta(x):
    return x*(3*x-1)/2
counter = 0
for i in range(1,2500):
    for j in range(1,i):
        if pentagonal(penta(i)+penta(j)) and pentagonal(penta(i)-penta(j)):
            print(penta(i)-penta(j))
            counter+=1
            break
    if counter==1:
        break

print(time.time()-st)

# 5482660  1.9814738273620605

counter = 0
sayi = 1
pentagonal = []
for i in range(1,2600):

    pentagonal.append(sayi)
    liste = []
    for x in range(((i-1)*3)+1,sayi-((i-1)*3)):
        s2 = 0
        for q in range(((i-1)*3)+1,4,-3):
            s2+=q
            if s2 < ((i-1)*(3*(i-1)-1)/2)//2+1 and s2 != sayi/2:
                liste.append(s2)
                continue
            elif ((i-1)*(3*(i-1)-1)/2) < s2:
                break
        break

    for j in liste:
        if j in pentagonal and j*2 in liste:
            print(abs(sayi-2*j))
            counter+=1
            break
    if counter == 1:
        break

    sayi += (i*3)+1
print(time.time()-st)

#5482660  17.157

