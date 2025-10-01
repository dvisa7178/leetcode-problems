class Solution:
    def strStr(self, haystack, needle):
        indexes = []
        if needle not in haystack:
            return -1
        else:
            i = 0
            j = 0
            startPos = 0
            while j < len(needle) and i < len(haystack):
                if haystack[i] != needle[j]:
                    startPos = startPos + 1
                    j = 0
                    i = startPos
                    pass
                else:
                    if j == 0:
                        indexes.append(i)
                        startPos = i     
                    j = j + 1
                    i = i + 1
            return indexes[-1]
            
sol = Solution().strStr("leetcode","leetio")
print(sol)
                
                    
                    

                    
                

