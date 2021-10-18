'''
Define the BankAccount class which has attributes for checking and savings.
Use the Python convention to make these attributes private.
Create the getters get_checking and get_savings,
and create the setters set_check and set_savings.
'''

class BankAccount:
    def __init__(self):
        self.__check = None
        self.__savings = None

    def set_checking(self, check):
        if type(check).__name__ != 'float':
            print('A float is the required type')
        else:
            self.__check = check

    def get_checking(self):
        return self.__check

    def set_savings(self, savings):
        if type(savings).__name__ != 'float':
            print('A float is the required type')
        else:
            self.__savings = savings
    
    def get_savings(self):
        return self.__savings

my_account = BankAccount()
my_account.set_checking(523)
my_account.set_checking('523')
my_account.set_checking(523.48)
print(my_account.get_checking())
my_account.set_savings(386.15)
print(my_account.get_savings())
