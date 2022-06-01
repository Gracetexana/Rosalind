#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.

t = open(".\\08_original.txt","r").read().replace("T", "U")
result = open("08_results","w").write(t).close()
