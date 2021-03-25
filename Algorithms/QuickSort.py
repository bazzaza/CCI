
def quicksort(a,start,end):

    length = end - start + 1

    if length > 1:

        pivot = start
        left = start + 1
        right = end
    
        while(left <= right):
    
            while(a[left] <= a[pivot] and left < end):
                left+=1
    
            while(a[right] >= a[pivot] and right > start):
                right-=1

            if(left <= right):
                a[left],a[right] = a[right],a[left]

        a[right],a[pivot] = a[pivot],a[right]

        quicksort(a,start,right-1)
        quicksort(a,right+1,end)








if __name__ == '__main__':

    a = [0]
    print("avant: ")
    print(a)
    quicksort(a,0,len(a)-1)

    print("apres: ")
    print(a)