# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0, head)

        # res = head
        max_len = 0
        while head:
            max_len += 1
            head = head.next

        # if max_len == 2 and n == 2:
        #     res.next = res.next.next
        #     return res.next
        # print(res,max_len)
        head = res
        index = 0
        while index < max_len - n:
            head = head.next
            index += 1
        print(index)
        print(head)
        if index == 0:
            head.next = head.next.next
        else:
            head.next = head.next.next
        # print(res)
        # if res.next:
        #     res.next = res.next.next
        # else:
        #     res = None
        # print(res)
        return res.next