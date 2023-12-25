target= 5
arr = [-1,2,1,-4]
# arr = [1,2,3,4]

equal=0
add=0
nearest = float('inf')
flag=False

for i in range(len(arr)-2):
    add = sum(arr[i:i+3])
    if add == target:
        print("add")
        equal = add
        flag = True
        break
    
    temp = abs(add-target)
    if temp<nearest:
        nearest = add
         

if flag:
    output = equal
else:
    output = nearest

    
# this would print the nearest neighbors by adding three consecutive numbers in an array            
print(output)        
