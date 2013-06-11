'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

num = 600851475143
i = 3
while num > 1:
    while num % i == 0:
        num /= i
    i += 2
print i-2
