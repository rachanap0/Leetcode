#Middle of a linked list

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

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
list1.add_list([20,30,34,27])
list1.print()
middle_node = list1.middle_node()
print(middle_node.val)
