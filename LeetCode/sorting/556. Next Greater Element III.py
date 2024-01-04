"""
556. Next Greater Element III
Solved
Medium

Topics

Companies
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        # Checking for the condition if the digits are in decreasing order
        # meaning no solution
        i = len(digits)-1
        while(i>0 and digits[i-1] >= digits[i]):
            i -= 1
        if i == 0:
            return -1

        pivot = i-1

        # When the digits are not in decreasing order, we find the first number
        # where the order is not maintained i.e. i-1
        # Also we find a j from lowest to highest since digits before i are sorted
        j = len(digits)-1
        while j > pivot and digits[j] <= digits[pivot]:
            j -= 1
        # j = bisect.bisect_left(digits[i:], digits[i-1])-1

        # Here we first swap the smallest digit with the (i-1)th
        # And then sort in reverse order to get the min value
        digits[pivot], digits[j] = digits[j], digits[pivot]
        digits[pivot+1:] = digits[pivot+1:][::-1]

        res = int(''.join(digits))

        return res if res<2**31 else -1

        


    
        
