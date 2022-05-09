a = 4028
b = 8089
i = 0
while a <= b:
    if a % 2 == 1:
        i += a
    a += 1
print(i)