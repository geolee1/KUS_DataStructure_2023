class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def clear_list(self):
        self.head = None

    def size_of_list(self):
        current = self.head
        if current is None:
            return 0
        count = 1
        while current.next != self.head:
            current = current.next
            count += 1
        return count

    def print_linked_list(self):
        if self.head is None:
            print("Empty linked list!")
        else:
            current = self.head
            circular_linked_list = []
            
            while True:
                circular_linked_list.append(current.data)
                current = current.next
                if current == self.head:
                    break
                
            print("circular_linked_list: ",circular_linked_list)
                
            

    def insert_Node1(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            prev = new_node
            prev.next = self.head
            last = self.head
            while last.next != self.head:
                last = last.next
                
            last.next = prev

        
    def insert_Node2(self, data, index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head      
        else:
            prev = new_node
            current = self.head
            i = 0

            if index == 0:
                prev.next=self.head
                while current.next != self.head:
                    current = current.next
                current.next = prev
                self.head = prev
            else:
                while i < index-1:
                    prev.next = current
                    current = current.next
                    i += 1
                prev.next = current.next
                current.next = prev


            
    def delete_Node(self, data):
        if self.head is None:
            print("Empty Circular List!")
            return

        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                self.head = self.head.next
                current.next = self.head
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                if current.data == data:
                    prev.next = current.next
                    return
                prev = current
                current = current.next

            # Check the last node
            if current.data == data:
                prev.next = current.next
            
        
    def find_Node(self, data):
        if self.head is None:
            print("Empty Circular List!")
            return None

        current = self.head

        while current.next != self.head:
            if current.data == data:
                return data
            current = current.next

        # Check the last node
        if current.data == data:
            return data

        # 데이터를 찾지 못한 경우 None을 반환
        return None
            

def main():
    computerArray = ["keyboard", "mouse", "monitor", "printer", "scanner"]

    circular_linked_list = CircularLinkedList()
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())
    
    for item in computerArray:
        circular_linked_list.insert_Node1(item)
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())
    print("asdf")
    circular_linked_list.insert_Node2("new_value",1)
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())
    print("Find node: ",circular_linked_list.find_Node('monitor'))

    circular_linked_list.delete_Node('new_value')
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())
main()

