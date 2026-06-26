class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map: Dict[str, int] = {}
        t_map: Dict[str, int] = {}

        for char in s:
            seen = s_map.get(char)
            if seen != None:
                s_map[char] = seen + 1
            else:
                s_map[char] = 1

        for char in t:
            seen = t_map.get(char)
            if seen != None:
                t_map[char] = seen + 1
            else:
                t_map[char] = 1

        for key in s_map.keys():
            s_occurences = s_map.get(key)
            t_occurences = t_map.get(key)

            if s_occurences != t_occurences:
                return False

        return True
