def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            idx = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            idx = mid
            high = mid - 1
    return idx

def find_smallest_memory_greater_than_x(arr, x):
    '''
        This function returns the smallest element
        greater than or equal to x in array arr.
        This function can be used to find the most
        optimal machine for running a program that
        takes x memory. arr contains total memory
        available in the machines in sorted order
    '''
    idx = binary_search(arr, x)
    if idx == -1:
        print("No machine can run program with memory x")
    else:
        print(f"Machine with index {idx + 1} can run the program")
    return idx

if __name__ == '__main__':
    arr = [1, 2, 5, 5, 6, 9, 9, 9, 10]
    idx = find_smallest_memory_greater_than_x(arr, 11)