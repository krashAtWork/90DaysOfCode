# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def move_0s_to_end(arr):

    if len(arr) < 2:
        return arr 
    
    cntr = 0 # number of Zeros found
    pt_2_0 = 0 # pointer that always points to the zero
    pt_2_next_elt = 0 # pointer that always points to the next element

    while pt_2_next_elt < len(arr):
        if arr[pt_2_next_elt] == 0:
            #zero found
            cntr +=1
        else:
            if cntr > 0 :
                arr[pt_2_0], arr[pt_2_next_elt] = arr[pt_2_next_elt], arr[pt_2_0]
                pt_2_0 +=1 #increment ptr_2_0

        pt_2_next_elt +=1

    return arr
      
