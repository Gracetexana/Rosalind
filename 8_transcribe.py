#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.

t = open(".\\8_original.txt","r").read().replace("T", "U")
#t = t.replace("T", "U")
result = open("8_results","w").write(t).close()
#result.close()
