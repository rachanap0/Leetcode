# Reversed Linked List

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def reverselist(self):
        if self.head is None:
            return
        
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 

        self.head = prev
      
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data, None)
    
    def add_list(self, list):
        self.head = None
        for data in list:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("The list is empty.")
            return
        
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.val)
            curr = curr.next
        print(llstr)

list1 = LinkedList()
list1.add_list([20,30,34])
list1.print()
list1.reverselist()
list1.print()