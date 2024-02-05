# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest  substring without repeating characters.


def is_find(a,arr):
    if a in arr:
        return True
    else:
        return False
    


# possible use cases to be considered.
# my_str = "abcabcbb"
my_str = "pwwkew"
# my_str = "bbbbb" 
my_str = "dvdf"
store = []
max_substr = 0
sub_str=0

for i in range(len(my_str)):
    if is_find(my_str[i],store):
          ind = store.index(my_str[i])
          store = store[ind+1:]

 
    store.append(my_str[i])
    sub_str = len(store)    
    if sub_str>max_substr:
        max_substr= sub_str
        # print(store)
        
print(max_substr)       