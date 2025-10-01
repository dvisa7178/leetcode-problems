class Solution:
    def removeElement(self, nums, val):
        j = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                aux = nums[j]
                nums[j] = nums[i]
                nums[i] = aux
                j = j + 1
            else:
                count = count + 1
                pass 
        
        numbersLeft = len(nums) - count
        return numbersLeft
        
        
sol = Solution().removeElement([3,2,2,3],3)
print(sol)