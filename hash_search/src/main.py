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
from typing import Any, Iterable, SupportsIndex, Optional, Tuple, List
import sys      # for call main function
import random   # for create random data

# Linked List
class Node:
    def __init__(self, __object:Any):
        self.data = __object
        self.next = None
     
class LinkedList:
    def __init__(self, __iterable:Iterable = None):
        '''Built-in mutable sequence.

        If no argument is given, the constructor creates a new empty linked list. The argument must be an iterable if specified.'''
        self.clear()
        if __iterable:
            self.extend(__iterable)
            
    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return "[" + ", ".join(str(data) for data in self) + "]"
        
    def __len__(self) -> int:
        '''Return len(self).'''
        return self._len
    
    def __iter__(self):
        '''Implement iter(self).'''
        node = self._head
        while node:
            yield node.data
            node = node.next
            
    def __getitem__(self, __index:SupportsIndex):
        if __index < 0:
            __index += self._len
        if __index < 0 or __index >= self._len:
            raise IndexError("linked list index out of range")
        else:
            node = self._head
            for _ in range(__index):
                node = node.next
        return node.data

    
    def append(self, __object:Any, /):
        '''Add an item to the end of the linked list.'''
        new_node = Node(__object)
        if not self._head:
            self._head = new_node
            self._tail = new_node
            self._len += 1
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._len += 1
            
    
    def extend(self, __iterable:Iterable, /):
        '''Extend the linked list by appending all the items from the iterable.'''
        for one in __iterable:
            self.append(one)
    
    def insert(self, __index:SupportsIndex, __object:Any, /):
        '''Insert object before index.'''
        if __index < 0:
            __index += self._len
        if __index < 0 or __index >= self._len:
            raise IndexError("insert index out of range")
        new_node = Node(__object)
        if __index == 0:
            new_node.next = self._head
            self._head = new_node
            self._len += 1
        else:
            node = self._head
            for _ in range(__index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
            self._len += 1
    
    def remove(self, __value:Any, /):
        '''Remove first occurrence of value.

        Raises ValueError if the value is not present.'''
        if self._head.data == __value:
            if self._tail == self._head:
                self._tail = None
            self._head = self._head.next
            self._len -= 1
        else:
            node = self._head
            while node.next:
                if node.next.data == __value:
                    if node.next == self._tail:
                        self._tail = node
                    node.next = node.next.next
                    self._len -= 1
                    return
                node = node.next
            raise ValueError(f"{__value} is not in linked list.")
    
    def pop(self, __index:SupportsIndex = -1, /):
        '''Remove and return item at index (default last).

        Raises IndexError if linked list is empty or index is out of range.'''
        if __index < 0:
            __index += self._len
        if __index < 0 or __index >= self._len:
            raise IndexError("pop index out of range")
        if __index == 0:
            data = self._head.data
            if self._tail == self._head:
                self._tail = None
            self._head = self._head.next
            self._len -= 1
        else:
            node = self._head
            for _ in range(__index - 1):
                node = node.next
            data = node.next.data
            if node.next == self._tail:
                self._tail = node
            node.next = node.next.next
            self._len -= 1
        return data
    
    def clear(self):
        '''Remove all items from the linked list.'''
        self._head = None
        self._tail = None
        self._len = 0
        
    
    def index(self, __value, __start = None, __end = None, /):
        '''Return first index of value.
        
        Raises ValueError if the value is not present.'''
        if start == None:
            start = 0
        if end == None:
            end = self._count
        node = self._head
        for _ in range(start, end):
            if node.data == __value:
                return _
            node = node.next
        raise ValueError(f"{__value} is not in linked list.")
    
    def count(self, __value) -> int:
        '''Return number of occurrences of value.'''
        count = 0
        for object in self:
            if object == __value:
                count += 1
        return count


class HashTable:
    def __init__(self, __size:int, __iterable:Iterable = None, /):
        '''Create a new hash table.
        
        size
          the number of bucket.
        iterable
          optional argument. If given, the hash table is initialized by the elements in the iterable.'''
        self._size = __size
        self._table = [None for _ in range(__size)]
        
        if __iterable:
            self.extend(__iterable)
        
    def hash(self, __object:int, /) -> int:
        '''Return hash value of object.'''
        return __object % self._size
        
    def append(self, __object:int, /):
        '''Add an item to the end of the hash table.'''
        bucket = self.hash(__object)
        if not self._table[bucket]:
            self._table[bucket] = LinkedList()
        self._table[bucket].append(__object)
    
    def extend(self, __iterable:Iterable, /):
        '''Extend the hash table by appending all the items from the iterable.'''
        for one in __iterable:
            self.append(one)
    
    def search(self, __value:int, /) -> Optional[Tuple[int, List[int]]]:
        '''Search value in hash table.
        
        Return (bucket, list of index) if found, else None.'''
        bucket = self.hash(__value)
        if not self._table[bucket]:
            return None
        result = [index for index, value in enumerate(self._table[bucket]) if value == __value]
        if not result: 
            return None
        if DEBUG: print(f"{bucket}-bucket", self._table[bucket])
        return (bucket, result)


# Create data for sort
def create_random_data(size:int = 10000, a:int = 0, b:int = 10000, /) -> list:
    '''Return the list of random integers in range [a, b], including both end points.'''
    return [random.randint(a, b) for _ in range(size)]


# define main function
def main(*args, **kwargs) -> int:
    rd_data = create_random_data(10000)
    
    try:
        ht = HashTable(97, rd_data)
        val = int(input("Search >> "))
        print()
        result = ht.search(val)
        if result:
            print(f"{val} is in {result[0]}-bucket index: {result[1]}")
        else:
            print(f"Not Found {val} in random numbers.")
    except Exception as e:
        print("Error : ", e)
        
    return 0


# call main function
if __name__ == '__main__':
    sys.exit(main())