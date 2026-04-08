class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = dict()

        for i, num in enumerate(nums):
            difference = target - num
            if difference in numsMap:
                return [numsMap[difference], i]
            numsMap[num] = i