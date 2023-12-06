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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index== self.length:
            return self.append(value)
        else:
            node = Node(value)
            temp = self.get(index-1)
            node.next = temp.next
            temp.next = node
        self.length+=1
        return True



myLL = LinkedList(0)
myLL.append(2)
myLL.insert(1,69)
myLL.print_list()

