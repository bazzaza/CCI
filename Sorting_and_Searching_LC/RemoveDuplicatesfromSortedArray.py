class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return len(nums)

        #2 pointer solution

        i=0

        for j in range(len(nums)):

            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]


        return i+1







if __name__ == '__main__':


    nums = [1,1,1,2,3,3,4,5,6,6]
    #Solution().shift_left(nums)
    x = Solution().removeDuplicates(nums)

    print(nums)
    print(x)