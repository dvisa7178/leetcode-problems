class Solution:
    def isValid(self, s):
        stack = []
        if s[0] == ")" or s[0] == "]" or s[0] == "}" or len(s) > 10**4:
            return False
        else:
            for i in range (len(s)):
                if s[i] == "(" or s[i] == "[" or s[i] == "{":
                    stack.append(s[i])
                else:
                    if not stack:
                        return False
                    if (s[i] == ")" and stack[-1] == "(") or (s[i] == "}" and stack[-1] == "{") or (s[i] == "]" and stack[-1] == "["):
                        elem = stack.pop()
                    else:
                        return False
            return not stack

sol = Solution().isValid("[({(())}[()])]")
print(sol)