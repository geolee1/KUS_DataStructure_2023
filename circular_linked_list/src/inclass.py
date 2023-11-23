class Node:
    def __init__(self, data=None):
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

        while current.next is not None:
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
            print(f"{circular_linked_list = }")

    def append_Node(self, data):
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

    def insert_Node(self, data, index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            prev = new_node
            current = self.head
            i = 0
            if index == 0:
                prev.next = self.head
                while current.next != self.head:
                    current = current.next
                current.next = prev
                self.head = prev
            else:
                while 1 < index-1:
                    prev.next = current
                    current = current.next
                    i += 1

                prev.next = current.next
                current.next = prev


def main():
    computerArray = ["keyboard", "mouse", "monitor", "printer", "scanner"]
    circular_linked_list = CircularLinkedList()
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())

    for item in computerArray:
        circular_linked_list.append_Node(item)
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())

    circular_linked_list.insert_Node("new_node", 0)
    circular_linked_list.print_linked_list()
    print("size: ", circular_linked_list.size_of_list())


if __name__ == "__main__":
    main()
