class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def prepend(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            node.next = self.head
            self.head = node
        self.length +=1 
        return True


myLL = LinkedList(1)
myLL.append(4)
myLL.print_list()
 
myLL.prepend(3)
myLL.prepend(2)
myLL.print_list()