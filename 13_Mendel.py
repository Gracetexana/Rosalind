#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

#k as first individual OR second individual results in 100% dominant phenotype
#m by m results in 75% dominant phenotype
#m by n results in 50% dominant phenotype
#n by n results in 0% dominant phenotype

k = int(input("Enter the number of homozygous dominant individuals\n"))
m = int(input("Enter the number of heterozygous individuals\n"))
n = int(input("Enter the number of homozygous recessive individuals\n"))
tot = k + m + n
prob = 2*k/tot + .75*(m/tot)*((m-1)/(tot-1)) + .5*(m/tot)*(n/(tot-1))
print(prob)
