'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
the 938th name in the list. So, COLIN would obtain a score
of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


with open('names.txt', 'r') as f:
    names = sorted(map(lambda x: x[1:-1], f.read().split(',')))

    #print sum(map(lambda y: y[0]*y[1], list(enumerate(map(lambda y: sum(map(lambda y: alphabet.index(y)+1, y)), names), 1))))

    total, i = 0, 1
    for n in names:
        total += sum(map(lambda x: alphabet.index(x)+1, n))*i
        i += 1
    print total
