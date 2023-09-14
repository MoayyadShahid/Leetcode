'''
Problem Name: Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 1


My Idea:
The direct way to solve this problem is by starting off with a chosen element and then checking them sum of that selected number 
with other integers in the array. If the target sum has not been found, then you move on and choose the next fixed element, and
then see all the sums that form with the remaining integers with the new chosen integer. This method would require two for-loops,
and that means the time-complexity would be O(n^2) or quadratic.


Test Change
'''

class Solution:
    def twoSum(self, nums: List[nums], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                

