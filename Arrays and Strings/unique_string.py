def unique(s):

    mydic = {}

    for i in range(len(s)):
        if s[i] in mydic:
            return False
        else:
            mydic[s[i]]=i
    return True


s = "Helo Word"

result = unique(s)
print(result)