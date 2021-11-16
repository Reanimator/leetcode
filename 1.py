# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for pos, num in enumerate(nums):
            for sum_pos in range(pos+1, len(nums)):
                if nums[pos] + nums[sum_pos] == target:
                    return [pos, sum_pos]


if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(nums=[3, 2, 4], target=6))
    print(Solution().twoSum(nums=[3, 3], target=6))
