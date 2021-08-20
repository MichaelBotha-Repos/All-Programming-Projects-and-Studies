'''This program accepts 9 rows of 9 numbers and tests whether they conform to the Sadoku logic'''

Lst=[]
for i in range(9):
    print("Please insert the",i+1,"row of the Sadoku:")
    string= input()
    temp_Lst= list(string)
    Lst.append(temp_Lst)
for elem in Lst:
    print(elem)

z = True
good=0
while z==True:
    for i in range(9):
        test=0
        for elem in Lst[i]:
            test+= int(elem)
        if test != 45:
            z= False
            break
        else:
            print("row",i+1,"fine")
            good+=1
    if z== False:
            print('no Sadoku row',i+1)
            break
        
    
    for x in range(9):
        test2=0
        for y in range(9):
            test2+= int(Lst[y][x])
        if test2 != 45:
            z= False
            break
        else:
            print("column",x+1,"fine")
            good+=1
    if z== False:
            print('no Sadoku column',x+1)
            break

    test3a=0
    test3b=0
    test3c=0
    test3d=0
    test3e=0
    test3f=0
    test3g=0
    test3h=0
    test3i=0
    for a in range(3):
        for b in range(3):
            test3a+=int(Lst[a][b])
            test3b+=int(Lst[a][b+3])
            test3c+=int(Lst[a][b+6])
            test3d+=int(Lst[a+3][b])
            test3e+=int(Lst[a+3][b+3])
            test3f+=int(Lst[a+3][b+6])
            test3g+=int(Lst[a+6][b])
            test3h+=int(Lst[a+6][b+3])
            test3i+=int(Lst[a+6][b+6]) 
            
    if (test3a!= 45) or (test3b!= 45) or (test3c!= 45) or (test3d!= 45) or (test3e!= 45) or (test3f!= 45) \
    or (test3g!= 45) or (test3h!= 45) or (test3i != 45):
        print('no saduko')
        break
    else:
        print('yes Saduko!')
        break

