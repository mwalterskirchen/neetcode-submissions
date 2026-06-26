class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict: Dict[int, int] = {}
        for num in nums:
            seen = dict.get(num)
            if seen == None:
                dict[num] = 1
            else:
                return True
        return False