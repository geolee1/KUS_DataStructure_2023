import random
import time

def partition(ary, left, right):
    pivot = ary[right]
    pIdx = left
    #print()

    for i in range(left, right):
        if ary[i] <= pivot:
            ary[pIdx], ary[i] = ary[i], ary[pIdx]
            pIdx += 1
            #print(ary)
    #print("pIdx: ", pIdx, "right: ", right,
    #      ", left: ", left)
    
    ary[pIdx], ary[right] = ary[right], ary[pIdx]
    #print(ary)
    return pIdx


def quickSort(ary, left, right):
    #print("quickSort in")
    
    if left < right:
        pIdx = partition(ary, left, right)
        quickSort(ary, left, pIdx - 1)
        quickSort(ary, pIdx + 1, right)

    #print("quickSort out")




# ary = [188, 150, 168, 162, 105, 120,
#       177,50,123]

ary = [random.randint(0,999) for _ in range(10000)]

n = len(ary)
start = time.time()
quickSort(ary, 0, n-1)
end = time.time()

print("Sorted ary", ary)

execution_time = end - start
print("Execution time: ", execution_time)
