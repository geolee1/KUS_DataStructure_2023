# 자료구조개론 7주차 과제5
# Circular Queue 구현
#
# 미래모빌리티학과
# 2021271402 이지오


# module containing
import sys


# 1. Circular Queue를 클래스로 구현하라. 배열을 이용하여 구현하라. linked list가 아니다.
#   - front, rear, n개의 data
# 2. isEmpty(), isFull(), clear() 메소드 구현
# 3. enqueue(), dequeue(), peek() 메소드 구현
# 4. display() 메소드 구현
#   - front > rear의 경우를 조심하라
class Queue:
    def __init__(self, queue_size:int = 8):
        self.MAX_QSIZE = queue_size
        self.clear()

        
    def is_empty(self) -> bool:
        return self.front == self.rear
    
    def is_full(self) -> bool:
        return self.front % self.MAX_QSIZE == (self.rear + 1) % self.MAX_QSIZE

    def clear(self) -> None:
        self.items = [None for _ in range(self.MAX_QSIZE)]
        self.front = -1
        self.rear = -1
        
    def enqueue(self, data: any) -> None:
        if self.is_full():
            raise IndexError('Queue is full')
        self.rear = (self.rear + 1) % self.MAX_QSIZE
        self.items[self.rear] = data

    def dequeue(self) -> any:
        if self.is_empty():
            raise IndexError('Queue is empty')
        self.front = (self.front + 1) % self.MAX_QSIZE
        result = self.items[self.front]
        self.items[self.front] = None
        return result
    
    def peek(self) -> any:
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items[(self.front + 1) % self.MAX_QSIZE]

    def display(self) -> None:
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue : <- ", end='')
            if self.front <= self.rear:
                for i in range(self.front + 1, self.rear + 1):
                    print(f"{self.items[i]} ", end='')
            else:
                for i in range(self.front + 1, self.MAX_QSIZE):
                    print(f"{self.items[i]} ", end='')
                for i in range(0, self.rear + 1):
                    print(f"{self.items[i]} ", end='')
            print("<-")
        print()
            
    def display_all(self) -> None:
        # print(f"front = {self.front}, rear = {self.rear}")
        for i in range(self.MAX_QSIZE):
            print(f"[{i}] = {str(self.items[i]):<5}", end = '')
            if i == self.front:
                print(" <-- front")
            elif i == self.rear:
                print(" <-- rear")
            else:
                print()
        print()



# define main function
def main() -> int:
    queue = Queue(8)
    queue.display()
    queue.display_all()
    
    print("\n첫번째 그림")
    queue.enqueue('G')
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.enqueue('D')
    queue.dequeue()
    queue.dequeue()
    
    queue.display()
    queue.display_all()
    
    print("\n두번째 그림")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue('D')
    queue.enqueue('E')
    queue.enqueue('F')
    queue.enqueue('G')
    queue.enqueue('A')
    queue.enqueue('B')
    queue.dequeue()
    queue.dequeue()
    
    queue.display()
    queue.display_all()


# call main function
if __name__ == '__main__':
    sys.exit(main())