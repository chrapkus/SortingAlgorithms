import random
import time
import sys
import matplotlib.pyplot as plt
from matplotlib import style

sys.setrecursionlimit(3000)


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


def heapSort(A):
    heap_size = len(A)
    for i in range(int(heap_size / 2), -1, -1):  # max heap build
        heapify(A, heap_size, i)

    for i in range(heap_size - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


def heapify(A, n, i):
    largest_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[largest_index] < A[left]:
        largest_index = left

    if right < n and A[largest_index] < A[right]:
        largest_index = right
    if largest_index != i:
        A[i], A[largest_index] = A[largest_index], A[i]
        heapify(A, n, largest_index)


"""def QuickSort(array):

    import sys
    sys.setrecursionlimit(10000)

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return QuickSort(less)+equal+ QuickSort(greater)
    else:
        return array"""
import sys

sys.setrecursionlimit(10000)


def QuickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def timer(f, A):
    tic = time.perf_counter()
    f(A)
    toc = time.perf_counter()
    return round(toc - tic, 5)


def list_generator(type, size):
    randomlist = []
    random.seed(9001)
    begin = 0  # wartości będą od 0
    end_range = size * 5  # do rozmiaru tabeli *5 <--------------
    if type == 1:
        for i in range(0, size):
            n = random.randint(begin, end_range)
            randomlist.append(n)
    elif type == 2:
        for i in range(begin, begin + size):
            randomlist.append(i)
    elif type == 3:
        for i in range(end_range, end_range - size, -1):
            randomlist.append(i)
    elif type == 5:
        first_item = int(size / 2)
        swich = 0
        for i in range(0, size):

            if first_item == 0:
                swich = 1

            if swich == 0:
                first_item = first_item - 1
                randomlist.append(first_item)
            else:
                first_item = first_item + 1
                randomlist.append(first_item)
    else:
        k = random.randint(-300000, 500000)
        for i in range(0, size):
            randomlist.append(k)

    return randomlist


def dictcreator():
    data_set_algorithms = {"Number_of_elements": [], "InsertionSort": [], "SelectionSort": [], "HeapSort": [],
                           "QuickSort": []}
    data_set_algorithms["Number_of_elements"] = []
    data_set_algorithms["InsertionSort"] = []
    data_set_algorithms["SelectionSort"] = []
    data_set_algorithms["HeapSort"] = []
    data_set_algorithms["QuickSort"] = []
    return data_set_algorithms


def put_data(myDict, starting_size, numbers_of_steps, step_size, data_type):
    array_size = starting_size
    for i in range(numbers_of_steps):
        list1 = list_generator(data_type, array_size)
        list2 = list1
        list3 = list1
        list4 = list1
        myDict["Number_of_elements"].append(array_size)
        myDict["InsertionSort"].append(timer(insertionSort, list1))
        myDict["SelectionSort"].append(timer(selectionSort, list2))
        myDict["HeapSort"].append(timer(heapSort, list3))
        myDict["QuickSort"].append(timer(QuickSort, list4))

        array_size = array_size + step_size


# 1-losowe, 2-rosnące, 3-malejące, 4-stałe, v-krztałtej-5

My_Dict_losowe = dictcreator()
put_data(My_Dict_losowe, 500, 20, 500, 1)
print(My_Dict_losowe)

y = My_Dict_losowe["InsertionSort"]
x = My_Dict_losowe["Number_of_elements"]
y1 = My_Dict_losowe["SelectionSort"]
x1 = My_Dict_losowe["Number_of_elements"]
y2 = My_Dict_losowe["HeapSort"]
x2 = My_Dict_losowe["Number_of_elements"]
y3 = My_Dict_losowe["QuickSort"]
x3 = My_Dict_losowe["Number_of_elements"]

plt.plot(x, y, label="InsertionSort")
plt.plot(x1, y1, label='SelectionSort')
plt.plot(x2, y2, label="HeapSort")
plt.plot(x3, y3, label="QuickSort")
plt.xlabel('number of elements')

plt.ylabel('time(s)')

plt.title('My first graph!')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()