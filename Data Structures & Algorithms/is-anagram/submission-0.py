class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = [0]*26
        for i in s:
            char_count[ord(i)-ord('a')] += 1
        for j in t:
            char_count[ord(j)-ord('a')] -= 1
            if char_count[ord(j)-ord('a')] < 0:
                return False
        return True