from sys import argv
from listnode import ListNode


# recursive solution
def search_list_rec(list, item):
    """ traverses linked list; returns node if item found, None otherwise """

    if list is None:
        print('The item was not found in the list.')
        return None
    elif list.item == item:
        return list
    else:
        return search_list(list.next, item)


# iterative solution
def search_list_it(list, item):
    """ traverses linked list; returns node if item found, None otherwise """

    while (list is not None):
        if list.item == item:
            return list
        list = list.next

    print('The item was not found in the list.')
    return None


# for use as script
if (__name__ == '__main__'):
    search_list(argv[1], argv[2])
