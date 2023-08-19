# https://leetcode.com/problems/add-two-numbers/?envType=featured-list&envId=top-interview-questions

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Are there numbers to combine?
        if not l1 and not l2:  # No numbers left, end loop.
            return None

        elif not l1:  # Number on l2, save it and continue.
            save_num = l2.val % 10
            remember_num = save_num // 10
            l2 = l2.next
            return ListNode(save_num, self.addTwoNumbers(l1, l2))

        elif not l2:  # Number on l1, save it and continue.
            save_num = l1.val % 10
            remember_num = save_num // 10
            l1 = l1.next
            return ListNode(save_num, self.addTwoNumbers(l1, l2))

        # Addition of numbers, splitting the answer into 2 -
        num = l1.val + l2.val
        save_num = num % 10  # The number to be saved in the node
        remember_num = num // 10  # The number to be sent to the next node "carrying"

        # Numbers used, move nodes to next values.
        l1 = l1.next
        l2 = l2.next

        # Who is going to carry the number?

        # if both nodes are None, make the carry the next value and end the loop.
        if not l1 and not l2:
            return ListNode(save_num, ListNode(remember_num, None))
        # l2 has a value, use it to carry the number.
        elif not l1:
            l2.val = l2.val + remember_num
            return ListNode(save_num, self.addTwoNumbers(l1, l2))
        # l1 has a value, use it to carry the number.
        elif not l2:
            l1.val = l1.val + remember_num
            return ListNode(save_num, self.addTwoNumbers(l1, l2))
        # Both have a value, l1 has been selected to carry.
        else:
            l1.val = l1.val + remember_num
            return ListNode(save_num, self.addTwoNumbers(l1, l2))



ln1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3)))) # 321
ln2 = ListNode(2, ListNode(3, ListNode(4))) # 432
# 321 + 432 = 753

ln3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))  # 9,999,999
ln4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))  # 999
# 9,999,999 + 999 = 10,009,998

s = Solution()
test1 = s.addTwoNumbers(ln1, ln2)
test2 = s.addTwoNumbers(ln3, ln4)

print()