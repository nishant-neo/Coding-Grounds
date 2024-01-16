"""
227. Basic Calculator II
Solved
Medium
Topics
Companies
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        sign = '+'
        num = 0
        stack = []
        for i, ch in enumerate(s):
            print(i, ch)
            # if ch == ' ':
            #     continue
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            if (not ch.isdigit() and ch != ' ' ) or i == n-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = ch
                num = 0
        # print(stack)

        return sum(stack)


        # s = s.strip()
        # s_ = ""
        # flag = False
        # for ch in s:
        #     if not ch.isnumeric():
        #         flag = True

        #     if ch != ' ':
        #         s_ = s_ + ch
        # if not flag:
        #     return int(s)

        # idx = len(s_)-1
        # value_so_far = 0
        # while(idx>=0):
        #     if s_[idx].isnumeric():
        #         value_so_far = value_so_far*10+int(s_[idx])
        #         idx -= 1
        #     else:
        #         break

        # print(value_so_far)
            

        # while(idx>=0):
        #     op = s_[idx]
        #     a = 0
        #     idx -= 1
        #     while(idx>=0):
        #         if s_[idx].isnumeric():
        #             a = a*10+int(s_[idx])
        #         else:
        #             break

        #     # if s_[idx].isnumeric():
        #     #     num = num*10+int(s_[idx])

        #     # a = int(s_[idx-1])
        #     if op == '*':     
        #         value_so_far = a*value_so_far
        #     elif op == '/':
        #         value_so_far = a//value_so_far
        #     elif op == '-':
        #         value_so_far = a-value_so_far
        #     else:
        #         value_so_far = a+value_so_far
            

        # print(value_so_far)
        return value_so_far
        
