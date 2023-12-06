# DOES NOT HAVE ANY INDEXS
# SPREAD ALL OVER THE PLACE IN MEMORY, NOT ATTACHED TOGETHER
# HEAD AND TAIL ARE THE FIRST AND LAST NODES
# TAIL NODE POINT TO NONE


# O(N) -> TO ACCESS ELEMENTS
# O(1) -> TO ADD AN ELEMENT
# O(N) -> TO REMOVE THE END NODE
# O(1) -> ADD ELEMENT FROM FRONT
# O(1) -> REMOVE ELEMENT FROM FRONT
# O(N) -> ADD IN THE MIDDLE 
# O(N) -> REMOVE IN THE MIDDLE

#  node = value + next pointer
# under the hood it's like a nested dict

# head = {
#     "value":11,
#     "next":{
#         "value": 3,
#         "next":{
#             "value":4,
#             "next":{
#                 "value":7,
#                 "next": None
#             }
#         }
#     }
# }

# ----- SYNTAX -------
class LinkedList:
    def __init__(self, value):
        # create a node
        pass
    def append(self,value):
        # create a node
        # add it the last
        pass
    def prepend(self,value):
        # create a node
        # add it the beginning
        pass
    def insert(self,index,value):
        #create a new node
        # add to the desired index
        pass


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


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)