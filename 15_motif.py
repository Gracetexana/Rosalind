#Given: Two DNA strings s and t (each of length at most 1 kbp).

#Return: All locations of t as a substring of s.

with open(".\\15_original.txt") as f:
    s = f.readline().strip()
    t = f.readline().strip()
l = [0]
while -1 not in l: #find function returns -1 if it does not find a match
    l.append(s.find(t, l[-1]+1))
print(" ".join(list(map(lambda x: str(x+1), l[1:-1]))))