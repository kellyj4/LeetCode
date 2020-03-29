#!/usr/bin/env python3
import typing 

from enum import IntEnum

class Value:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

class Solution:
    def romanToInt(self, s: str) -> int:
        """
          1. romanToInt
          Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
          Symbol       Value
          ------       -----
          I             1
          V             5
          X             10
          L             50
          C             100
          D             500
          M             1000

          For example, two is written as II in Roman numeral, just two one's added together. Twelve is written
          as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

          Roman numerals are usually written largest to smallest from left to right. However, the numeral for
          four is not IIII. Instead, the number four is written as IV. Because the one is before the five we
          subtract it making four. The same principle applies to the number nine, which is written as IX. There
          are six instances where subtraction is used:
          I can be placed before V (5) and X (10) to make 4 and 9. 
          X can be placed before L (50) and C (100) to make 40 and 90. 
          C can be placed before D (500) and M (1000) to make 400 and 900.
               
          Example 1:
          Input: "III"
          Output: 3
               
          :type s: str
          :rtype: int
        """
        self.s = s

        i = 0
        sum = 0
        while i < len(self.s):
            if i < len(self.s) - 1:
                if self.s[i] == 'I' and self.s[i+1] == 'V':
                    sum += 4
                    i +=2
                    continue
                if self.s[i] == 'I' and self.s[i+1] == 'X':
                    sum += 9
                    i +=2
                    continue
                if self.s[i] == 'X' and self.s[i+1] == 'L':
                    sum += 40
                    i +=2
                    continue
                if self.s[i] == 'X' and self.s[i+1] == 'C':
                    sum += 90
                    i +=2
                    continue
                if self.s[i] == 'C' and self.s[i+1] == 'D':
                    sum += 400
                    i +=2
                    continue
                if self.s[i] == 'C' and self.s[i+1] == 'M':
                    sum += 900
                    i +=2
                    continue

            sum += getattr(Value, self.s[i])
            i += 1
        return sum

def main():
    fred = Solution()
    print(fred.romanToInt.__doc__)
    print("The input is III looking for value of 3 => {0}\n\n".format(fred.romanToInt("III")))

if __name__ == "__main__":
    main()
