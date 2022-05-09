t = open(".\\8_original.txt","r").read().replace("T", "U")
#t = t.replace("T", "U")
result = open("8_results","w").write(t).close()
#result.close()