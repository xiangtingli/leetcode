ass Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        pfast = head
        pslow = head
        while pfast and pfast.next:
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow:
                return True
        return False


