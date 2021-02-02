def isPermutation(s1,s2):

    primes = {'a': 2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,
    'g': 17,'h': 19,'i': 23,'j': 29,'k': 31,'l': 37, 'm': 41,
    'n': 43, 'o': 47,'p': 53,'q': 59, 'r': 61, 's': 67,'t': 71,
    'u': 73,'v': 79,'w': 83,'x': 89,'y': 97,'z': 101 }

    prod1 = 1
    for c in s1:
        prod1*=primes[c]

    prod2 = 1
    for c in s2:
        prod2*=primes[c]

    if prod1 == prod2:
        return True
    else:
        return False


s1 = "hellosw"
s2 = "lloehss"

result = isPermutation(s1,s2)
print(result)