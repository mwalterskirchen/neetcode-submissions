class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            if n in dict:
                value = dict.get(n)
                if value != None:
                    new_value = value + 1
                    dict[n] = new_value
            else:
                dict[n] = 1

        print(dict, max(dict))
        
        return max(dict, key=lambda k: dict[k])


        