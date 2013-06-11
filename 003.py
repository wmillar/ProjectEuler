'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def maxFactor(n):
    '''n must be odd'''
    maxFactor = 1
    div = 3
    while n > 1:
        while n % div == 0:
            n /= div
            if div > maxFactor:
                maxFactor = div
        div += 2
    return maxFactor


print maxFactor(600851475143)
