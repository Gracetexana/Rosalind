o = open("G:\\My Drive\\PyPractice\\Rosalind\\5_original.txt", "r")
n = open("G:\\My Drive\\PyPractice\\Rosalind\\results.txt", "w")
i = 1
for line in o:
    if i % 2 == 0:
        n.write(line)
    i += 1
n.close()
