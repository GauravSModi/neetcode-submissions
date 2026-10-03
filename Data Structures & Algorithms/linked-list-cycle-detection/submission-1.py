# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
# O(n) runtime, O(n) space
# Uses hashset to keep track of seen nodes
        # curr = head
        # seen = set()
        
        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        
        # return False

# O(n) runtime, O(1) space
# One pointer is fast, one is slow. If there's a cycle, they'll be equal somewhere
# surprisingly faster than the first method, and uses constant memory

        slow, fast = head, head.next

        while fast:
            if slow == fast:
                return True
            
            slow = slow.next


            if fast.next != None:
                fast = fast.next.next
            else:
                return False
            
        return False
