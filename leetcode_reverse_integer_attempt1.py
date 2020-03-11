#!/usr/bin/env python3

class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a 32-bit signed integer, reverse digits of an integer.
        
        Example 1:
        Input: 123
        Output: 321
        
        :type x: int
        :rtype: int
        """
        convert_int = ""
        result = -1
        
        if x == 0:
            return x
        elif x < 0:
            convert_int = str(abs(x))
            result = (int(convert_int[::-1]) * -1)
            if result < 2**31 * -1:
                return 0
            else:
                return result
            
        elif x > 0:
            convert_int = str(x)
            result = int(convert_int[::-1])
            
            if result > 2**31 - 1:
                return 0
            else:
                return result

solution = Solution()

print(solution.reverse.__doc__)
print("Inputting -321, expecting -123 => {0}".format(solution.reverse(-321)))
