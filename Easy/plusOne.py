class Solution:
    def plusOne(self, digits):
        if len(digits) == 1 and digits[0] == 0:
            return [1]
        else:
            elev = len(digits) - 1
            maxSize = 10 ** elev
            element = 0
            for i in range(len(digits)):
                element += (digits[i] * maxSize)
                maxSize = maxSize//10
            element = element + 1
            element = str(element)
            digits = []
            for i in range(len(element)):
                num = int(element[i])
                digits.append(num)
            return digits
            
sol = Solution().plusOne([9])
print(sol)
        