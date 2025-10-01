class Solution:
    def removeDuplicates(self, nums):
        cont = 0
        j = 1
        for i in range (1,len(nums)):          
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j = j + 1                    
            else:
                pass
                cont = cont + 1 

        uniques = len(nums) - cont
        return uniques
    
        
cont = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(cont)