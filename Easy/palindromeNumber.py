class Solution:
    def isPalindrome(self, x):
        x = str(x)
        reverse = ""
        for i in range(len(x)-1,-1,-1):
            reverse = reverse + x[i]
        if(x == reverse):
            return True
        else:
            return False
