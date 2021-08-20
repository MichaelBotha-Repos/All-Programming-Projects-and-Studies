''' This is a program implementing the unsecure Caesar Cypher with rot values'''

strn = input('Please insert your plain-text message:\n')
rot = int(input('Please insert your desired shift value: from 1 to 25\n'))
encrp = ''
#code = None

for char in strn:
    code = ord(char)
    #if (code <0) or (code >128):
       # print(char,'is not a valid entry')
        #break
    if ((code <65) or ((code >90) & (code <97)) or ((code >122) & (code <128))): # Test for special characters
        encrp += char                                                            # Add unchanged if special character
        continue
    
    cod_rot= code + rot
    if code <91:
        if cod_rot <91:
            encrp += chr(cod_rot)
            continue
        else:
            encrp = chr(64 + cod_rot - 90)
            continue

    if code >91:
        if cod_rot <123:
            encrp += chr(cod_rot)
        else:
            encrp += chr(96 + cod_rot - 122)
    

        
print(encrp)

