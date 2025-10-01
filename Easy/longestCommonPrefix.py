class Solution:
    def longestCommonPrefix(self, strs):
        firstWord = strs[0]
        commonPrefix = ""
        for i in range(len(firstWord)):
            char = firstWord[i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return commonPrefix
            commonPrefix += char       
        return commonPrefix
common = Solution().longestCommonPrefix(["flower","flow","flood"])
print(common)