# Remove the elements from a linked list that have a specific value.

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #create a dummy node so that the initial node can also be checked for the val.
    def removeElements(self, val):
        dummy = ListNode(0)
        dummy.next = self.head

        curr = dummy

        #while starts at curr.next as curr is the empty node 
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next # as it points the original head
      
    
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
            llstr += str(curr.val) + '->'
            curr = curr.next
        print(llstr)

list1 = LinkedList()
list1.add_list([20,30,34, 27])
list1.print()
list1.removeElements(30)
list1.print()