class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


def CreateLinkedList(lst):
    head = Node(lst.pop(0))
    while len(lst) > 0:
        current_node = head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(lst.pop(0))
    return head


def create_linked_list_better_performance(lst):
    try:
        head = Node(lst.pop(0))
        tail = head

        while len(lst) > 0 :
            tail.next = Node(lst.pop(0))
            tail = tail.next
    except IndexError:
        head = None

    return head


if __name__ == '__main__':
    inputlist = [1,2,3,4,5]
    #print(CreateLinkedList(inputlist))
    print(create_linked_list_better_performance(inputlist))

        



