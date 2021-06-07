# Definition for singly-linked list.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None

        h = []
        for l in lists:
            if l:
                heappush(h, (l.val, id(l), l))

        head = node = ListNode()
        while len(h) > 0:
            val, node_id, l = heappop(h)
            node.next = ListNode(val)
            node = node.next
            if l.next:
                l = l.next
                heappush(h, (l.val, id(l), l))

        return head.next