# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

totalSum = 0L
i = 1
while i <= 1000:
    totalSum += i**i
    i += 1
print str(totalSum)[len(str(totalSum))-10:]
