#This is the 3rd capstone project of the HyperionDev SE course, T32#

#========Class definitions==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_product(self):
        '''
        Code to return the product
        '''
        return self.product

    def get_cost(self):
        '''
        Code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_code(self):
        '''
        Code to return the code of the shoe
        '''
        return self.code

    def get_quantity(self):
        '''
        Code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        This code returns a string representation of a class.
        '''
        return f'''{self.product} {self.code} ({self.country}), Cost: {self.cost}, Quantity: {self.quantity}'''


#=============Shoe list===========
'''
Initiate an empty list to store the objects of shoes.
Note that on re-start the list is repopulated from the inventory.txt file
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function opens the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. ##You must use the try-except in this function
    for error handling.## Remember to skip the first line using your code.
    '''
    try:
        file = open('inventory.txt', 'r', encoding='utf-8')
        shoes = file.readlines()
        for shoe in shoes:
            shoe = shoe.replace("\n", "")
            shoe = shoe.split(",")
            if shoe[0] == "Country":
                pass
            else:
                shoe_ = Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4])
                shoe_list.append(shoe_)
                
    except FileNotFoundError:
           print("Check that file 'inventory.txt' is in the correct folder")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    new_product = input("What is the name of the product? ")
    new_code = input("Enter the product code: ")
    new_country = input("Enter the country: ")
    new_cost = input("Enter the cost: ")
    new_quantity = input("Enter the quantity: ")
    #creates a new Shoe object with the input data
    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    #appends to the list of shoes
    shoe_list.append(new_shoe)
    
    #Reads the current shoe inventory to a list from the inventory.txt file and then adds the new shoe
    #Then writes the updated inventory to the inventory.txt file
    current_inventory = []
    with open('inventory.txt', 'r+') as inventory:
        for line in inventory.readlines():
                current_inventory.append(line)

    if current_inventory[-1].__contains__("\n") == False:
        current_inventory.append("\n")
    current_inventory.append(f"{new_country},{new_code},{new_product},{new_cost},{new_quantity}\n")
    updated_inventory_to_write_to_file = current_inventory

    with open('inventory.txt', 'w+') as inventory:
        for items in updated_inventory_to_write_to_file:
            inventory.write(items)
        print(f'''New product added successfully
Please restart the programme.''')
 
def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    print(f'''=======Inventory======

Product, Code (Country), Cost, Quantity in stock\n''')

    for index, product in enumerate(shoe_list):
        print(f" {index+1} {product}")

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest = shoe_list[0]
    for product in shoe_list:
        if int(product.get_quantity()) < int(lowest.get_quantity()):
            lowest = product
    print(f"The lowest stocked product is {lowest.__str__()}")

    #ask user how much they want to restock
    restock = int(input("How much do you want to add to this quantity?: "))
    

    #open the file in read mode first to calculate the updated quantity
    with open('inventory.txt', 'r') as inventory:
        for line in inventory.readlines():
            line = line.replace("\n", "")
            line = line.split(",")
            if line[1] == lowest.get_code():
                current_quantity = int(line[-1])
                new_quantity = current_quantity + restock
                line[-1] = new_quantity
                #print(line) #class 'list' where line[-1] is the updated quantity
                line[-1] = str(line[-1]) #convert element 4 back to string
                line_to_add = ','.join(line)
                #print(line_to_add)

    #then open in write mode to update the inventory file
    
    shoe_to_update = []
    with open('inventory.txt', 'r+') as inventory:
        for line in inventory.readlines():
            if line.__contains__(lowest.get_code()):
                pass
            else:
                shoe_to_update.append(line)
    if shoe_to_update[-1].__contains__("\n") == False:
        shoe_to_update.append("\n")
    shoe_to_update.append(f"{line_to_add}\n")
    #print(shoe_to_update)

    #Now write the updated inventory to the inventory.txt file

    with open('inventory.txt', 'w+') as inventory:
        for items in shoe_to_update:
            inventory.write(items)
        print(f"Selected product stock updated from {current_quantity} to {new_quantity} successfully")

def search_shoe():
    '''
     This function searches for a shoe from the list
     using the shoe code and the print the object
    '''
    code_input = input("Enter the code of the product you want to retrieve: ")
    
    for product in shoe_list:
        if code_input == product.get_code():
            print(f"\n{product}")
        else:
            pass

def value_per_item():
    '''
    This function calculates the total value for each item and prints
    the information to the console for all shoes
    '''
    for shoe in shoe_list:
        print(shoe)

    for product in shoe_list:
        cost = float(product.get_cost())
        quantity = float(product.get_quantity())
        print(f"Total value of {product.get_product()} = {cost*quantity}")

def highest_qty():
    '''
    This code determines the product with the highest quantity and
    prints that shoe as being for sale.
    '''
    highest = shoe_list[0]
    for product in shoe_list:
        if int(product.get_quantity()) > int(highest.get_quantity()):
            highest = product

    #prints that the most stocked product is for sale
    print(f"{highest.get_product()} is for sale!")
        

#==========Main Menu=============
'''
The following menu executes each function above inside a while loop
'''
print(f''' Welcome to the Inventory Program

Type "all shoes" to view all shoes in the inventory
Type "search"  to search by code
Type "value" to calculate the total value in stock for each item
Type "highest" to find the most stocked shoe
Type "restock" to restock the least stocked shoe
Type "add shoe" to add a new shoe product to the inventory
Type "quit" to end the programme
''')

#initialise database
read_shoes_data()

user_entered = input("")

while user_entered != "quit":
 if user_entered == "all shoes":
    read_shoes_data()
    file = open('inventory.txt', 'r', encoding='utf-8')
    shoes = file.readlines()
    shoe_list = shoe_list[0:(len(shoes) - 1)] #Makes sure entries aren't repeated
    view_all()
    user_entered = input("\nEnter another function or quit: ")
 if user_entered == "search":
    search_shoe()
    user_entered = input("\nEnter another function or quit: ")
 if user_entered == "value":
    value_per_item()
    user_entered = input("\nEnter another function or quit: ")
 if user_entered == "highest":
    highest_qty()
    user_entered = input("\nEnter another function or quit: ")
 if user_entered == "restock":
    re_stock()
    print('''Database updated. 
    Now quit and restart the program.''')
    user_entered = input("\nEnter quit: ")
 if user_entered == "add shoe":
    capture_shoes()
    user_entered = input("\nEnter another function or quit: ")
 elif user_entered == "quit":
    quit
 else:
    print(f"Invalid input")
    user_entered = input("Enter a function or quit: ")
print("Goodbye!")