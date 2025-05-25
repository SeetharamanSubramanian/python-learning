from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merge process
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and merge them in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, which starts from the next of the dummy node
        return dummy.next

# Test cases
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper function to print a linked list
    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

    # Test cases
    solution = Solution()
    
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list = solution.mergeTwoLists(list1, list2)
    print_linked_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged_list = solution.mergeTwoLists(list1, list2)
    print_linked_list(merged_list)  # Output: (empty)

    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged_list = solution.mergeTwoLists(list1, list2)
    print_linked_list(merged_list)  # Output: 0