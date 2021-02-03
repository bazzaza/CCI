#One Away 1.5 CCI

def OneAway(a,b):

    def helper(small,big):
        for i in range(len(small)):
            if small[i] != big[i]:
                for j in range(i,len(small),1):
                    if small[i] != big[i+1]:
                        return False
        return True


    if len(a) - len(b) == 1:
        return(helper(small=b,big=a))

    elif len(b) - len(a) == 1:
        return(helper(small=a,big=b))

    elif len(b) == len(a):
        counter = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                counter+=1
                if counter == 2:
                    return False
        return True

    else:
        return False

a = "Pale"
b = "Ple"

a = "Pales"
b = "Pale"

a = "Pale"
b = "bale"

# a = "Pale"
# b = "bake"

result = OneAway(a,b)
print(result)