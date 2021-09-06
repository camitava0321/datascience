def getprimes(N=100):
    result=[]
    for n in range(N,N+100):
        for x in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,53,57,59,61,67,71,73,79,83,89,91,93,97]:
            if n%x==0:
                #print n, '-->',x,' * ',n/x
                break
        else:
            result.append(n)
    return result