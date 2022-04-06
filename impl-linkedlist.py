class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            
            current_node.next = Node(value)
    return head

if __name__ == '__main__':

    input_list = [1,2,3,4,5,6]
    head = create_linked_list(input_list)
    print('finished!!')

