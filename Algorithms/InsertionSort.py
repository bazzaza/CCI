def InsertionSort(a):
    tmp = None

    for i in range(len(a)):
        tmp = a[i]
        for j in range(i):
            if tmp < a[j]:
                while(j<=i): #my mistake was using '<' instead of '<='
                    tmp,a[j] = a[j],tmp
                    j+=1
                break


a = [1,5,2,3,10,0]
InsertionSort(a)
print(a)