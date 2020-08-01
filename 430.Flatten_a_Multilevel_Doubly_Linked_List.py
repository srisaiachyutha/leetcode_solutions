"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        s = []
        cur = head
        while cur or s:
            if cur.child!=None:
                #if there is a child for current node at that time we append it to the stack
                if cur.next:
                    s.append(cur.next)
                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
                cur = cur.next
            else:
                #when ever there is no child for the current node at that time we check stack is empty
                #or not and also the current node next is not None at that time we will pop it and make 
                #it as present node
                if s and not cur.next:
                    cur.next = s.pop()
                    cur.next.prev = cur
                    cur = cur.next
                else :
                    cur = cur.next
        return head