#Not-complete
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addnum(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        sum = Node()

        num1_last_node = self.head
        num2_last_node = self.head
        while num1_last_node.next and num2_last_node.next:
            num1_last_node = num1_last_node.next
            num2_last_node = num2_last_node.next
        sum = sum + num1_last_node + num2_last_node
        return sum
    
num = LinkedList()
num.addnum([1,2,3],[3,2,1])
print(num)
