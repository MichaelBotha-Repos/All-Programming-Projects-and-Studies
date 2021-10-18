# Import the module required for interfacing with MYSQL database
import mysql.connector 
from mysql.connector import Error

#Create a function to write to the database
def database_write(query):
    ''' Used to write to the database '''
    connection = None
    connection = mysql.connector.connect(host = 'localhost', 
                                         user = 'root', 
                                        passwd = 'pass',
                                        database = 'OnlineStore')

    cursor = connection.cursor(buffered = True)
    cursor.execute(query)
    connection.commit()

#Create a function to read from the database
def database_read(query):
    ''' Used to read from the database '''
    connection = None
    connection = mysql.connector.connect(host = 'localhost', 
                                         user = 'root', 
                                        passwd = 'pass',
                                        database = 'OnlineStore')
    result = None
    cursor = connection.cursor(buffered = True)
    cursor.execute(query)
    result = cursor.fetchall()
    return result


# Below class requires much more input checking and exception handling for real world application
class Customer:
    '''The Customer class represents a customer's details in the database'''

    def __init__(self):
        ''' The Customer object's attributes are created and stored only temporarily when called by the UserInterface object, to be able to update the relevant database table '''
        self.__first_name = None 
        self.__last_name = None
        self.__email = None 
        self.__cell = None
        self.__ID = None
        self.__bank_name = None
        self.__card_number = None
        self.__name_on_card = None
    
    def set_details(self):
        ''' To set all details when a customer is created in a store, so as to populate the CustomerDetails & CustomerFinancialDetails database tables '''
        print("Please enter your first name")
        self.__first_name = input()
        print("Please enter your last name")
        self.__last_name = input()
        print("Please enter your email address")
        self.__email = input()
        print("Please enter your cell number")
        self.__cell = input() 

        statement = "INSERT INTO CustomerDetails VALUES('"+ self.__first_name+"','"+ self.__last_name+"','"+self.__email+"','"+self.__cell+"',NULL);"
        database_write(statement)
        
        #Set bank details
        while True:
            print("Would you like to store your credit card details for future pruchases? y or n")
            choice = input()
            if choice =='y':
                print("Please enter your bank name")
                self.__bank_name = input()
                print("Please enter your card number")
                self.__card_number = input()
                print("Please enter the name on your card")
                self.__name_on_card = input()
                statement = "SELECT customerID FROM CustomerDetails WHERE firstName='"+ self.__first_name+"' AND lastName='"+ self.__last_name+"' AND email='"+self.__email+"';"
                self.__ID = database_read(statement)[0][0]
                statement = "INSERT INTO CustomerFinancialDetails VALUES('"+ str(self.__ID)+"','"+ self.__bank_name+"','"+self.__card_number+"','"+self.__name_on_card+"');"
                database_write(statement)
                break
            elif choice == 'n':
                break
            else:
                print("Please select a valid option")

    def get_ID(self):
      return self.__ID
   
# The below class will not be completed for the prototype as employees will have a separate front-end application
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
        '''Creates a customer object with all relevant details, as well as login details. Updates LoginDetails database table'''
        customer = Customer()
        customer.set_details()
        ID = customer.get_ID()
        username = input("Please enter a user login name:\n")
        password = input("Please enter a login password:\n")
        statement = "INSERT INTO LoginDetails VALUES('"+ str(ID)+"','" + username + "','" + password + "', FALSE);"
        database_write(statement)
        print("User successfully created")

    def login(self):
        '''Validates a username and password, thereafter sets the logged in flag for the user in the database LoginDetails table'''
        n =0
        while n != 3:
            username = input("please enter your username or r to return:\n")
            if username == 'r':
                break
            try:
                statement = "SELECT password FROM LoginDetails WHERE username='"+ username+"';"
                password = database_read(statement)[0][0]
                enter_pass = input("Please enter your password:\n")
                if password == enter_pass:
                    statement = "UPDATE LoginDetails SET loggedIn = True WHERE username = '" + username + "';"
                    database_write(statement)
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
                statement = "SELECT COUNT(*) FROM LoginDetails WHERE loggedIn = TRUE"
                logged_in_count = database_read(statement)
                if logged_in_count[0][0] == 0:
                    print('You must be logged in to place an order')
                else:
                    statement = "SELECT customerID FROM LoginDetails WHERE loggedIn = TRUE;"
                    customer_ID = database_read(statement)[0][0]
                    self.__stores[0].place_order(customer_ID)
            elif choice == '4':
                break
            else:
                print("You have not entered a valid option")


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
        self.__warehouses.append(warehouse1) 

    def display_catalogue(self):
        '''Displays all products in the warehouse with relevant details, with accompanying product number, and stock count'''
        self.__warehouses[0].print_product(self.__warehouses[0].get_products())
            
    def get_storefront(self):
        '''Storefront getter'''
        return self.__storefront

    def search_product(self):
        '''Searches through all products in the warehouse comparing the customer-provided substring with product description string'''
        substring = input('Please enter the type of item you are looking for e.g. drill:\n').lower()
        matches = []
        product_details = []
        for product in self.__warehouses[0].get_product_description():
            if ((substring in product) and (product not in matches)):
                matches.append(product)
        for description in matches:
            statement = "SELECT * FROM Products WHERE description = '" + description + "';"
            product_tuple = database_read(statement)
            for row in product_tuple:
                for value in row:
                    product_details.append(value)
            self.__warehouses[0].print_product(product_details)
            product_details = []

    def place_order(self, customer_ID):
        '''Takes a user through the process of making a purchase, which creates an order for the related warehouse'''
        while True:
            print('Please enter the product number of the item you would like to purchase, or r to return')
            product_no = input()
            if product_no == 'r':
                break
            try:
                order = Order(product_no, customer_ID)
                answer = input("would you like to proceed to checkout, enter y for yes or c to cancel?: ")
                if answer == 'y':
                    order.set_details()
                    order.set_delivery_address()
                    order.payment()
                    order.__str__()
                    break
            except:
                print('You have entered an incorrect product number')


