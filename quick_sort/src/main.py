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


# module containing
import sys      # for call main function
import random   # for create random data
import time     # for check time

# 정렬할 데이터 생성
def create_random_data(size:int = 10000) -> list:
    return [random.randint(0, 999) for _ in range(size)]

# Quick Sort 구현
def quick_sort(data:list, start:int, end:int) -> None:
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort(data, start, right - 1)
    quick_sort(data, right + 1, end)


# 콜백 함수를 이용한 수행시간 측정
def time_check(func, *args, **kwargs) -> any:
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f'수행시간 : {end - start:.3f}초\n')
    return result


# define main function
def main(*args, **kwargs) -> int:
    data = create_random_data()
    print("정렬 전 데이터")
    print(f"{data[:20]} ... {data[-20:]}\n")   # print first 10 and last 10 data
    
    print("정렬 시행...")
    time_check(quick_sort, data, 0, len(data) - 1)
    
    print("정렬 후 데이터")
    print(f"{data[:20]} ... {data[-20:]}\n")   # print first 10 and last 10 data
    
    return 0  # return exit code 0 (success)


# call main function
if __name__ == '__main__':
    sys.exit(main())