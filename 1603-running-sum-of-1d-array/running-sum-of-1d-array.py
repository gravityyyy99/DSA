class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            # Add the value of the previous element to the current element
            nums[i] += nums[i - 1]
            
        return nums