# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,root):
        len = 0
        while root:
            len+=1
            root = root.next
        return len
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = root
        l = self.length(l)
        #print(l)
        ans = []
        head = root
        if l<k:
            #here we will perform when the length of the linkedlist is less than the specified k value
            while head:
                ans.append(head)
                
                head = head.next
                ans[-1].next = None
            for i in range(k-l):
                ans.append(None)
            return ans
        elif l%k >0:
            #suppose when the modular division of length of the linkedlist greater than zero means we cannot give all the linked list to have the same number of elements
            #first l%k linked lists will contain " 1 " elemenent extra than the remaining linked lists
            m = l%k
            tm = l//k+1
            
            
            for ls in range(m):
                c=1
                ans.append(head)
                while c!=tm:
                    head = head.next
                    c+=1
                y = head
                head = head.next
                y.next = None
            tm-=1
            #this is to perform because the remaining linkedlist elements will have length of one unit less than the previous length
            
            l-=m#here we are making the length to be divisible by k
        if l%k ==0:
            #here when the length of linkedlist can be equally divisible by k or when we modular division is greater and after that we make the length modify such that it is divisible by k after making the l%k linkedlists
            start ,last = head,head
            count = 1
            
            c = l//k
            while last:
                if count == c:
                    
                    m = last.next
                    ans.append(start)
                    last.next = None
                    start ,last = m ,m
                    count =1
                else:
                    count+=1
                    last = last.next
        return ans