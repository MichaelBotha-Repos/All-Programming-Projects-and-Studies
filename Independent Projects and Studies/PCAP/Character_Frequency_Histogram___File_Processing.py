from os import strerror

dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'p':0, \
    'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'x':0, 'y':0, 'z':0}
try:
    src = (str(input('Please enter a file path to evaluate')))
    src = src.lower()
    
    for line in open(src, "rt"):
        for char in line:
            for key in dict:
                if char == key:
                    dict[key]+=1

    for char in dict:
        if dict[char]> 0:
            print(char, '->', dict[char])

except IOError as error:
    print('error is:', strerror(error.errno))
    
    