# Below class requires much more input checking and exception handling for real world application
class Customer:
    '''The Customer class represents a customer's details in the system'''
    def __init__(self):
        self.__name = None 
        self.__email = None 
        self.__address = None
        self.__bank_details = None 
        self.__coupons = None 
    
    def set_details(self):
        ''' To set all details when a customer is created in a store '''
        print("Please enter your name")
        self.__name = input()
        print("Please enter your email address")
        self.__email = input()
        print("Please enter your postal address")
        self.__address = input() 
        while True:
            print("Would you like to store your credit card details for future pruchases? y or n")
            choice = input()
            if choice =='y':
                print("Please enter your card number")
                self.__bank_details = input()
                break
            elif choice == 'n':
                break
            else:
                print("Please select a valid option")

    def __str__(self):
        ''' Prints a Customer object'''
        return ("---Customer Details---\n" + "Name:" + self.__name + "\n" + "Email:" + self.__email + "\n")

    # All getter definitions follow
    def get_name():
        return self.__name
    def get_email():
        return self.__email
    def get_address():
        return self.__address
    def get_bank_details():
        return __bank_details
    def get_coupons():
        return self.__coupons
    
    # All setter definitions follow
    def set_name():
        name = input("Please input a your name")
        self.__name =  name
    def set_email():
        email = input("Please input a your email")
        self.__email =  email
    def set_address():
        address = input("Please input a your address")
        self.__address =  address
    def set_bank_details():
        bank = input("Please input a your bank details")
        self.__bank_details =  bank
    def set_coupons(coupon):
        self.__coupons =  coupon  
   
# The below class will not be completed for the prototype as employees are not part of the brief
class Employee(Customer):
    ''' Represents an employee in the program'''
    def __init__(self):
        Customer.__init__(self)
        self.__employee_number = None 
        self.__division = None  
        self.__location = None
        self.__priv_level = None 



class UserInterface:
    '''The primary interface whereby a user my access a store, and the required services'''
    def __init__(self,store1 , warehouse1):
        self.__users = []
        self.__user_logins = {}
        self.__logged_in_users = []
        self.__stores = [store1]           # In real system there would be multiple stores fed in. The code has been adapted for only one
        self.__warehouses = [warehouse1]   # In real system there would be multiple warehouses fed in. The code has been adapted for only one

    def user_window1(self):
        '''Presents initial interface to user'''
        print('''
*********************************************************************
                  WELCOME TO AMY'S HARDWARE DISTRIBUTORS                  
*********************************************************************                                                                  
                ''')

        print("What would you like to do?:\n1 > Browse\n2 > Create a profile to purchase goods\n3 > Login")
        choice = input()
        return choice

    def create_user(self):
        '''Creates a customer object and asks for relevant details'''
        customer = Customer()
        customer.set_details()
        self.__users.append(customer)
        name = input("Please enter a user login name:\n")
        password = input("Please enter a login password:\n")
        self.__user_logins[name] = password
        print("User successfully created")

    def login(self):
        '''Validates a username and password, thereafter locates the correct profile and puts it into the logged_in_users list'''
        n =0
        while n != 3:
            name = input("please enter your username or r to return:\n")
            if name == 'r':
                break
            try:
                password = self.__user_logins[name]
                enter_pass = input("Please enter your password:\n")
                if password == enter_pass:
                    j = -1
                    for key in self.__user_logins:                   # Correlate dictionary index and users index to link username with profile
                        j +=1
                        if key == name:
                            break
                    self.__logged_in_users.append(self.__users[j])
                    print("Login successful")
                    return True
                    break
                else:
                    print("You have entered an incorrect password")
                    n +=1
            except:
                print("The username you entered does not exist")

    def store_interface(self):
        '''Interfaces the user to a specifc store. Only one store exists in the prototype'''
        choice = None
        while True:
            print(self.__stores[0].get_storefront())
            choice = input()
            if choice == '1':
                self.__stores[0].display_catalogue()
            elif choice == '2':
                self.__stores[0].search_product()
            elif choice == '3':
                if len(self.__logged_in_users) == 0:
                    print('You must be logged in to place an order')
                else:
                    self.__stores[0].place_order(self.__logged_in_users[0])
            elif choice == '4':
                break
            else:
                print("You have not entered a valid option")
    
    def get_logged(self):
        '''Returns the currently logged in user'''
        return self.__logged_in_users[0]


