class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head        
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        return


dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)

node = dlist.head
print('read from head')

while(node):
    print(node.value)
    node = node.next

print('read start from head end ---')    


node = dlist.tail
print('read from tail')

while(node):
    print(node.value)
    node = node.previous
    
print('read from tail end ---')    



