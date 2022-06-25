import shelve

my_shelve = shelve.open("my.shlv")
my_shelve['one'] = 'hello'
my_shelve['two'] = 'goodbye'
my_shelve.close()

my_shelve_r = shelve.open('my.shlv')
print(my_shelve_r['one'])
