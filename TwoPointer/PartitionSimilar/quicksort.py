def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] <= pivot:    
            nums[j], nums[i] = nums[i], nums[j]
            i+=1

    nums[right], nums[i] = nums[i], nums[right]
    return i

def quicksort(array, start, end):
    if  start < end: #用if not while, if is a one time branching operation while loop does things as long as the condition is true
        pivot = partition(array, start, end)
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)


array = [3, 2, 1, 0, 9, 7, 7, 6, 5, 4]
quicksort(array, 0, 9)
print(array)
# print(partition(array, 0, 9))