class Warehouse:
    ''' Houses all the products available for purchase in a particular product domain '''

    def print_product(self, product_list):
        ''' Accepts list of product details and prints in correct format with available stock'''
        n =1
        for value in product_list:
            if n == 1:
                print("--Product Details--\nManufacturer :", value)
                n +=1
            elif n == 2:
                print("Description :", value)
                n +=1
            elif n == 3:
                print("Model :", value)
                n +=1
            elif n == 4:
                print("Category :", value)
                n +=1
            elif n == 5:
                print("Price :", value)
                n +=1
            elif n == 6:
                print("ProductID:", value)
                statement = "SELECT COUNT(*) productID FROM Stock WHERE productID= '" + str(value) + "';" 
                stock = database_read(statement)
                print("Number in stock:", stock[0][0], '\n')
                n = 1

    def get_products(self):
        ''' Fetches all products and their details from the database and formats into list to return to calling code'''
        products_list = []
        statement = "SELECT * FROM Products;"
        products_tuple = database_read(statement)
        for row in products_tuple:
            for value in row:
                products_list.append(value)
        return products_list

    def get_product_description(self):
        ''' Fetches all products' descriptions for further processing by Python code '''
        products_description = []
        statement = "SELECT description FROM Products;"
        description_list = database_read(statement)
        for row in description_list:
            for value in row:
                products_description.append(value)
        return products_description
            

class Order:
    ''' Takes a customer through the process of purchasing a product, and updates the database with relevant information '''

    def __init__(self, product_ID, customer_ID):
        ''' Creates variables stored temporarily during order processing so as to update database '''
        self.__product_ID = product_ID
        self.__customer_ID = customer_ID

    def __str__(self):
        ''' Prints an order object's respective details '''
        print(self.__customer_ID)
        statement1 = "SELECT * FROM CustomerDetails WHERE CustomerID=" + str(self.__customer_ID) + ";"
        customer_details = database_read(statement1)
        statement2 = "SELECT houseNumber, street, province, code, country FROM CustomerAddress WHERE CustomerID=" + str(self.__customer_ID) + ";"
        address_details = database_read(statement2)
        statement3 = "SELECT * FROM Products WHERE productID=" + str(self.__product_ID) + ";"
        product_details = database_read(statement3)

        print("<--ORDER DETAILS-->")
        headings = ['-Customer Details-\nFirstname:',
                   'Lastname:', 
                   'Email:', 
                   'Cell:', 
                   'CustomerID:',
                   'House Number:',
                   'Street:',
                   'Province:',
                   'Postal Code:',
                   'Country:',
                   '-Product details-\nManufacturer:',
                   'Description:',
                   'Model:',
                   'Category:',
                   'Price:',
                   'ProductID:']
        n = 0
        for data in [customer_details, address_details, product_details ]:
            for row in data:
                for value in row:
                    print(headings[n], value)
                    n+=1

      
    def set_details(self):
        ''' Writes relevant order details to database order table '''
        print('''
Please select a delivery option:
1 > Overnight Express
2 > Standard 3-day
''')
        delivery_option = input()
        statement = "INSERT INTO Orders VALUES(" + str(self.__customer_ID) + "," + str(self.__product_ID) + ",1 ," + delivery_option + ");"
        database_write(statement)

    def set_delivery_address(self):
        print("Please enter your delivery details below")
        house_number = input("Please enter house number: ")
        street = input("Please enter street: ")
        province = input("Please enter province: ")
        code = input("Please enter postal code: ")
        country = input("Please enter country: ")
        statement = "INSERT INTO CustomerAddress VALUES(" + str(self.__customer_ID) + ",'" + house_number + "','" + street + "','" + province + "'," + code + ",'" + country + "');"
        database_write(statement)

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


## Main body of code follows ##

#Main object instantiations
main_warehouse = Warehouse()
main_store = Store(main_warehouse)
interface = UserInterface(main_store, main_warehouse)


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
