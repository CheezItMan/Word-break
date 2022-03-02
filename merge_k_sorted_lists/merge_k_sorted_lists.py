from typing import List, Optional
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for head in lists:
        current = head
        while current:
            heappush(heap, (current.val, current))
            current = current.next

    if (len(heap) == 0):
        return None
    head = heappop(heap)[1]
    tail = head
    while len(heap) > 0:
        popped_tuple = heappop(heap)
        popped_node = popped_tuple[1]
        tail.next = popped_node
        tail = tail.next

    return head
        