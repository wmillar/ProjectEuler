def p(n):
    return (3*n*n-n)/2
def isP(n):
    series = int((1+(1+24*n)**.5)/6)
    if p(series)==n:
        return True
    return False

numFound = False
for n1 in xrange(1,3000):
    for n2 in xrange(n1+1,3000):
        p1,p2=p(n1),p(n2)
        pSum = p1+p2
        if isP(pSum):
            pSub = p1-p2
            if pSub < 0:
                pSub = -pSub
            if isP(pSub):
                print pSub
                numFound = True
    if numFound:
        break
