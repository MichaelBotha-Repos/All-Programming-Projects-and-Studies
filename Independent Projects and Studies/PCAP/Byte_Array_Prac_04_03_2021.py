from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = ord('a') + i

try:
    bf = open('C:/Users/Michael Botha/Desktop/Coding/Programs/bytearray.bin', 'wb')
    print('bytes written:', bf.write(data))
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

data = bytearray(10)

try:
    bf = open('C:/Users/Michael Botha/Desktop/Coding/Programs/bytearray.bin', 'rb')
    print('bytes read:',bf.readinto(data))
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
