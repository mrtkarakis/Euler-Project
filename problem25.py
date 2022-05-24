a = 0
b = 1
c = []
s = "0"
sayac = 0
while True:
    c.clear()
    s = 0
    b+=a
    sayac += 1
    a+=b
    c.append(int(b))
    for i in c:
        s+=i
    s = str(s)
    if len(s) >= 1000:
        break
    else:
        sayac +=1
        s = 0
        c.clear()
        c.append(a)
        for i in c:
            s+=i
        s = str(s)
        if len(s) >=1000:
            break
        else:
            continue
print(sayac)
# 4782      0.0