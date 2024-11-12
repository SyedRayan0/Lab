'''
Milburn's Repository link - https://
github.com/Milburn-Simon-Veron-Lobo/software-memory
'''
'''
Baahir's Repository link - https://github.com/Baahir2007/GCIS.git
'''
'''Syed Rayan Repository- https://github.com/SyedRayan0/Lab'''
import random
import time

def generate_sorted_data(size):
    """
    This function generates an array of random integers between 1 and 100, 
    sorts the array using insertion sort or merge sort and returns the sorted array.
    """
    # To make array of random integers between 1 and 100
    data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(size)]
    
    print("Data before sorting:", data)
    
    print("Press 1 to sort using Insertion sort\nPress 2 to sort using Merge sort\nPress 0 to quit")
    
    ans = int(input("------>"))

    while ans:

        if ans == 1: # Insertion Sort
            print("Performing Insertion Sort.....")
            for i in range(1, size):
                key = data[i]
                j = i - 1
                while j >= 0 and key < data[j]:
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = key
            
            # Printing the data after sorting
            print("Data after Insertion sorting:", data)
            
            return data
        
        elif ans == 2: # Merge Sort
            print("Performing Merge Sort.....")
            sorted_data = arr_split(data)

            # Printing the data after sorting
            print("Data after Merge sorting:", sorted_data)
            return sorted_data
        
        elif ans == 0: # Quitting the function
            print("Quitting the sort function.....")
            break

        else:
            print("Invalid input, enter again")
            print("Press 1 to sort using Insertion sort\nPress 2 to sort using Merge sort\nPress 'q' to quit")
            ans = int(input("------>"))
    

def arr_split(arr):
    """
    This function splits the given array into two halves and further splits
    each half into two using recursion. It then sends both the obtained halves 
    to the merge_sort() function.
    """
    if arr is None:
        return arr
    elif len(arr) <= 1:
        return arr
    else:
        mid=len(arr)//2
        arr[:mid] = arr_split(arr[:mid]) # Recursion 1
        arr[mid:] = arr_split(arr[mid:]) # Recursion 2
        arr[0:] = merge_sort(arr[:mid], arr[mid:]) # Recursion 3
        print("---------->", arr)
        return arr

def merge_sort(left, right):
    """
    This function returns a sorted array by comparing the left array
    with the right array.
    """ 
    if not left:
        return right
    if not right:
        return left
    if left[0] <= right[0]:
        return [left[0]]+merge_sort(left[1:],right) # Recursion 4
    else:
        return [right[0]]+merge_sort(left,right[1:]) # Recursion 5
    
  

def linear_search(arr, target):
    """
    Performs linear search on an array using a while loop to find the index of the target.
    Returns the index of the target if found, otherwise returns None.
    """
    i = 0  
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1  
    return None  # Target not found

def binary_search(sorted_array, target):
    """
    Performs binary search on a sorted array to find the index of the target.
    Returns the index of the target if found, otherwise returns None.
    """
    start = 0
    end = len(sorted_array) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

def main():
    size = 101 # 990 for 1000 elements
      # Adjust the size for larger datasets
    sorted_data = generate_sorted_data(size)

    # Sample Target
    target = 72
    
    # Measure the time for linear search
    start_time = time.perf_counter()
    linear_index = linear_search(sorted_data, target)
    linear_time = time.perf_counter() - start_time

    # Measure the time for binary search
    start_time = time.perf_counter()
    binary_index = binary_search(sorted_data, target)
    binary_time = time.perf_counter() - start_time

 
    if linear_index is not None:
        print("Linear Search: Target",target,"found at index", linear_index)
    else:
        print("Linear Search: Target ",target, "not found.")
    
    if binary_index is not None:
        print("Binary Search: Target ",target,"found at index ",binary_index)
    else:
        print("Binary Search: Target",target," not found.")
    
    print("Linear Search Time:",linear_time, "seconds")
    print("Binary Search Time" ,binary_time, "seconds")


if __name__ == "__main__":
    main()
    
  