# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

            def merge(l1, l2):
                dummy = ListNode()
                cur = dummy
                while l1 and l2:
                    if l1.val < l2.val:
                        cur.next = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        cur.next = ListNode(l2.val)
                        l2 = l2.next
                    cur = cur.next

                if l1:
                    cur.next = l1
                if l2:
                    cur.next = l2

                return dummy.next

            if not lists:
                return None

            while len(lists) > 1:
                merged = []
                for i in range(0, len(lists), 2):
                    if i + 1 < len(lists):
                        merged.append(merge(lists[i], lists[i+1]))
                    else:
                        merged.append(lists[i])
                lists = merged

            return lists[0]