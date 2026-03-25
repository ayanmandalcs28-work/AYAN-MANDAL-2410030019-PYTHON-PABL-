"""Given an array arr[]. The task is to find the largest element and return it.
Examples:
Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90."""

class Solution:
    def largest(self, arr):
        mx = arr[0]
        for x in arr:
            if x > mx:
                mx = x
        return mx

