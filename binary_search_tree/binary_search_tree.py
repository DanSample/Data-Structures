import sys
sys.path.append('../queue')
from the_queue import Queue

sys.path.append('../stack')
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # create node to insert into tree
        new_node = BSTNode(value)

        # check to see if there are existing children
        if self.value:
            if value >= self.value:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(value)
        else:
            self.value = value  
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check to see if the BST is empty
        if self.value:
            # check to see if the target == the self.value
            if target == self.value:
                return True
            # check to see if target is larger or smaller then the self.value
            if target > self.value:
                if not self.right:
                    return False
                return self.right.contains(target)
            else:
                if not self.left:
                    return False
                return self.left.contains(target)                    
        # if there is no value then just return False
        else:
            return False
    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            
            current_node = current_node.right

        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

            if self.left:
                self.left.in_order_print(node)

            print(self.value)

            if self.right:
                self.right.in_order_print(node)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):      
        # make a queue
        new_queue = Queue()
        # # enqueue the node
        new_queue.enqueue(node)
        # # as long as the queue is not empty, dequeue from the front, this is our current node
        while(new_queue.size != 0):
            node = new_queue.dequeue()
            print(node.value) 
            ## enqueue the children for the current node on the queue.
            if node.left:
                new_queue.enqueue(node.left)
            if node.right:
                new_queue.enqueue(node.right)
    # Print the value of every node, starting with the given node,


    # in an iterative depth first traversal
    def dft_print(self, node):
        # make a stack
        new_stack = Stack()
        #push the node onto the stack
        new_stack.push(node)
        #as long as the stack is not empty
        while len(new_stack) != 0:
            ## pop off the stack, this is our current node
            node = new_stack.pop()
            print(node.value)
            ## put the children of the current node on the stack
            if node.left:
                new_stack.push(node.left)
            if node.right:   
                new_stack.push(node.right) 
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

