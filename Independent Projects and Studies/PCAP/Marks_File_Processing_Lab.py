from os import strerror

src_file = input("please insert the file path")

try:
    dict = {}
    for line in open(src_file):
        
        value = ''
        key = ''
        for char in line:
            if (char == '0') or (char == '1') or (char == '2')or (char == '3')or (char == '4')or (char == '5')\
                or (char == '6')or (char == '7') or (char == '8')or (char == '9')or (char == '.'):
                  value += char
            else:
                if char != '\n':
                     key += char
            
        dict[key]= value
        

    print(dict)


except IOError as Error:
    print( 'Error is:', Error.strerror(errno))
    