#!/usr/bin/env python3
from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two sum
        Given an array of integers, return indices of the two numbers such that 
        they add up to a specific target. You may assume that each input would 
        have exactly one solution, and you may not use the same element twice.

        Example:

        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1]. 
    
        :type nums: List[int]
        :type target: int
        :rtype: List[int] 
        """

        result = []
        targ = 0
        ind = 0
        
        # If there is a 0 and the target number in the list.
        if target in nums and 0 in nums:
            result.append(nums.index(0))
            if nums.index(0) == nums.index(target):
                nums[nums.index(target)] = 1
                result.append(nums.index(target))
            else:
                result.append(nums.index(target))
            return result    
            
        # Loop through the list till you get the magic combo.
        while ind < (len(nums) - 1):
            targ = target - nums[ind]
            
            if targ in nums[ind+1:]:
                result.append(ind)
                if ind != nums.index(targ):
                    result.append(nums.index(targ))
                else:
                    nums[nums.index(targ)] = targ - 1 
                    result.append(nums.index(targ))
                break
                
            targ = 0 
            ind += 1
                
        return result

fred = Solution()

print(fred.twoSum.__doc__)
print("The inputs are [2,7,11,15] looking for value of 9 => {0}\n\n".format(fred.twoSum([2,7,11,15], 9)))
