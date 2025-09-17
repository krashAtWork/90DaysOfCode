import math

def get_max_subarray_sum(arr):

    if len(arr) == 0:
        return 0
    best = arr[0]
    currentSum = arr[0]

    # we must go through entire array to answer this question
    for i in range(1, len(arr)):

        currentSum = arr[i] + currentSum # determine the current sum number
        currentSum = max(currentSum, arr[i]) # currentSum  is the max of current number  and the currentSum
        best = max(currentSum, best) # 
        if currentSum < 0:
            currentSum = 0
    return best
    
# print(get_max_subarray_sum([1,2,3,4,5])) # 15

# This is the implementation of Kadane's algorithem, which states that you only add an element that increases the value, if youadd something that decreases the value to be negative, then make it to 0
# Time complexity is O(n)
# Space complexity is O(1)

