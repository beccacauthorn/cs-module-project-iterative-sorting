def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        #compare the target element to the midpoint
        mid= (high+low) // 2
        #if the midpoint element matches our target, then we've found what we are looking for
        #return the midpoint index
        if target == arr[mid]:
            return mid
        #determine which half to go in; toss out the other half
        if target < arr[mid]:
            #cut out the right half
            #reassign high to mid -1
            high = mid -1
        if target > arr[mid]:
            #cut out left half
            #reassign low to mid -1
            low = mid +1
            #repeat the process, we need a loop for this
    #we've reached the outside of the loop, the element doesn't exist in the array
    return -1  # not found
