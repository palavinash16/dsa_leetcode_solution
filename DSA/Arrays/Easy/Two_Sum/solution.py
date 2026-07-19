class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst=[]
        for i in range(len(nums)):
            for j in range(len(nums)-1):

                if  i !=j and nums[i] +nums[j] == target:
                    lst.extend([i,j])
                    return lst
