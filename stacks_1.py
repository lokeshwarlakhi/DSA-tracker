# O(1) - add or remove from the stack
# O(n) - add or remove from the other end

# we'll use linked list in stacks to make a little challenging
# we'll add or remove elements from the head [ as it takes O(1) to add or remove element from the start of the linked list]
# we'll have 'Top' and 'Bottom' in stacks similar to what we had in linked list as "head" and 'tail"
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    

mys = Stack(4)
mys.print_stack()