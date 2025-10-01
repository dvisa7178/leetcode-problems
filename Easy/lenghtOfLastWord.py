class Solution:
    def lengthOfLastWord(self, s):
        if " " not in s:
            return len(s)
        else:
            lenghtLast = 1
            i = len(s)-1
            while s[i] == " ":
                i = i - 1
            s = s[0:i]
            i = len(s)-1
            while i >= 0:
                if s[i] == " ":
                    break
                else:
                    lenghtLast = lenghtLast + 1
                    i = i - 1               
            return lenghtLast
                        
sol = Solution().lengthOfLastWord("   fly me   to   the moon  ")
print(sol)
