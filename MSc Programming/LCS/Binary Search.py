
import random 

def binary_search(List, Target):
    while len(List) >1:    
        if (len(List)%2) == 0:
            if (List[len(List)//2 -1])== Target:
                print(True)
                return
            else:
                if Target < (List[(len(List)//2-1)]) :
                    return binary_search(List[0:len(List)//2], Target)
                else:
                    return binary_search(List[len(List)//2 +1:], Target)
        else:
            if (List[(len(List)-1)//2])== Target:
                print(True)
                return
            else:
                if Target < (List[(len(List)-1)//2]) :
                    return binary_search(List[0:len(List)//2], Target)
                else:
                   return binary_search(List[len(List)//2 +1:], Target)
    else:
        print(False)
    

lst = [ random.randrange(1000000) for i in range(100000)]
lst.sort()
print(lst)

T = 8
binary_search(lst,T)

