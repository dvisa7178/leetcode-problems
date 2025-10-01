class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        listLefts = []
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            else:
                if target > nums[mid]:
                    left = mid + 1
                    listLefts.append(left)
                    
                else:
                    right = mid - 1    
        print(listLefts)
        result = listLefts[len(listLefts)-1] if nums[0] < target else 0
        return result

sol = Solution().searchInsert([1,3,5,6],0)
print(sol)