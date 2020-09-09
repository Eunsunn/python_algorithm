
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #방법1.
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        head: ListNode = None
        prev: ListNode = None
        node: ListNode = None
        if l1.val < l2.val:
            head = prev = ListNode(l1.val)
            l1 = l1.next
        else:
            head = prev = ListNode(l2.val)
            l2 = l2.next  
        
        while l1 is not None and l2 is not None:
            #l1을 선택한다
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            prev.next = node
            prev = node
        

        #나머지 노드들 이어주기
        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2

        return head
                
        
        # #방법2. 재귀로 이어주기
        # if (not l1) or (l2 and (l1.val > l2.val)):
        #     l1, l2 = l2, l1
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1