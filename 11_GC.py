f = open(".\\11_original.txt", "r")
d = {"": 0}
x = ""
GC = 0
tot = 0
FASTA = ""
cont = 0

for pos, v in enumerate(f):
    if v.startswith(">"):
        if d[x] > cont:
            FASTA = x
            cont = d[x]
        else:
            pass
        x = v
        GC = 0
        tot = 0
    else:
        GC += v.count("G") + v.count("C")
        tot += len(v.rstrip())
        d[x] = GC / tot
if d[x] > cont:
    FASTA = x
    cont = d[x]
else:
    pass

print(FASTA[1:] + str(cont*100))
f.close()