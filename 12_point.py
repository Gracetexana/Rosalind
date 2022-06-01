#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

f = open(".\\12_original.txt")
c = 0
s = f.readline().rstrip()
t = f.readline().rstrip()

for bp in range(len(s)):
    if s[bp] != t[bp]:
        c += 1
    else:
        pass

print(c)
f.close()
