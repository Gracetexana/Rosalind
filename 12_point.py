#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

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