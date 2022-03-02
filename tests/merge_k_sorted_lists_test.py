from merge_k_sorted_lists.merge_k_sorted_lists import merge_k_sorted_lists, ListNode


def linked_list_from_array(array):
    head = None
    tail = None
    for i in array:
        if not head:
            head = ListNode(val = i)
            tail = head
        else:
            tail.next = ListNode(val = i)
            tail = tail.next

    return head

def array_from_linked_list(head):
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array


def test_example_one():
    # Arrange
    list1 = linked_list_from_array([1, 4, 5])
    list2 = linked_list_from_array([1, 3, 4])
    list3 = linked_list_from_array([2, 6])
    # Act
    answer = merge_k_sorted_lists([list1, list2, list3])

    # Assert
    assert array_from_linked_list(answer) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_example_two():
    # Arrange
    # Act
    answer = merge_k_sorted_lists([])

    # Assert
    assert array_from_linked_list(answer) == []

def test_example_three():
    # Arrange
    list1 = linked_list_from_array([])
    # Act
    answer = merge_k_sorted_lists([list1])

    # Assert
    assert array_from_linked_list(answer) == []
