''' This program tests two inputted strings to determine whether the second is an anagram of the first'''
''' The program ignores spaces, and treats upper and lower-case characters as equal'''
''' Two empty strings are not equal '''

def squ_low(num):                           # Function asks for string input, removes spaces, makes all lower-case
    print("Please input your",num,"word")   # and returns the string. num is input number
    strn = input()                  
    strn = strn.replace(' ','')
    strn = strn.lower()          
    return strn

def sum(string):                            # Funtion accepts string argument and calculates the sum of its code points
    total = 0   
    for char in string:
        co_po = ord(char)
        total += co_po
    return total   

string1 = squ_low(1)
string2 = squ_low(2)

total1 = sum(string1)
total2 = sum(string2)

if total1 == total2:
    print('Anagrams')
else:
    print('Not anagrams')
