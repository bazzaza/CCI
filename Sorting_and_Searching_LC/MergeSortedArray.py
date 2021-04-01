#LeetCode Question 88
#Frequency ~70%

#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

#Constraints
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[i] <= 109

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

#Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

#Difficulty: Easy

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        #First we cover the edge cases
        if m == 0:
            nums1[:] = nums2[:]
            return None

        if n == 0:
            return None

        numst = [0 for i in range(m)]
        numst[:] = nums1[0:m]

        i,j,pos=0,0,0

        while(i<m and j <n):

            if numst[i] < nums2[j]:
                nums1[pos] = numst[i]
                i+=1

            else:
                nums1[pos] = nums2[j]
                j+=1

            pos+=1

        if i==m:
            while(pos < m+n):
                nums1[pos] = nums2[j]
                j+=1
                pos+=1

        else:
            while(pos <m+n):
                nums1[pos] = numst[i]
                i+=1
                pos+=1

        return None









if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3



    Solution().merge(nums1,m,nums2,n)

    print(nums1)