count = 0
n = 0

def tower(a, b, c):
    global count
    global n
    
    if(len(b) == n):
        return count 
    else:
        if(len(a) > 0):
            if(len(b) == 0):
                b.append(a[-1])
                del a[-1]
                count += 1
                print(a,b,c)
                return tower(a, b, c)
            elif(len(c) == 0):
                c.append(a[-1])
                del a[-1]
                count += 1
                print(a,b,c)
                return tower(a, b, c)
            elif(b[-1] > a[-1]):
                b.append(a[-1])
                del a[-1]
                count += 1
                print(a,b,c)
                return tower(a, b, c)
            elif(c[-1] > a[-1]):
                c.append(a[-1])
                del a[-1]
                count += 1
                print(a,b,c)
                return tower(a, b, c)
         
        '''           
            elif len(b)>0:
                if(len(a) == 0):
                    a.append(b[-1])
                    del b[-1]
                    count += 1
                    print(a,b,c)
                    return tower(c, a, b)
                elif(len(c) == 0):
                    c.append(b[-1])
                    del b[-1]
                    count += 1
                    print(a,b,c)
                    return tower(c, a, b)
                elif(a[-1] > b[-1]):
                    a.append(b[-1])
                    del b[-1]
                    count += 1
                    print(a,b,c)
                    return tower(c, a, b)
                elif(c[-1] > b[-1]):
                    c.append(b[-1])
                    del b[-1]
                    count += 1
                    print(a,b,c)
                    return tower(c, a, b) 
        '''
                
                elif len(c)>0:
                    if(len(a) == 0):
                        a.append(c[-1])
                        del c[-1]
                        count += 1
                        print(a,b,c)
                        return tower(c, a, b)
                    elif(len(b) == 0):
                        b.append(c[-1])
                        del b[-1]
                        count += 1
                        print(a,b,c)
                        return tower(c, a, b)
                    elif(c[-1] > b[-1]):
                        a.append(b[-1])
                        del b[-1]
                        count += 1
                        print(a,b,c)
                        return tower(c, a, b)
                    elif(c[-1] > b[-1]):
                        c.append(b[-1])
                        del b[-1]
                        count += 1
                        print(a,b,c)
                        return tower(c, a, b) 
 '''

while True:
    try:
        n = int(input('please enter the number of disks:\n'))
        break

    except:
        continue

stack_a = [i + 1 for i in reversed(range(n))]
stack_b = []
stack_c = []

print(stack_a, stack_b, stack_c)

print(tower(stack_a, stack_b, stack_c))


