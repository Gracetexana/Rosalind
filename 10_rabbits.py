#Given: Positive integers n≤40 and k≤5.
#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n = 36
k = 3

m = 0
f = 0
l = 1
t = 1
for x in range(0, n):
    f = m * k
    t = m + l
    m += l
    l = f
print(t)
