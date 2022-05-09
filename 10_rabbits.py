from re import M


n = 36
k = 3

m = 0
f = 0
l = 1
t = 1
for x in range(0, n):
    f = m * k
    t = m + l
    m += l
    l = f
print(t)