class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first= new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

myq= Queue(30)
myq.print_queue()