'''
The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164. Note that
1 = 0^2 + 1^2 has not been included as this problem is concerned with the
squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and
can be written as the sum of consecutive squares.
'''

def isPal(n):
    nStr = str(n)
    return nStr == nStr[::-1]


def getPalindromes(maximum):
    palindromes = set()
    for start in xrange(1, maximum):
        current = pow(start, 2)
        if current * 2 >= maximum:
            break
        for end in xrange(start + 1, maximum):
            result = pow(end, 2)
            if current + result >= maximum:
                break
            current += result
            if isPal(current):
                palindromes.add(current)
    return palindromes


palindromes = getPalindromes(pow(10, 8))
print sum(palindromes)