class Store:
    ''' Represents a store that a customer can interact with '''
    def __init__(self, warehouse1):
        self.__storefront = ''' 
****************************************************************
          WELCOME TO DRILLING, WELDING, & CUTTING GALORE
****************************************************************

What would you like to do?
1 > View the store catalogue
2 > Search for a product
3 > Order a product
4 > Return to previous page
'''
        self.__warehouses = []     # In a real system multiple warehouses would be used but the code is adapted for just one here
        self.__store_name = None
        self.__store_manager = None
        self.store_contact = None 
        self.__warehouses.append(warehouse1) 

    def display_catalogue(self):
        '''Displays all products in the warehouse, with accompanying product number'''
        for product in self.__warehouses[0].get_products():
            print('Product number is:', product[0])
            print(product[1].__str__())
            

    def get_storefront(self):
        '''Storefront getter'''
        return self.__storefront


    def search_product(self):
        '''Searches through all products in the warehouse comparing the customer-provided substring with product description string'''
        substring = input('Please enter the type of item you are looking for e.g. drill:\n').lower()
        matches = []
        for product in self.__warehouses[0].get_products():
            if substring in product[1].get_description().lower():
                matches.append(product)
        for product in matches:
            print('Product number is:', product[0])
            print(product[1].__str__())

    def place_order(self, customer):
        '''Takes a user through the process of making a purchase, which creates an order for the related warehouse'''
        while True:
            print('Please enter the product number of the item you would like to purchase, or r to return')
            product_no = input()
            if product_no == 'r':
                break
            try:
                product = self.__warehouses[0].get_single_product(product_no)
                order = Order(product)
                answer = input("would you like to proceed to checkout, enter y for yes or c to cancel?")
                if answer == 'y':
                    order.set_customer(customer)
                    order.set_delivery_address()
                    order.set_delivery_option()
                    order.payment()
                    self.__warehouses[0].set_orders(order)
                    order.__str__()
                    break
            except:
                print('You have entered an incorrect product number')

                  


class Warehouse:
    ''' Houses all the products available for purchase in a particular product domain '''
    def __init__(self):
        self.__products = {}
        self.__orders = []

    def add_product(self):
        ''' Creates a product and assigns it a warehouse location, known as the product number by customers'''
        location = input("Please enter location to place in warehouse:\n")
        self.__products[location] = ProductType()

    def get_products(self):
        ''' Is a generator function iteratively returning a tuple of warehouse location (seen as item number by customer) and product'''
        for product in self.__products.items():
            yield product

    def get_single_product(self, key):
        return self.__products[key]

    def get_orders(self):
        for product in self.__orders:
            yield product

    def set_orders(self, order_obj):
        self.__orders.append(order_obj)
            

class Order:
    def __init__(self, product):
        self.__product = product
        self.__customer = None
        self.__delivery_address = None
        self.__delivery_option = None

    def __str__(self):
        print("Order details are as follows:\n")
        print(self.__product.__str__())
        print("---Delivery Address---\n", self.__delivery_address, "\n")
        print(self.__customer.__str__())
        
       

    def get_product(self):
        return self.__product

    def set_customer(self, customer):
        self.__customer = customer

    def set_delivery_address(self):
        self.__delivery_address = input('Please enter delivery address:\n')

    def set_delivery_option(self):
        print('''
Please select a delivery option:
1 > Overnight Express
2 > Standard 3-day
''')
        self.__delivery_option = input()

    def payment(self):
                print('''
Please select a payment option:
1 > Credit/Debit card
2 > PayPal
3 > Coupons
''')
                option = input()
                if ((option == '1' ) or (option == '2') or (option == '3')):
                    print("Payment Successful")

        


