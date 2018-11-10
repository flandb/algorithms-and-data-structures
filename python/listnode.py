""" ListNode(item, next) class to be used in creating linked lists. """


class ListNode:
    """ item is any value; next is None or another ListNode (pointer) """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
