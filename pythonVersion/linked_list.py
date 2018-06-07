# coding:utf-8


class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self._next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self._next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self._next = new_next


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert(self,iterm):
        item = Node(item)
        item.set_next(self.head)
        self.head = item
    # O(n)
    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

    # O(n)
    def search(self,item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_data()
        return found

    # O(n)
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        if not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous:
            previous.set_next(current.get_next())
        else:
            self.head = current.get_next()

