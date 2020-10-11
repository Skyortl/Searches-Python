import random
import numpy
import time,datetime, contextlib

def linear_search(values, search_for):
    search_at = 0
    search_res = False
    while search_at < len(values) and search_res!=1:
        if values[search_at] == search_for:
            search_res = 1
        else:
            search_at+=1
    return search_res
def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else: 
        return -1
def intpolsearch(values, x):
    idx0 = 0
    idxn = (len(values) - 1)
    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
        mid = idx0 + int(((float(idxn - idx0) / (values[idxn] - values[idx0])) * (x - values[idx0])))
        if values[mid] == x:
            return 1
        if values[mid] < x:
            idx0 = mid + 1
        else:
            idxn=mid-1
    return -1
def partition(arr, low, high):
    i = (low-1) 
    pivot = arr[high] 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        sort(arr, low, pi-1)
        sort(arr, pi+1, high)
 
searching = int(input("Введите число для поиска "))
items = []
min =50000
max = 1000000
step = 50000
while min <= max:
    items =  [random.randint(0, 100000) for i in range(min)]
    t = time.monotonic()
    index = linear_search(items, searching)
    if index==1:
        print('linear {}'.format(time.monotonic() - t), 'elements {}'.format(min))
    else:
        print('linear элемент не найден {}'.format(time.monotonic() - t))
    sort(items, 0, len(items) - 1)
    t = time.monotonic()
    index = binarySearch(items, 0, len(items) - 1, searching)
    if index == 1:
        print('binary {}'.format(time.monotonic() - t), 'elements {}'.format(min))
    else:
        print('binary элемент не найден {}'.format(time.monotonic() - t))
    t = time.monotonic()
    index = intpolsearch(items, searching)
    if index == 1:
        print('interpol {}'.format(time.monotonic() - t), 'elements {}'.format(min))
    else:
        print('interpol элемент не найден {}'.format(time.monotonic() - t))
    min = min + step


