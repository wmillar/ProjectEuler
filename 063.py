'''
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

numFound = 0
for base in xrange(1,11):
    i = 1
    while True:
        result = str(base**i)
        resultLen = len(result)
        if resultLen == i:
            numFound += 1
        else:
            break
        i += 1
print numFound
