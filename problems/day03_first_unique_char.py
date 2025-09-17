'''Find the First unique character in a string'''

def firstUniqueChar(st1):
    len_input = len(st1)
    if len_input == 0:
        raise IndexError("String is empty")
    elif len_input == 1:
        return st1
    else:
        #write actual lofic
        temp = {} #a,1, b,2
        for i in range(0, len_input):
            if st1[i] not in  temp:
                temp[st1[i]] = 1
            else:
                temp[st1[i]] +=1

        print(temp)

        #go through keys and find the key which has value of 1
        # Iterate through the dictionary to find the first unique character
        for key, val in temp.items():
            if val == 1:
                print("1 " + key)
                print("2 " + str(temp[key]))
                return key
        return False
        
                


    

