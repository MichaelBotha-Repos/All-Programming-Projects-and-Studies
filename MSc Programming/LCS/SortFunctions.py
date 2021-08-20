import time 

def insertion_sort(lst):
    temp = None
    for i in range(1,len(lst)):
        temp = lst[i]
        k=1
        while lst[i-k].lower()> temp.lower():
            lst[i-k+1] = lst[i-k]
            if (i-k)==0:
                k+=1
                break
            k+=1
        lst[i-k+1]=temp
    cnt=1
    for i in lst:
        print(cnt, i)
        cnt+=1
        
##def Bubble_sort(lst):
##    '''This function performs an ascending order Bubble sort where the list is iterated through
##       comparing each consecutive element pairs to see if there is one greater than the other in
##       a lower index position which would subsequently be swapped. The for loop is iterated by the
##       while loop which continues until no more swaps are made, controlled by the "swap" control
##       variable. It takes a single parameter which is the list'''
##    swap=1
##    while swap== 1:
##        swap=0
##        for i in range(len(lst)-1):
##            if lst[i].lower() > lst[i+1].lower():
##                lst[i], lst[i+1] = lst[i+1], lst[i]
##                swap=1        

lst = ['michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David'\
       'michael botha','Amy Botha','Louise wath','Pin Code:)','Emergency Services','jame','john','chris','Philip',\
        'charles','abraham','william','robert','imtiaz','sini','vernon','julios','malcom','lorraine','abigal',\
       'shakespeare', 'billy','lance','douglas','shaun','Sanjiv','promise','strom','sky','Isiaih','Moses','David']

print(lst)
insertion_sort(lst)
time.sleep(5)

