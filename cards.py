cards = ['Jack', 8, 2, 6, 'King', 5, 3,6, 'Queen','Jack','Queen','King']
size = len(cards)

# initially these loops are used to sort the numbers only
for i in range(size-1):
    if type(cards[i])==str:
        continue

    for j in range(size):
        if type(cards[j])==str:
            continue
            
        elif cards[i]<cards[j]:
            temp = cards[i]
            cards[i] =  cards[j]
            cards[j] =  temp
 
# this logic is used to sort the string
flag = True
cnt=0
while flag:    
    if 'Jack' in cards:
        cards.remove('Jack')
        cnt+=1
    else:
        flag=False
        
for i in range(cnt):    
    cards.append('Jack')
        
flag = True
cnt=0
while flag:    
    if 'Queen' in cards:
        cards.remove('Queen')
        cnt+=1
    else:
        flag=False
        
for i in range(cnt):    
    cards.append('Queen')

flag = True
cnt=0
while flag:    
    if 'King' in cards:
        cards.remove('King')
        cnt+=1
    else:
        flag=False       
for i in range(cnt):    
    cards.append('King')
cards