def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        curr_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min_idx]:
                curr_min_idx = j
        arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]

arr1 = [14, 46, 43, 27, 57, 41, 45,21, 70]
selection_sort(arr1)
print(arr1)

arr2 = [14, 46, 43, 27, 57, 41, 45,21, 70]
insertion_sort(arr2)
print(arr2)



