# 자료구조개론 8주차 과제6
# Quick Sort 구현
#
# 미래모빌리티학과
# 2021271402 이지오


# <조건 1> 정렬 예정인 데이터는 0~999 사이의 임의의 정수 총 1만개이다.
# <조건 2> 중복된 데이터도 정렬되어야 한다. (버리면 안된다.)
# <조건 3> leftAry, rightAry = [], [] 배열을 사용하지 않는다. 즉, <조건 1>에서 주어진 배열만
# 사용한다.(in-place)
# <조건 4> append() 메소드는 사용하지 않는다.
# <조건 5> 프로그램 수행시간을 출력한다.


# True : print debug message
DEBUG = False   


# module containing
import sys      # for call main function
import random   # for create random data
import time     # for check time


# Create data for sort
def create_random_data(size:int = 1000) -> list:
    return [random.randint(0, 999) for _ in range(size)]


# Print data
def print_data(data:list, skip:int = 5, *args, **kwargs) -> None:
    result = data
    if len(data) > skip*2:
        result = data[:skip] + [" ... "] + data[-skip:]   # print first (number of)skip and last (number of)skip data
    print('[', end="")
    hidden = True
    for num in result:
        if type(num) is int:
            if hidden:
                print(f"{num:}", end="")
                hidden = False
            print(f", {num:}", end="")
        else:
            print(num, end="")
            hidden = True
    print(']')
    print(f"Data length : {len(data)}", *args, **kwargs)


# Quick Sort - Return swap count
def quick_sort(data:list, start:int, end:int) -> int:
    swap_count = 0
    if start < end:
        pivot = (end - start) // 2 + start
        left = start
        right = end
        while left <= right:
            while data[left] < data[pivot]:
                left += 1
            while data[right] > data[pivot]:
                right -= 1
            if left <= right:
                if left != right and data[left] != data[right]:
                    data[left], data[right] = data[right], data[left]
                    if DEBUG: print(f"swap {data[left]} <-> {data[right]}")
                    swap_count += 1
                left += 1
                right -= 1
        swap_count += quick_sort(data, start, right)
        swap_count += quick_sort(data, left, end)
    return swap_count


# Time check using callback function
def time_check(func, *args, **kwargs) -> any:
    start = time.time()
    result = func(*args, **kwargs) # call func and save result
    end = time.time()
    print(f'\'{func.__name__}\' function Run Time : {end - start:.6f} Sec')
    return result # return func result


# define main function
def main(*args, **kwargs) -> int:
    data = create_random_data(5)
    
    print("Data before Quick sort")
    print_data(data, 10, end='\n\n')
    
    swap_count = time_check(quick_sort, data, 0, len(data) - 1)
    if DEBUG: print(f"swap count : {swap_count}")
    print()
    
    print("Data after Quick Sort")
    print_data(data, 10)
    
    return 0


# call main function
if __name__ == '__main__':
    sys.exit(main())