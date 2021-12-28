import re

for item in dir(re.match):
    print(item)

my_string = "The lazy fox jumped over the rusty fence"
my_string2 = 'fox'
pattern = r'fox'

match = re.match(pattern, my_string2)

print(match)

