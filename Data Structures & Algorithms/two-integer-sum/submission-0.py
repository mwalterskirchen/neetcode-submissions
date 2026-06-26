class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = set()
        for i in range(len(nums)):
          for j in reversed(range(len(nums))):
            if i != j:
                if nums[i] + nums[j] == target:
                    result.add(i)
                    result.add(j)
        
        return list(result)
