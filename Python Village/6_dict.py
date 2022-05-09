o = open("G:\\My Drive\\PyPractice\\Rosalind\\6_original.txt","r")
r = o.read().split()
d = {}
for i in r:
    if i not in d:
        d[i] = r.count(i)
        print(i,d[i])