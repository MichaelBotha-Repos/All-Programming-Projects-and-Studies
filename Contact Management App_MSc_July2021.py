""" This program is a Contact Management Application Software which allows a user to
    enter contacts with related details and work with the records """

book = {
    'michael botha':['Phone1: 079 777 8888','Phone2:','Email: Mbotha@gmail.com'],                  #Line 4-9 creates the global dictionary data structure with some                                    
    'Amy Botha':['Phone1: 0728874545','Phone2: 079 784 3333', 'Email: Abotha.com'],                #preloaded values for test purposes
    'Louise wath':['Phone1: 0821234567','Phone2:', 'Email: LW@haha.co.za'],
    'Pin Code:)':['Phone1: 987654','Phone2:', 'Email: Johan@Thunder.com'],
    'Emergency Services':['Phone1: 911','Phone2: 0611115554','Email: fun@him.co.za']}                                               

## Initial sort used was a Bubble Sort with efficiency inferior to Insertion Sort algorithm##
#def sort(lst):
#    '''This function performs an ascending order Bubble sort where the list is iterated through
#       comparing each consecutive element pairs to see if there is one greater than the other in
#       a lower index position which would subsequently be swapped. The for loop is iterated by the
#       while loop which continues until no more swaps are made, controlled by the "swap" control
#       variable. It takes a single parameter which is the list'''
#    swap=1
#    while swap== 1:
#        swap=0
#        for i in range(len(lst)-1):
#            if lst[i].lower() > lst[i+1].lower():
#                lst[i], lst[i+1] = lst[i+1], lst[i]
#                swap=1

def sort(lst):
    '''This function performs an ascending-order Insertion Sort. A single
        parameter in the form of a list containing names will be fed to it'''
    
    temp = None
    for i in range(1,len(lst)):                                                                    #Line 30-40 starts at second element (index 1) and moves to index + 1
        temp = lst[i]                                                                              #after each iteration. The value selected is stored in temp and
        k=1                                                                                        #all the values before the selected postion are checked to see
        while lst[i-k].lower()> temp.lower():                                                      #if larger than temp. If true the values are shifted towards 
            lst[i-k+1] = lst[i-k]                                                                  #the temp index position until the first element or a value smaller than temp
            if (i-k)==0:
                k+=1
                break
            k+=1
        lst[i-k+1]=temp
        
        
def add():
    ''' This function adds a contact with its respective details and has no parameters'''
    global book
    
    a = input("Please enter name of new or existing contact or press enter:\n")                     #Line 47-50 asks user for input to temporarily store in local scope variables
    b = input("Please enter new Phone1 number or press enter:\n")
    c = input("Please enter new Phone2 number or press enter:\n")
    d = input("Please enter new Email address or press enter:\n")

    while True:
        check = input("Are you sure you want to add this contact? Insert y for yes, n for no:\n")  #Line 52-65 makes sure user wants to save entry,                                                                                      
        if(check == 'y'):                                                                           #then saves to dictionary, displays saved contact's details and returns to 
            book[a] = ['Phone1: ' + b, 'Phone2: ' + c, 'Email: ' + d]                               #main program, or exits if user does not want to save, or if not y or n
            print("Contact added successfully\n")                                                   #requests correct input from user
            print("Name: " + a) 
            for val in book[a]:
                print(val)
            print("\n\n")
            break
        elif(check == 'n'):
            break
        else:
            print("Please enter a correct option")

## Investigate use of Binary Search algorithm for improved search efficiency##
#def binary_search(List, Target):
#    while len(List) >1:    
#        if (len(List)%2) == 0:
#            if (List[len(List)//2 -1])== Target:
#                print(True)
#                return
#            else:
#                if Target < (List[(len(List)//2-1)]) :
#                    return binary_search(List[0:len(List)//2], Target)
#                else:
#                    return binary_search(List[len(List)//2 +1:], Target)
#        else:
#            if (List[(len(List)-1)//2])== Target:
#                print(True)
#                return
#            else:
#                if Target < (List[(len(List)-1)//2]) :
#                    return binary_search(List[0:len(List)//2], Target)
#                else:
#                   return binary_search(List[len(List)//2 +1:], Target)
#    else:
#        print(False)

def search(name):
    ''' This function will display a contacts related details by searching for the entered
        string within the dictionary keys, and then displaying matches in a sorted format.
        It takes one parameter which is the string the user enters'''
    global book
    temp= []
    
    for key in book:                                                                                #Line 98-109 Iterates through dictionary keys checking for matches of 
        if name.lower() in key.lower():                                                             #lowercase versions. If no names were matched the user is told so
            temp.append(key)                                                                        #and the function exited back to the main program body.                                           
    if len(temp)==0:                                                                                #If matches are found they are sorted and printed.                                                  
        print("No names were found that match")
        return False                                                                                
    sort(temp)                                                                                      
    for element in temp:
            print('Name: ',element)
            for elem in book[element]:
                print(elem)
            print()

def delete(name):
    ''' This function takes a string parameter in then uses the display() function to search for
        matches. The user then needs to enter the full name to delete, is asked if sure, then
        deletes the entry from the dictionary'''
    global book

    find = search(name)                                                                                #Line 117-133 searches for a name matching the keyword
    if find == False:                                                                                  #to ensure that the user's saved name is displayed exactly,
        return                                                                                         #which is then entered as-is. Thereafter the user is prompted 
    while True:                                                                                        #for certainty of decision. Afterwards, the program attempts to                                                                 
        remove= input("Please enter the full name of the entry to delete exactly as above:\n")         #delete the dictionary entry, if it fails it informs the user
        check = input("Are you sure you want to delete this contact? Insert y for yes, n for no:\n")  #of incorrect name entry and loops.
        if check == 'y':
            try:
                del book[remove]
                print("Contact deleted succesfully")
                break
            except:
                print("You have entered an incorrect name")
        elif check == 'n':
            break
        else:
            print("Please enter a correct option")

def display_all():
    ''' This function will display all contacts stored in alphabetical order, without any of their
        related details. It has no parameters.'''
    global book
    temp= []

    for key in book:                                                                               #Line 141-143 iterates through dictionary values/contact names
        temp.append(key)                                                                           #and appends to the temp list, thereafter the list sorts the list
    sort(temp)
    i=1
    for name in temp:                                                                              #Line 144-147 prints the contacts alphabetically
        print(i,'-',name,sep='')                                                                   #with number references too 
        i+=1
    
    
# Main Body of the program begins here #

print(''' 
       **************************************************************
       *      This is a Contact Management Application              *
       *      It will allow you to create and manage your contacts  *
       *      Please enjoy using it - Michael Botha (developer)     *
       ************************************************************** ''')

while True:                                                                                         #Line 159 keeps looping the program infinitely unless exited explicitly 
                                                                                                    #Line 161-167 prints the available options for the user 
    print('''                               
     1.) Add new or edit existing contact
     2.) Search for and display details of contact/s
     3.) Delete a contact and all related details
     4.) Display numbered alphabetical list of all contact names
     5.) Exit program
     ''')

    select = input("Please enter the number of the task to perform:\n")                             #Line 169-185, requested option is read, the flow directed accordingly,
                                                                                                    #and the appropriate code executed 
    if (select == '1'): 
        add()
    elif (select =='2'):
        name = input("Please input a keyword to search:\n") 
        search(name)
    elif (select =='3'):
        name = input("Please input a keyword to search:\n")
        delete(name)
    elif (select =='4'):
        display_all()
    elif (select =='5'):    
        break      
    else:
        print("You have entered an incorrect option, Please try again")
        continue



    

 
