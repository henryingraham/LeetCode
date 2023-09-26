# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize  one temp node and mark it as prev node
        prev = tempHead = ListNode(0, next = head)
        # check the next node and next next node exist

        while prev.next and prev.next.next:
            # get the next node and next next node exist
            first = prev.next
            second = prev.next.next
            # set first.next to second.next, point to next node pair
            first.next = second.next
            # set second.next to first, perform the swap
            second.next = first
            # set prev.next to second, point to current node pair
            prev.next = second
            # set prev to first, set prev to node previous to next node pair
            prev = first

        return tempHead.next