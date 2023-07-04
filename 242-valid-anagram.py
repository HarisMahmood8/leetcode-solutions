class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        total_length = 0
        if len(s) != len(t):
            return False
        for i in s:
            if i in t:
                t = t.replace(i, '',1)
                total_length += 1
        print(total_length)
        if total_length == len(s):
            return True
        else:
            return False
