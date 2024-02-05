# Third Maximum Number in an array 
# arr = [ 6,5,4,3,2,1]    # pass
# arr = [ 1,2,3,4,5,6]    # pass
# arr =  [100,23,77,-2,34,11]    # pass
arr =  [9,-2,98,47,98]    # pass

max_num = arr[0]
sec_max = arr[1]
thrd_max = arr[2]


for i in arr:
    
    if i > max_num:
        thrd_max = sec_max
        sec_max = max_num
        max_num = i
        
        
    
    elif i>sec_max and i!=max_num:
        thrd_max = sec_max
        sec_max = i
        
    elif i>thrd_max and i!=sec_max and i!=max_num:
        thrd_max = i

        
print(max_num)
print(sec_max)
print(thrd_max)
