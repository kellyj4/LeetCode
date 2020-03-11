#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Example 1:

        Input: 121
        Output: True
    
        Example 2:

        Input: -121
        Output: False

        :type x: int
        :rtype: bool
        """
        comp = str(x)
        compare = comp[::-1]
        
        if x < 0:
            return False
        elif x == int(compare) or x == 0:
            return True

solution = Solution()

print(solution.isPalindrome.__doc__)
print("The input was -121 the output should be false => {0}".format(solution.isPalindrome(-121)))
