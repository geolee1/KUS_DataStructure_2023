import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, bucket):
        self.buckets = [None] * bucket

    def insert(self, k):
        hash_k = k % len(self.buckets)
        if not self.buckets[hash_k]:
            self.buckets[hash_k] = Node(k)
        else:
            current = self.buckets[hash_k]
            while current.next:
                current = current.next
            current.next = Node(k)

    def search(self, k):
        hash_k = k % len(self.buckets)
        current = self.buckets[hash_k]
        i = 0
        while current:
            if current.value == k:
                return hash_k, i  # hash_k 번째 bucket의 i 번째 linked list
            current = current.next
            i += 1
        return "not found"

# Create a hash table
hash_table = HashTable(97)

'''
for _ in range(10000):
    hash_table.insert(random.randint(1, 100000))
'''

for i in range(99):
    hash_table.insert(i)

# Search for a random number
# result = hash_table.search(random.randint(1, 100000))
result = hash_table.search(98)
print(result)
