class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return len(nums)

        counter = 0

        tmp = nums[0]
        for i in range(1,len(nums),1):

            if nums[i] == tmp:
                nums[i] = None
                counter +=1
            else:
                tmp = nums[i]

        #counter
        x = len(nums)-counter

        #remove Nones
        i = 0
        while(i < len(nums) -1):

            if nums[i] == None:
                nums[i:] = nums[i+1:]
                i-=1

            i+=1




        return x







if __name__ == '__main__':


    nums = [1,1,1,2,3,3,4,5,6,6]
    #Solution().shift_left(nums)
    x = Solution().removeDuplicates(nums)

    print(nums)
    print(x)