def binaryToInt(string):
        maxBits = 2 ** (len(string) - 1)
        converted = 0
        i = 0
        while i < len(string):
            if string[i] == "0":
                converted = converted + (0*maxBits)
                maxBits = maxBits//2
                i = i + 1
            else: 
                converted = converted + (1*maxBits)
                maxBits = maxBits//2
                i = i + 1
        return int(converted)    


class Solution:    
    def addBinary(self, a, b) :
        intA = binaryToInt(a)
        intB = binaryToInt(b)
        intSum = intA + intB
        sum = str(bin(intSum))
        return(sum[2:])
        
sol = Solution().addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011")
print(sol)
