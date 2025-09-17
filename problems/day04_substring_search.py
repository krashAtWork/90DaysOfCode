'''find substring in string'''

def isSubStringPresent(main_str, sub_str):
    len_main = len(main_str)
    len_sub = len(sub_str)

    if len_sub > len_main:
        return False
    j = 0 #index for substr

    for i in range(0, len_main):
        if len_main - i >= len_sub - j:
            if main_str[i] == sub_str[j]:
                print("target string found")
                j = j+1
                if j == len_sub:
                    return True
        else:
            return False
        
    

