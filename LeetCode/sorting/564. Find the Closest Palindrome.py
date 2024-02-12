"""
564. Find the Closest Palindrome
Solved
Hard
Topics
Companies
Hint
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n_int = int(n)
        results = []
        length = len(n)

        if length == 1:
            return str(int(n)-1)

        # cases when the digits overflow / underflow
        results.append(10 ** length + 1)
        results.append(10 ** (length - 1) - 1)


        # cases where we find the closest palidrome by reversing the prefix and prefix-1 and prefix+1
        mid = length // 2
        if length % 2 == 1:
            e = int(n[:mid+1])
            results.append(int( n[:mid]+n[mid]+n[:mid][::-1] ))
            results.append(int( str(e+1)+str(e+1)[::-1][1:] ))
            results.append(int( str(e-1)+str(e-1)[::-1][1:] ))

        else:
            e=int(n[:mid])
            results.append(int( n[:mid]+(n[:mid][::-1] )))
            results.append(int( str(e+1)+str(e+1)[::-1] ))
            results.append(int( str(e-1)+str(e-1)[::-1] ))
        print(results)

        diff=float(inf)
        ans = None
        for res in results:
            if res != n_int and (diff > abs(res-n_int)):
                diff = abs(res-n_int)
                ans = res
            if diff == abs(res-n_int) and res < ans:
                ans = res

        return str(ans)
