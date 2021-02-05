def RotateString(A,B):

    if len(A) != len(B):
        return False

    if len(A) < 2:
        return True

    letters_map = {'a': 2,
                  'b': 3,
                  'c': 5,
                  'd': 7,
                  'e': 11,
                  'f': 13,
                  'g': 17,
                  'h': 19,
                  'i': 23,
                  'j': 29,
                  'k': 31,
                  'l': 37,
                  'm': 41,
                  'n': 43,
                  'o': 47,
                  'p': 53,
                  'q': 59,
                  'r': 61,
                  's': 67,
                  't': 71,
                  'u': 73,
                  'v': 79,
                  'w': 83,
                  'x': 89,
                  'y': 97,
                  'z': 101
                 }

    prod_1, prod_2 = 1,1

    for i in range(len(A)):
        prod_1 *= letters_map.get(A[i])
        prod_2 *= letters_map.get(B[i])


    if prod_1 != prod_2:
        return False

    #Now we know both are same length and both have same characters

    temp = ""

    for i in range(len(A)):
        temp = A[1:]
        temp = temp + A[0]
        if temp == B:
            return True
        A = temp

    return False



s1 = ""
s2 = ""

result = RotateString(s1,s2)
print(result)