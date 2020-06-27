class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node == None:
            return None
        if node.next_node is not None:
            # node.set_next(node.next_node)
            self.reverse_list(node.get_next(), prev = node)
            # node.set_next(prev)
            print(self.head.value)
        else:
            self.head = node
            node.set_next(prev)
        
        
        




            # iterate through to end of list
            # set the last node as head
            # change pointers
            # set old head.next to none
        
