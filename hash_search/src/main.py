# 자료구조개론 9주차 과제7
# hash와 linked list를 이용한 검색 구현
#
# 미래모빌리티학과
# 2021271402 이지오

# <전제 1> 임의의 정수 1만개가 있다.
# <조건 1> bucket을 97개 만든다. (하필이면 97인가?)
# <조건 2> 각각의 bucket에 1만개의 정수를 linked list로 위치 시킨다.
# <조건 3> 임의의 숫자가 몇 번째 bucket의 몇 번째 linked list에 위치하는지 출력
# 없다면 “not found” 출력

# True : print debug message
DEBUG = False   


# module containing
import sys      # for call main function
import random   # for create random data


# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
     
class LinkedList:
    def __init__(self, iterable_data = None):
        self.clear()
        if iterable_data:
            self.extend(iterable_data)
            
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def __len__(self) -> int:
        return self._len
    
    def __iter__(self):
        pass
    
    def __next__(self):
        pass
    
    # Add an item to the end of the linked list.
    def append(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._len += 1
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._len += 1
            
    # Extend the linked list by appending all the items from the iterable.
    def extend(self, iterable_data):
        for data in iterable_data:
            self.append(data)
    
    # Insert an item at a given position. 
    # The first argument is the index of the element before which to insert, 
    # so a.insert(0, x) inserts at the front of the linked list, 
    # and a.insert(len(a), x) is equivalent to a.append(x).
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self._head
            self._head = new_node
            self._len += 1
        else:
            node = self._head
            for _ in range(index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
            self._len += 1
    
    # Remove the first item from the list whose value is equal to x. 
    # It raises a ValueError if there is no such item.
    def remove(self, data):
        pass
    #     if self._head.data == data:
    #         self._head = self._head.next
    #         self._count -= 1
    #     else:
    #         node = self._head
    #         while node.next.data != data:
    #             node = node.next
    #         if node.data != data:
    #             raise ValueError(f"{data} is not in linked list.")
    #         if node.next == None:
    #         node.next = node.next.next
    #         self._count -= 1
    
    # Remove the item at the given position in the list, and return it. 
    # If no index is specified, a.pop() removes and returns the last item in the list. 
    # (The square brackets around the i in the method signature denote that the parameter is optional, 
    # not that you should type square brackets at that position. 
    # You will see this notation frequently in the Python Library Reference.)
    def pop(self, index = None):
        pass
    
    # Remove all items from the linked list.
    def clear(self):
        self._head = None
        self._tail = None
        self._len = 0
        
    # Return zero-based index in the list of the first item whose value is equal to x. 
    # Raises a ValueError if there is no such item.
    # The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. 
    # The returned index is computed relative to the beginning of the full sequence rather than the start argument.
    def index(self, data, start = None, end = None):
        pass
    #     if start == None:
    #         start = 0
    #     if end == None:
    #         end = self._count
    #     node = self._head
    #     for _ in range(start, end):
    #         if node.data == data:
    #             return _
    #         node = node.next
    #     raise ValueError(f"{data} is not in linked list."
    
    # Return the number of times x appears in the list.
    def count(self, data):
        pass

# Create data for sort
def create_random_data(size:int = 10000) -> LinkedList:
    linked_list = LinkedList()
    return [random.randint() for _ in range(size)]


# define main function
def main(*args, **kwargs) -> int:
    return 0


# call main function
if __name__ == '__main__':
    sys.exit(main())