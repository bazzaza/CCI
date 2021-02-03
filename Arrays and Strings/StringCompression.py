def compress(s):

    count = 0
    snew = ""
    prev = 0

    for i in range(len(s)):
        if s[i] == prev:
            count+=1
        else:
            if prev:
                snew += prev
                snew += str(count+1)

            prev = s[i]
            count = 0

    snew+=prev
    snew+=str(count+1)


    if len(snew) < len(s):
        return snew
    else:
        return s

s = "aaabbbccccddddAAAaaa"
result = compress(s)
print(result)