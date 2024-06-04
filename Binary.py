class Solution:
    def binaryNextNumber(self, s):
        # Reverse the string
        s = s[::-1]
        carry = 1
        s = list(s)
        
        for i in range(len(s)):
            if carry == 1:
                if s[i] == '0':
                    s[i] = '1'
                    carry = 0
                else:
                    s[i] = '0'
            else:
                break
        
        if carry:
            s.append('1')
        
        # Reverse the string back
        s = s[::-1]
        
        # Convert list back to string
        s = ''.join(s)
        
        # Remove leading zeros
        s = s.lstrip('0')
        
        return s

# Example usage:
# sol = Solution()
# print(sol.binaryNextNumber("110"))  # Output: "111"
