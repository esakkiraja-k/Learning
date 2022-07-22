from lib2to3.pytree import Node


class node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    
    def append(self,value):
        if self.head is None:
            self.head = node(value)
            return
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node(value)
        
        return

    def to_list(self):
        node_values = []
        node = self.head
        while node:
            node_values.append(node.value)
            node = node.next
        
        return node_values


if __name__ == '__main__':

    input_list = [1,2,3,4,5]
    new_linked_list = linked_list();
    for item in input_list:
        new_linked_list.append(item)
    
    print(new_linked_list.to_list())
    
    


