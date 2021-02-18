# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        node = ListNode(head.val)
        
        node.next = head.next
        
        map = {}
        
        map[head] = 0
        
        while(node.next):
            
            node = node.next
            if node in map:
                return node
            map[node] = 0
            
        return None
            
            
        