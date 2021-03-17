


def linearsearch(numlist,target):
    for i,num in enumerate(numlist):
        if num == target:
            return i
    return -1

def binarysearch(numlist,target,sum=0):
    l = len(numlist)
    if l == 0:
        return -1

    mid = int(l/2)
    if target == numlist[mid]:
        return mid+sum
    elif target > numlist[mid]:
        return binarysearch(numlist[mid+1:],target,sum+len(numlist[0:mid+1]))
    elif target < numlist[mid]:
        return binarysearch(numlist[:mid],target,sum)



if __name__ == "__main__":

    nums = [1,2,4,5,7,9,13]
    target = 13

    index = binarysearch(nums,target)


    if index !=-1:
        print("Target {} found at the {}th index".format(target,index))
    else:
        print("Target not found!")
