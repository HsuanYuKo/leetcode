# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        ans = ListNode(0)
        a = ans

        while head:
            value = head.val
            head = head.next
            if value not in nums:                
                a.next = ListNode(value)
                a = a.next

        return ans.next


