class Solution:     
    def twoSum(self,nums,target):
        for i in range(len(nums)):           
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    indexes = [i,j]
                    return indexes
                    
indexes = Solution().twoSum([1,4],5)
print(indexes)