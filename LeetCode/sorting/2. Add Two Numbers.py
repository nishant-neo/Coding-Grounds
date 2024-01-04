"""
2. Add Two Numbers
Solved
Medium

Topics

Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        t1, t2, t3 = l1, l2, head

        carry = 0
        while(t1 or t2 or carry>0):
            t1_val = t1.val if t1 else 0
            t2_val = t2.val if t2 else 0
            sum_num = t1_val+t2_val+carry
            remainder = sum_num % 10
            carry = int(sum_num / 10)
            
            t3.next = ListNode(remainder, None)
            t3 = t3.next
            t2 = t2.next if t2 else None
            t1 = t1.next if t1 else None

        

        return head.next

        
