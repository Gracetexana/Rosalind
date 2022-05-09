#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

with open(".\\16_original.txt") as f:
    l = list(map(lambda x: x.strip().upper(), f.readlines()[1::2])) #THIS PART NEEDS TO BE FIXED AS THE FILE USES MULTIPLE LINES FOR ONE DNA STRAND
print(l)
positions = list(zip(*l)) #group bases by position in DNA strings
print(positions)
d = {"A":[],
     "C":[],
     "G":[],
     "T":[]}
consensus = ""
for p in positions:
    consensus += max(p, key=p.count)
    d["A"].append(p.count("A"))
    d["C"].append(p.count("C"))
    d["G"].append(p.count("G"))
    d["T"].append(p.count("T"))
print(consensus)
print("A: "+" ".join(map(str,d["A"])))
print("C: "+" ".join(map(str,d["C"])))
print("G: "+" ".join(map(str,d["G"])))
print("T: "+" ".join(map(str,d["T"])))
