import sys

class _Node:
    '''
    Creates a Node with two fields:
    1. element (accessed using ._element)
    2. link (accessed using ._link)
    '''
    def __init__(self, element, link):
        '''
        Initializes _element and _link with element and link respectively.
        '''
        self._element = element
        self._link = link

class LinkedList:
    '''
    Consists of member functions to perform different operations on the linked list.
    '''
    def __init__(self):
        '''
        Initializes head, tail and size with None, None, and 0 respectively.
        '''
        self._head = None
        self._tail = None
        self._size = 0

    def len(self):
        '''
        Returns length of linked list.
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if linked list is empty, otherwise False.
        '''
        return self._size == 0

    def addLast(self, e):
        '''
        Adds the passed element at the end of the linked list.
        '''
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest
        self._tail = newest
        self._size += 1

    def addFirst(self, e):
        '''
        Adds the passed element at the beginning of the linked list.
        '''
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._head = newest
        self._size += 1

    def addAnywhere(self, e, index):
        '''
        Adds the passed element at the passed index position of the linked list.
        '''
        if index == 0:
            self.addFirst(e)
        elif index >= self._size:
            self.addLast(e)
        else:
            newest = _Node(e, None)
            p = self._head
            for _ in range(index - 1):
                p = p._link
            newest._link = p._link
            p._link = newest
            self._size += 1
        print(f"Added Item at index {index}!\n\n")

    def removeFirst(self):
        '''
        Removes element from the beginning of the linked list. Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty. Cannot perform deletion operation.")
            return None
        e = self._head._element
        self._head = self._head._link
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e

    def removeLast(self):
        '''
        Removes element from the end of the linked list. Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty. Cannot perform deletion operation.")
            return None
        p = self._head
        if p._link is None:
            e = p._element
            self._head = None
            self._tail = None
        else:
            while p._link._link is not None:
                p = p._link
            e = p._link._element
            p._link = None
            self._tail = p
        self._size -= 1
        return e

    def removeAnywhere(self, index):
        '''
        Removes element from the passed index position of the linked list. Returns the removed element.
        '''
        if index == 0:
            return self.removeFirst()
        elif index == self._size - 1:
            return self.removeLast()
        else:
            p = self._head
            for _ in range(index - 1):
                p = p._link
            e = p._link._element
            p._link = p._link._link
            self._size -= 1
            return e

    def display(self):
        '''
        Utility function to display the linked list.
        '''
        if self.isempty():
            print("Empty")
        else:
            p = self._head
            while p:
                print(p._element, end=' --> ')
                p = p._link
            print("NULL")

    def search(self, key):
        '''
        Searches for the passed element in the linked list. Returns the index position if found, else -1.
        '''
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._link
            index += 1
        return -1

def options():
    '''
    Prints Menu for operations.
    '''
    options_list = [
        'Add Last', 'Add First', 'Add Anywhere',
        'Remove First', 'Remove Last', 'Remove Anywhere',
        'Display List', 'Print Size', 'Search', 'Exit'
    ]
    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')
    choice = int(input("Enter choice: "))
    return choice

def switch_case(choice):
    '''
    Switch Case for operations.
    '''
    if choice == 1:
        elem = int(input("Enter Item: "))
        L.addLast(elem)
        print("Added Item at Last!\n\n")
    elif choice == 2:
        elem = int(input("Enter Item: "))
        L.addFirst(elem)
        print("Added Item at First!\n\n")
    elif choice == 3:
        elem = int(input("Enter Item: "))
        index = int(input("Enter Index: "))
        L.addAnywhere(elem, index)
    elif choice == 4:
        print("Removed Element from First:", L.removeFirst())
    elif choice == 5:
        print("Removed Element from Last:", L.removeLast())
    elif choice == 6:
        index = int(input("Enter Index: "))
        print(f"Removed Item: {L.removeAnywhere(index)} !\n\n")
    elif choice == 7:
        print("List: ", end='')
        L.display()
        print("\n")
    elif choice == 8:
        print("Size:", L.len())
        print("\n")
    elif choice == 9:
        key = int(input("Enter item to search: "))
        index = L.search(key)
        if index >= 0:
            print(f"Item {key} found at index position {index}\n\n")
        else:
            print("Item not in the list\n\n")
    elif choice == 10:
        sys.exit()

if __name__ == '__main__':
    L = LinkedList()
    while True:
        choice = options()
        switch_case(choice)
