"""
Given a string, find the length of the longest substring without repeating
 characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a
substring.
"""

# import itertools
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # This was a bad approach
        """
        # Short circuit the easy case
        testset = ''.join(sorted(set(s), key=list(s).index))
        if testset in s:
            return len(testset)
        for letter in range(len(testset)):
            perms = itertools.permutations(
                list(testset), len(testset) - letter
                )
            for perm in perms:
                if ''.join(perm) in s:
                    return len(perm)
        """

        # This is better, but still too slow...
        """
        substrs =  sorted(
            list(
                s[start:end]
                for start in (i for i,_ in enumerate(s))
                for end in (i for i,_ in enumerate(s[start:], start+1))
            ), key=len, reverse=True)

        for key in substrs:
            if key == ''.join(sorted(set(key), key=list(key).index)):
                return len(key)
        else:
            return 0
        """

        # I gave up on scanning permutations of the set. That was kinda dumb.
        # It is much more efficient to just check valid substrings.

        # check if the full _set_ of input is a substring of the full string
        testset = ''.join(sorted(set(s), key=list(s).index))
        if testset in s:
            return len(testset)

        # Start with the largest substring, slowly shrinking the size of our
        # substring
        for i in reversed(range(len(s))):
            # start with a window of len(i) on the left edge of the input
            # string, slide window to the right until we find a fully unique
            # substring
            for j in range(len(s) - (i) + 1):
                # check if it is fully unique by comparing the length of our
                # substring to the length of the set of unique characters in
                # our substring.
                if len(s[j:j+i]) == len(set(s[j:j+i])):
                    # When we hit a match, return our slice.
                    return len(s[j:j+i])
