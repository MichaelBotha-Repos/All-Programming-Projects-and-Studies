'''
    The following code checks to see whether a postal identifier/code
    is in the correct format according the UK system:
    
   {    }.......= Outcode
        {   }...= incode
    xxxx xxx
         {  }...= Unit
   {      }.....= Sector
   {    }.......= Subdistrict
   {   }........= District
   {  }.........= Area

    General:
    # Total legth = 5-7 
    # Alphanumeric characters only 
    # 1st position does not contain the letters Q, V, X 
    # 2nd position does not contain the letters I, J, Z
    # Only A, B, C, D, E, F, G, H, J, K, S, T, U, W used in 3rd position
    # Always used capitals

    Outcode:
    # 2-4 characters then space
    # Always begins with letter
    # Ends in letter or number

    Incode:
    # Always 3 characters
    # Format is always: Numeric, Alpha, Alpha
    # C, I, K, M, O, V never used

    Information found at:
    https://www.mrs.org.uk/pdf/postcodeformat.pdf
    https://ideal-postcodes.co.uk/guides/uk-postcode-format

'''

import re

code = input("Please enter the postal code:\n").upper()

# Test for correct length of total code
if len(code) < 6 or len(code) > 8:
    print("incorrect length")
    
# Test for only alphanumeric characters   
count = 0
for char in code:
    count += 1
    if ord(char) > 90 or (ord(char) < 48 and ord(char) != 32)\
       or (ord(char) > 57 and ord(char) < 65) :
        print("Incorrect character used at character", count, "from left side")
        break

# Check outcode is 2-4 characters then space
if (not re.match(r'..\s', code))and (not re.match(r'...\s', code))\
   and (not re.match(r'....\s', code)):
    print('Should be 2-4 characters and then a space')

# Check correct first letter 
if re.match(r'[Q, V, X]', code) or (ord(code[0])) < 65 \
    or (ord(code[0])) > 90:
    print('Incorrect letter used as first character')

# Check correct second character
if re.match(r'.[I, J, Z]', code):
    print('Incorrect letter used as second character')

# Check correct third character
if not re.match(r'..[A, B, C, D, E, F, G, H, J, K, S, T, U, W]', code):
    print('Incorrect letter used as third character')

# Check incode has 3 characters
if not re.search(r'\s...$', code):
    print("The incode must have three characters")
    
# Check incode in format: Numeric, Alpha, Alpha
if not re.search(r'\d\w\w', code):
    print('Must be in format NumericAlphaAlpha')


# Ensure correct letters are used in incode
if re.search(r'[C, I, K, M, O, V]..$', code)\
or re.search(r'.[C, I, K, M, O, V].$', code)\
or re.search(r'.[C, I, K, M, O, V]$', code):
    print('Incorrect letter used in incode')

















    
        
  
