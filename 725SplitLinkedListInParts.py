# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        arr = []
        if head == None:
            for i in range(0, k):
                b = ListNode("")
                arr.append(b)
            return arr

        start = head
        head_size = 1
        while head:
            if head.next:
                head_size += 1
                head = head.next
            else:
                break
        
        if head_size / k > 0:
            length = head_size / k
        else:
            length = k
        add = head_size % k
        
        head = start
        if head_size < k:
            while head:
                if head.val >= 0:
                    buffer = head.next
                    head.next = None
                    arr.append(head)
                    head = buffer
                else:
                    break
            lack = k - head_size
            for i in range(0, lack):
                b = ListNode("")
                arr.append(b)
            return arr
        else:
            head = start
            start = head
            count = 0
            cell_add = 0
            l = length
            flag = False
            if add != 0:
                flag = True
            while head:
                if head.val >= 0:
                    count += 1
                    print(count,l, cell_add,add,flag)
                    if count == l + 1 and cell_add != add and flag:
                        buffer = head.next
                        head.next = None
                        head = start
                        arr.append(head)
                        head = buffer
                        start = head
                        cell_add += 1
                        if cell_add == add:
                            flag = False
                        l = l + length + 1
                    elif count == l and cell_add == add and not flag:    
                        buffer = head.next
                        head.next = None
                        head = start
                        arr.append(head)
                        head = buffer
                        start = head
                        l = l + length 
                    else:
                        head = head.next
                else:
                    break

            return arr




        
