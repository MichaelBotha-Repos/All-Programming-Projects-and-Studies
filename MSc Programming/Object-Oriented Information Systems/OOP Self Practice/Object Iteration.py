'''This module implements the Fun data structure where various users
   can work as a team on a single shared object.
'''

class Fun:
    ''' The class represents a shared fun value cnt 
        and activities to do with it.
    '''

    cnt = 0
 
    def __init__(self):
        print(Fun.cnt)

    def increment(self):
        '''Increments class variable cnt'''
        Fun.cnt+=1
        print(Fun.cnt)


#Main control flow begins here
amy = Fun()
michael = Fun()
charmaine = Fun()
Johan = Fun()

for object in (amy, michael, charmaine, Johan):
    object.inc()    
