#
# Description: sort for test.
# Author: Wang Yong
# email: dr.yongwang at hotmail.com
# Date: 2023/12/01
# 
# O(n^2)
#

# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

# insert sort
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

# select sort
def select_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
# merge sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1
    return result

# heap sort
def heap_sort(arr):
    pass


if __name__ == '__main__':
    arr = [3, 2, 1, 4, 5, 7, 10, 25, 6, 9]
    print(bubble_sort(arr))
    print(insert_sort(arr))


