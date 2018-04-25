class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSet = set(nums)
        return (len(numsSet) != len(nums))