class ProductType:
    ''' The Product class is used to represent items for sale in a warehouse, where a single Product instantiation
        will represent all details pertaining to numerous items of a particular type. '''

    # Class lists are formed so that all products can use standard inputs for related fields, forcing product capturers to input correct data 
    # Admins will be able to change a list for accommodation of a new item after a change-control process 
    # All lists will contain string types 
    __category_list = ['Drilling','Welding','Wood Work']
    __manufacturer_list = ['Bosch','Makita','Eurolux']
    __description_list = ['Drilling Machine', 'Welding Machine', 'Welding Rods', 'Jigsaw', 'Nails' ]
    __supplier_list = ['Bosch Central', 'Bosch Eastern', 'Central Electics']

    def set_list_generic(self):
        '''Allows editting of the various Class lists'''

        # Line 314-337 is used to set the class list that will be editted #
        choice = None
        while choice != 'r':
            print('Please enter the number corresponding to the list you would like to edit:\n1 > Category\n2 > Manufacturer\n3 > Description\n4 > Suppliers\n5 > Exit ')
            List = input()
            if List == '1':
                List = ProductType.__category_list
                list_name = 'Category'
                break
            elif List == '2':
                List = ProductType.__manufacturer_list
                list_name = 'Manufacturer'
                break
            elif List == '3':
                List = ProductType.__description_list
                list_name = 'Discription'
                break
            elif List == '4':
                List = ProductType.__supplier_list
                list_name = 'Supplier'
                break
            elif List == '5':
                choice = 'r'
            else :
                print('Please enter a correct option')

        while choice != 'r':
            print("Would you like to delete or add a " + list_name + "? Enter d for delete, a for add, or r to return:")
            choice = input().lower()

            # Line 344-372 guides the user through the process of deleting a list element #
            if choice == 'd':
                print('Would you like to display all current', list_name, 'or search for a specific one to delete? Enter d for display or s for search:')
                choice2 = input().lower()
                if choice2 == 'd':
                    for description in List:
                        print(description)
                elif choice2 == 's':
                    searchMatches = []
                    subString = input("Please enter a portion of the " + list_name + " to search for:\n")
                    for string in List:
                        if subString.lower() in string.lower():
                            searchMatches.append(string)
                    if len(searchMatches) == 0:
                        print("No matches found")
                    else:
                        print("Matches:")
                        for match in searchMatches:
                            print(match)
                else:
                    print("Please enter a correct option")

                elemToDel = input("Please enter the " + list_name + " to delete as displayed above:\n")
                try:
                    index = List.index(elemToDel)
                    del List[index]
                    choice = 'r'
                    print("Delete Successful")
                except ValueError:
                    print("You need to enter the exact value as seen displayed above")

            # Line 375-392 guides the user through the process of adding a list element #
            elif choice == 'a':
                print("Please enter a ",list_name,":")
                description = input()
                for current_description in List:
                    if description in current_description:
                        print("That description already exists")
                        break
                while True:
                    print("Are you sure you want to add", '"',description ,'" ? Enter y for yes, or r to return')
                    choice3 = input().lower()
                    if choice3 == 'y':
                        List.append(description)
                        choice = 'r'
                        break
                    elif choice3 == 'r':
                        break
                    else: 
                        print("Please enter a valid input")

    def __init__(self):
        ''' The __init__ method creates the required data attributes requried to represent a product type available in the store'''

        # All data attributes will contain string types and be converted by another class as required
        self.__category = None 
        self.__manufacturer = None
        self.__description = None 
        self.__model = None
        self.__price = None
        self.__suppliers = []  
        self.__serial_numbers = []     # This list will be used both to store the various item serial numbers, and to calculate the corresponding number of items in stock

        ##Below would force an employee to enter all the required fields upon creation of a product
        #while(
            #(self.__category == None) 
            #or (self.__manufacturer == None) 
            #or (self.__description == None) 
            #or (len(self.__suppliers)== 0) 
            #or (self.__model == None) 
            #or (self.__price == None) 
            #or (len(self.__suppliers)== 0) 
            #or (len(self.__serial_numbers) == 0)):          
            #print("You need to add an initial value to each of the product's relevant fields")
            #self.set_attribute_generic()
            #print(self)
    

    def __str__(self):
        '''Allows a product instantion to be printed, which will display the current value of all related data attributes'''

        return ("---PRODUCT DETAILS---\n" + "Category: " + str(self.__category) + "\nManufacturer: " + str(self.__manufacturer) + "\nDescription: " + str(self.__description) +\
                "\nModel: " + str(self.__model) + "\nPrice: " + str(self.__price) + "\nSupplier: " + str(self.__suppliers) + "\nNumber in stock: " + str(len(self.__serial_numbers)) + '\n\n')


    def set_attribute_generic(self):
        ''' Allows the editting of any of an objects data attributes ''' 

        # Line 432-454 is used to set which data attribute will be editted 
        choice = None
        while choice != 'r':
            print('Please enter the number corresponding to the product attribute you would like to add/edit:\n1 > Category\n2 > Manufacturer\n3 > Description\n4 > Model\n5 > Price\n6 > Serial Numbers\n7 > Supplier\n8 > Exit ')
            attribute = input()
            if attribute == '1':
                class_list = ProductType.__category_list
                att_name = 'Category'
                break
            elif attribute == '2':
                class_list = ProductType.__manufacturer_list
                att_name = 'Manufacturer'
                break
            elif attribute == '3':
                class_list = ProductType.__description_list          
                att_name = 'Description'
                break
            elif attribute == '7':
                class_list = ProductType.__supplier_list          
                att_name = 'Supplier'
                break
            elif ((int(attribute) > 3) and (int(attribute) < 7) or (int(attribute) == 8)):
                break 
            else:
                print('You have made an incorrect selection')

        if ((attribute == '1') or (attribute == '2') or (attribute == '3') or (attribute == '7')):
            print('Please select a', att_name, 'from the available options below')
            n = 1
            for option in class_list:
                print(n," > ", option )
                n += 1
            while True:
                try:
                    index = int(input()) -1
                except ValueError:
                    print("You have not entered a number, or you have put a decimal place. Please try again")
                if ((index < 0) or (index > n)):
                    print("You have not entered a number in the range available. Please try again")
                else:
                    break

            if (attribute == '1'):
                self.__category = class_list[index]
            elif (attribute == '2'):
                self.__manufacturer = class_list[index]
            elif (attribute == '3'):
                self.__description = class_list[index]
            elif (attribute == '7'):
                self.__suppliers.append(class_list[index])

        else:
            if attribute == '4':
                model = input('Please enter a model:\n')
                self.__model = model 
            elif attribute == '5':
                while True:
                    price = input('Please enter a price in xx.xx format:\n')
                    try:
                        float(price)
                        self.__price = price
                        break
                    except:
                        print("You have used a incorrect value")                     
            elif attribute == '6':
                serial = input('Please enter serial number:\n')
                self.__serial_numbers.append(serial)

    def get_description(self):
        return self.__description

