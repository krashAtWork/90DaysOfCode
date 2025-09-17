'''Remove duplicates from sorted array in place
'''

def remove_duplicates(nums):
    j = None
    mem = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] in mem: # current elemen is in memory
            nums[i] = "_" # assign it as duplicate
            if j is None: # if there is no "_" yet
                j = i
        else:
            mem.append(nums[i])
            if  j: # if there is already a "_"
                nums[j], nums[i] = nums[i], nums[j]
                nj = j
                while(nj < i):
                    if nums[nj] == "_":
                        j = nj
                    else:
                        nj+=1

                
    print(nums)
    return nums

def remove_duplicates_v2(nums):
    #i the pointer that asks current element are you unique, and determines answer by checking previous i.e. i-1 element
    #j the pointer that is holding space for the next unique element
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]: # current element is unique
            nums[j] = nums[i] # replace jthe index with current new element
            j+=1 # increment j i.e. hold space for the next unique element
        else:
            print(f"{nums[i]} and {nums[i-1]} is same")
            print(j)
    for k in range(j, len(nums)):
        nums[k] ="_"
    return nums


nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates_v2(nums))





