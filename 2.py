from re import A


st = str("Объектно-ориентированный")
count = 0
for i in st:
    print (count, " ", i)
    count+=1 
o = st[17]
r = st[16]
t = st[14]
a = st[19]
b = st [1]
e = st [3]
k = st [4]
n = st [20]
w1 = st[16:19]
w2 = st[1] + st [9:11]
w3 = st[6:8]+ st[5] + st [19]
w4 = st[10]+st[19]+st [6]+st [19]
w5 = k + o + t
w6 = t + o + r
w7 = b + a + t + o + n
w8 = r + o + k
w9 = k+o+r+a 
w10 = a+r+k+a

print (w1,w2, w3, w4, w5, w6, w7, w8, w9, w10),