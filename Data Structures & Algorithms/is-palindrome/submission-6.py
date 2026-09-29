class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "").lower()
        flag = True
        li = len(st)-1
        fi = 0
        for i in range(len(st)):
            if fi >= li:
                break
            while fi < li and not st[fi].isalnum():
                fi += 1	
            while li > fi and not st[li].isalnum():
                li -= 1
            if st[fi] != st[li]:
                flag = False
                break

            li -= 1
            fi += 1
        return flag