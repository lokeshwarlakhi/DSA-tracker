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

        return temp.value

        # the below code gives an error saying "AttributeError: 'NoneType' object has no attribute 'next'"
        # temp = self.head
        # if temp is None:
        #     return None
        # if temp.next.next is None:
        #     self.head.next = None
        #     self.tail.next = None

        # else:
        #     while (temp.next.next):
        #         temp = temp.next
        #     temp.next = None
        #     self.tail = temp
        # return temp


myLL = LinkedList(1)
myLL.append(4)

myLL.print_list()
 
print(myLL.pop())
print(myLL.pop())
print(myLL.pop())
