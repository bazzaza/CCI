def URLify(s,len):
    i = 0
    while(i < len):
        if s[i] == " ":
            j = len-1
            while(j > i):
                s[j],s[j+2] = s[j+2],s[j]
                s[j-1],s[j+1] = s[j+1],s[j-1]
                j = j -2
            s[i],s[i+1],s[i+2] = '%', '2', '0'
            len +=2
            i+=2
        i += 1

def URLify2(s,len):

    mystr = ""

    for i in range(len):
        if s[i] != " ":
            mystr += s[i]
        else:
            mystr += "%20"

    return mystr


s = "I have a cat      "
s = list(s)
len = 12

s = "hello world  "
s = list(s)
len = 11

s = "a b c d e f g hahaha              "
s = list(s)
len = 20

# URLify(s,len)
# print(s)

print(URLify2(s,len))