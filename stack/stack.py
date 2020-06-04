import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Use the methods from the doubly_linked_list class DoublyLinkedList.
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size = self.size + 1
        self.storage.append(value)

    def pop(self):
        # Error Handling Check to see if there is no length
        if self.size is 0:
            return None
        # If there is length to the Stack
        else:
            # Remove 1 from the size
            self.size -= 1
            # Return the value removed from the head
            return self.storage.pop()


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size = self.size + 1
#         self.storage.add_to_head(value)

#     def pop(self):
#         # Error Handling Check to see if there is no length
#         if self.size is 0:
#             return None
#         # If there is length to the Stack
#         else:
#             # Remove 1 from the size
#             self.size -= 1
#             # Return the value removed from the head
#             return self.storage.remove_from_head()