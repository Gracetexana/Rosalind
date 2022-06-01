#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement sc of s.

s = open(".\\9_original.txt","r").read().strip()
c = ""
for x in s:
    if x == "A":
        c = "T" + c
    elif x == "T":
        c = "A" + c
    elif x == "C":
        c = "G" + c
    else:
        c = "C" + c
print(c)
