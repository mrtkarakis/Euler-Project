import time
from itertools import permutations

st =time.time()

liste = list()

for i in list(permutations([1,2,3,4,5,6,7,8,9,10])):

    if (i[0]+i[1]+i[2]) == (i[3]+i[2]+i[4]) and (i[0]+i[1]+i[2]) == (i[5]+i[4]+i[6]) and (i[0]+i[1]+i[2]) == (i[7]+i[6]+i[8]) and (i[0]+i[1]+i[2]) == (i[9]+i[8]+i[1]) and (str(i[0])+str(i[1])+str(i[2])) not in liste:

        i = str(i)
        i = i.strip("(")
        i = i.strip(")")
        i = i.split(", ")

        liste.append(i[0]+i[1]+i[2]),liste.append(i[3]+i[2]+i[4]),liste.append(i[5]+i[4]+i[6]),liste.append(i[7]+i[6]+i[8]),liste.append(i[9]+i[8]+i[1])
        liste.append(i[0]+i[1]+i[2]+i[3]+i[2]+i[4]+i[5]+i[4]+i[6]+i[7]+i[6]+i[8]+i[9]+i[8]+i[1])

print(liste[-1])
print(time.time()-st)

#6531031914842725  1.6104213333129883
