#Palindrome Permutation 1.4 CCI

def isPalPerm(s):

    map = {}

    for i in range(len(s)):
        if s[i] != ' ':
            if s[i].lower() in map:
                map[s[i].lower()] += 1
            else:
                map[s[i].lower()] = 1

    odd = 0

    for i in map.values():
        if i%2 == 1:
            odd +=1

    if odd > 1:
        return False

    return True


s = "cattac sf"
result = isPalPerm(s)
print(result)


