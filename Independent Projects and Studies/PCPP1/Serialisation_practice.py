import pickle 

'''
my_dict = {1 : ['a', 'b', 'c'], 2 : ['d', 'e', 'f'] }

with open('store.pckl', 'wb') as file_out:
    pickle.dump(my_dict, file_out)
'''

with open('store.pckl', 'rb') as file_in:
    my_dict = pickle.load(file_in)

print(my_dict)