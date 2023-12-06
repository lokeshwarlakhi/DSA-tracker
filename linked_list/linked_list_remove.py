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
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length ==0:
            self.head = None
            self.tail = None
    
    def pop_first(self):
        temp = self.head
        if self.head is None:
            return None
        self.head= temp.next
        temp.next= None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp.value
# none when it is unsuccessfull returning a node
# false when we are unseccfull to perform the action
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre= self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length-=1
        return temp


myLL = LinkedList(1)
myLL.append(4)
myLL.append(6)
myLL.print_list()

print(myLL.remove(1),"\n")
myLL.print_list()
# print(myLL.get(3))