## Main body of code follows ##

#Test data set up and main objects instantiation
main_warehouse = Warehouse()
product1 = ProductType()
product2 = ProductType()
product3 = ProductType()
product4 = ProductType()
product1._ProductType__category = 'Drilling'
product1._ProductType__manufacturer = 'Bosch'
product1._ProductType__description = 'Drilling Machine'
product1._ProductType__model = '750W Home Use'
product1._ProductType__price = 1500.00
product1._ProductType__suppliers = ['Bosch Central', 'Bosch Eastern']
product1._ProductType__serial_numbers = ['abc123', 'abc124', 'abc125','abc126']
product2._ProductType__category = 'welding'
product2._ProductType__manufacturer = 'Eurolux'
product2._ProductType__description = 'welding rods'
product2._ProductType__model = 'ARC welding 100 pack'
product2._ProductType__price = 300.00
product2._ProductType__suppliers = ['central Electrics']
product2._ProductType__serial_numbers = ['def123', 'def124', 'def125']
product3._ProductType__category = 'Wood work'
product3._ProductType__manufacturer = 'Bosch'
product3._ProductType__description = 'Jigsaw'
product3._ProductType__model = '1000W Industrial'
product3._ProductType__price = 3000.00
product3._ProductType__suppliers = ['Bosch Central', 'Bosch Eastern']
product3._ProductType__serial_numbers = ['ghi123', 'ghi124', 'ghi125','ghi126']
product4._ProductType__category = 'Welding'
product4._ProductType__manufacturer = 'Eurolux'
product4._ProductType__description = 'Welding Machine'
product4._ProductType__model = 'Industrial Inverter Welder'
product4._ProductType__price = 4000.00
product4._ProductType__suppliers = ['central Electrics']
product4._ProductType__serial_numbers = ['rst123', 'rst124', 'rst125']
main_warehouse._Warehouse__products = { 'A55' : product1, 'A45' : product2 , 'A35' : product3, 'B95' : product4 }
main_store = Store(main_warehouse)
interface = UserInterface(main_store, main_warehouse)
customer1 = Customer()
customer1._Customer__name = "Michael Botha"
customer1._Customer__email = "mbotha88@gmail.com"
customer1._Customer__address = "7 Grenich Village, 6 Teviot Place, Howick, KZN, South Africa "
interface._UserInterface__users = [customer1]
interface._UserInterface__user_logins = {'mike' : 'unsecure123'}

#Interconnecting and using objects
while True:
    choice = interface.user_window1()
    if choice == '1':
        interface.store_interface()
    elif choice == '2':
        interface.create_user()
    elif choice == '3':
        validate = interface.login()
        if validate == True:
            interface.store_interface()
