class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def clear_list(self):
        print("Clear_list!")
        self.head = None

    def size_of_list(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def print_linked_list(self):
        node_list = []
        current = self.head
        while current:
            node_list.append(current.data)
            current = current.next
        print(node_list)
        
    def insert_Node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
         
    def delete_Node(self, data):
        current = self.head
        while current and current.data != data:
            prev = current
            current = current.next
        if not current:
            return
        prev.next = current.next

    def find_Node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current= current.next
        return None


def main():
    linked_list = LinkedList()

    linked_list.print_linked_list()
    print("size: ", linked_list.size_of_list())

    if linked_list.isEmpty() :
        print("Empty linked list!")

    computerArray = ['keyboard', 'mouse', 'monitor', 'printer', 'scanner']

    print("Insert node!")
    for data in computerArray:
        linked_list.insert_Node(data)
    linked_list.print_linked_list()
    print("size: ", linked_list.size_of_list())
    print()

    print("delete node!")
    linked_list.delete_Node('keyboard')
    print("size: ", linked_list.size_of_list())
    linked_list.print_linked_list()
    print()

    
    print("Find node: ",linked_list.find_Node('mouse'))
    print("size: ", linked_list.size_of_list())
    linked_list.print_linked_list()
    print()
    
    linked_list.clear_list()
    linked_list.print_linked_list()
    print("size: ", linked_list.size_of_list())
    print()
    
    if linked_list.isEmpty() :
        print("Empty linked list")
        

main()
