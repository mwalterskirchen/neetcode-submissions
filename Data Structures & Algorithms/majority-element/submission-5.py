class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        return max(count, key=lambda k: count[k])


        