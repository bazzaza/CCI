def merge_2_sorted_lists(a,b):

    c = []

    i,j=0,0
    while(i < len(a) and j < len(b)):
        if a[i] < b[j]:
            c.append(a[i])
            a = a[1:]

        else:
            c.append(b[j])
            b = b[1:]

    for num in a:
        c.append(num)

    for num in b:
        c.append(num)

    return c

def split_into_2(a):

    mid = int(len(a)/2)

    return a[:mid],a[mid:]

def merge_sort(a):

    if len(a) <= 2:
        a1,a2 = split_into_2(a)
        return merge_2_sorted_lists(a1,a2)

    else:
        a1,a2 = split_into_2(a)
        a1 = merge_sort(a1)
        a2 = merge_sort(a2)
        return merge_2_sorted_lists(a1,a2)

if __name__ == '__main__':

    a = [1,3,3,3,2,2,6,4]

    a = merge_sort(a)

    print(a)
    pass
