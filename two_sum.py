"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # First try, passes
        """
        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums[index+1:]):
                if num + num2 == target:
                    return [index, index+index2+1]
        """

        # I think I can get better performance here...
        """
        # sort list so we can short circuit more easily
        sortnums = sorted(nums)
        # track if we have a mix of +/- ints in our list, as that can
        # make things trickier and will break our optimizations
        mix_pos_neg = any(n < 0 for n in sortnums)
        
        # This is a non-pythonic method of iterating over the list, but
        # `pop`ing can interfere with other iteration methods, so it is
        # a bit safer in this case.
        for i in range(len(sortnums)):
            # pop because we never want to check this number again
            # start from the end of the list (so pulling larger numbers)
            num1 = sortnums.pop(-1)
            # Short circuit if our number is already bigger than the taget
            # This works well if the whole list is positive, but breaks down
            # for a mix of positive and negative ints.
            if num1 > target and not mix_pos_neg:
                continue
            # Start our second iterator from 
            for num2 in sortnums:
                # Short circuit if our outer number + our smallest number is
                # already greater than our target. This again can behave oddly
                # for mixed positive/negative lists
                if num1 + num2 > target and not mix_pos_neg:
                    break
                # success case, look up the indeces for the solution we found
                # in the original list
                elif num1 + num2 == target:
                    # normal success case
                    if num1 != num2:
                        return [nums.index(num1), nums.index(num2)]
                    # have to handle the case where our numbers are the same,
                    # otherwise we will pull the same index twice, which violates
                    # the "you may not use the same element twice" rule
                    else:
                        index1 = nums.index(num1)
                        index2 = nums.index(num2, index1+1)
                        return [index1, index2].sort()
        """
        # Worst case is still the same (slightly worse because of the sorting and
        # index lookup, but average case is significantly better due to the early
        # branch exits

        # Let's try something else...
        for index, num in enumerate(nums):
            # instead of checking every item in the list, why not just check if
            # the list contains the difference between our current number and the
            # target?
            if (target - num) in nums[index + 1:]:
                return [index, nums.index(target - num, index + 1)]
        # BOOM! That's the one. Much less code (and therefore fewer bugs, right?),
        # plus the runtime should be roughly O(n)


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([-3, 4, 3, 90], 0))
