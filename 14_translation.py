#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp)
#Return: The protein string encoded by s.

f = open(".\\14_original.txt")
RNA = f.read(3)
protein = []
while len(RNA) == 3:
    
    #second base U
    if RNA[1] == "U":
        if RNA[0] == "G":
            protein.append("V")
        elif RNA == "AUG":
            protein.append("M")
        elif RNA[0] == "A":
            protein.append("I")
        elif RNA[0] == "C":
            protein.append("L")
        elif RNA[2] in {"A","G"}:
            protein.append("L")
        else: protein.append("F")

    #second base C
    elif RNA[1] == "C":
        if RNA[0] == "G":
            protein.append("A")
        elif RNA[0] == "A":
            protein.append("T")
        elif RNA[0] == "C":
            protein.append("P")
        else: protein.append("S")

    #second base G
    elif RNA[1] == "G":
        if RNA[0] == "G":
            protein.append("G")
        elif RNA[0] == "C":
            protein.append("R")
        elif RNA in {"AGA","AGG"}:
            protein.append("R")
        elif RNA[0] == "A":
            protein.append("S")
        elif RNA == "UGG":
            protein.append("W")
        elif RNA == "UGA":
            protein.append("Stop")
        else: protein.append("C")

    #second base A
    else:
        if RNA[0] == "G":
            if RNA[2] in {"U","C"}:
                protein.append("D")
            else: protein.append("E")
        elif RNA[0] == "A":
            if RNA[2] in {"U","C"}:
                protein.append("N")
            else: protein.append("K")
        elif RNA[0] == "C":
            if RNA[2] in {"U","C"}:
                protein.append("H")
            else: protein.append("Q")
        else:
            if RNA[2] in {"U","C"}:
                protein.append("Y")
            else: protein.append("Stop")

    RNA = f.read(3)

print("".join(protein))
f.close()
