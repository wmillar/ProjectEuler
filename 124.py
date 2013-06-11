'''
The radical of n, rad(n), is the product of distinct prime factors of n.
For example, 504 = 2^3 * 3^2 * 7, so rad(504) = 2 * 3 * 7 = 42.

If we calculate rad(n) for 1 <= n <= 10, then sort them on rad(n), and sorting
on n if the radical values are equal, we get:

 Unsorted 	    Sorted
n   rad(n) 	n   rad(n)   k
1     1		1     1	     1
2     2		2     2      2
3     3		4     2	     3
4     2		8     2	     4
5     5		3     3	     5
6     6		9     3	     6
7     7		5     5	     7
8     2		6     6	     8
9     3		7     7	     9
10    10	10    10     10

Let E(k) be the kth element in the sorted n column; for example,
E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 <= n <= 100000, find E(10000).
'''

def getPrimeFactors(n):
    pDict = {1:False, 2:False}
    for i in xrange(3, n, 2):
        if i not in pDict:
            pDict[i] = False
            for i2 in xrange(i*2, n, i):
                if i2 in pDict:
                    if i2 not in pDict[i2]:
                        pDict[i2].append(i)
                else:
                    pDict[i2] = [i]
    for n in xrange(4, n, 2):
        if n in pDict:
            pDict[n] = [2] + pDict[n]
        else:
            pDict[n] = [2]
    return pDict


def multList(L):
    product = 1
    for n in L:
        product *= n
    return product


pFactors = getPrimeFactors(100001)
for n in pFactors:
    if not pFactors[n]:
        pFactors[n] = n
    else:
        pFactors[n] = multList(pFactors[n])

radDict = {}
for n in pFactors:
    result = pFactors[n]
    if result in radDict:
        radDict[result].append(n)
    else:
        radDict[result] = [n]

k = 10000
i = 0
for r in radDict:
    t_i = len(radDict[r])
    if i + t_i > k:
        print radDict[r][k-i-1]
        break
    else:
        i += t_i
