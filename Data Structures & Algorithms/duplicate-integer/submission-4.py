class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we loop through the array
        #we check if num at i is already in set if true return true
        #store each into the set

        numSet = set()

        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False
        