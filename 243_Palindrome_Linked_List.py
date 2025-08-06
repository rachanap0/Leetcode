class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def isPalindrome(self):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
    
        slow = self.head
        fast = self.head

        #slow will stop at the midpoint
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next

        # the part from slow is to be reversed
        prev = 0
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # compairing the reversed part after the slow vs the first half
        left = self.head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.val)
            curr = curr.next
        print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            node = ListNode(data, None)
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data, None)


    def add_list(self, list):
        self.head = None
        for data in list:
            self.insert_at_end(data)


List1 = LinkedList()
List1.add_list([1,2,2,1,2,2,1])
List1.print()  
isPalindrome = List1.isPalindrome()
print(isPalindrome)

        
