#=====importing libraries===========

# Import date class from datetime module to get current date
from datetime import date


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#Read usernames and passwords from the user.txt file. user.txt must read "admin, adm1n, "
users_file = open("user.txt", "r")
usernames = users_file.read() #stores the contents of the .txt file as a string
users_file.close()
#print(usernames)

#format usernames and store in a list
usernames = usernames.replace(" ","")
usernames = usernames.replace("\n","")
users_split = usernames.split(",")
print(users_split)

#Ask user for their username store in variable
username_input = input("Please enter your username: ")

#check if username is in database and allow login if it matches the password
while username_input not in users_split:
    print("User not found")
    username_input = input("Please enter your username: ")

while username_input in users_split:
 password_input = input("Please enter your password: ")
 if password_input == users_split[users_split.index(username_input) + 1]:
  print("Login successful")
  break
 else:
  print("Username or password are incorrect. Try again")
  username_input = input("Please enter your username: ")


while True:
    #present the menu to the user and 
    #convert the user input to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user (admin only)
a - Adding a task
va - View all tasks
vm - view my task
s - view stats (admin only)
e - Exit
: ''').lower()

    if menu == 'r' and username_input == 'admin':
        pass
        '''In this block only if logged in as admin:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise present a relevant message.'''
        new_user = input("Enter a new username: ")
        if new_user in users_split:
            print("Username already in database")
            break
        new_pwd = input("Enter a password: ")
        new_pwd_confirm = input("Please confirm the password: ")
        if new_pwd == new_pwd_confirm:
         with open('user.txt', 'a') as users:
          users.write(f"\n{new_user}, {new_pwd},")
          print("User added")
        else:
            print("Please try again")

    #if attempting to use the register feature not as admin, display appropriate message
    elif menu == 'r' and username_input != 'admin':
        print("Login as admin to use this feature")


    elif menu == 'a':
        pass
        '''In this block:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        user_task = input("Enter the username of the person whom the task is assigned to: ")
        name_task = input("Enter the name of the task: ")
        description_task = input("Enter a description of the task: ")
        duedate_task = input("When is the task due? YYYY-MM-DD: ")
        # Returns the current local date
        today = date.today()
        with open('tasks.txt', 'a') as tasks:
          tasks.write(f"\n{user_task}, {name_task}, {description_task}, {duedate_task}, {today}, No,")
          print("Task added")

    elif menu == 'va':
        pass
        '''In this block:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        tasks = open("tasks.txt", "r")
        all_tasks = tasks.read() #stores the contents of the .txt file as a string
        all_tasks = all_tasks.replace("\n", "")
        all_tasks = all_tasks.split(",") #converts to a list that can be iterated across
        print(all_tasks)
        tasks.close() 
        for i in range (0, len(all_tasks)-1, 6):
         print(f''' All tasks:
                    This task is assigned to {all_tasks[i]}
                    The task title is: {all_tasks[i+1]}
                    The task description is: {all_tasks[i+2]}
                    The date task was assigned is: {all_tasks[i+3]}
                    The task is due: {all_tasks[i+4]}
                    Is the task complete? {all_tasks[i+5]}
                    ''')

    elif menu == 'vm':
        pass
        '''In this block:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        tasks = open("tasks.txt", "r")
        all_tasks = tasks.read() #stores the contents of the .txt file as a string
        all_tasks = all_tasks.replace("\n", "")
        all_tasks = all_tasks.split(",") #converts str to a list that can be iterated across
        tasks.close() 
        for i in range (0, len(all_tasks)-1, 6):
            if all_tasks[i] == username_input: #added if loop to only display sub-set of all tasks
             print(f''' The following tasks are assigned to {username_input}:
                    
                    The task title is: {all_tasks[i+1]}
                    The task description is: {all_tasks[i+2]}
                    The date task was assigned is: {all_tasks[i+3]}
                    The task is due: {all_tasks[i+4]}
                    Is the task complete? {all_tasks[i+5]}
                    ''')
    
    elif menu == 's' and username_input == 'admin':
        pass
        ''' In this block:
         - Display total number of tasks
         - Display total number of users'''

        #print number of current tasks
        tasks = open("tasks.txt", "r")
        all_tasks = tasks.read() #stores the contents of the .txt file as a string
        all_tasks = all_tasks.replace("\n", "")
        all_tasks = all_tasks.split(",") #converts str to a list that can be iterated across
        tasks.close() 
        number_of_tasks = round((len(all_tasks))/6)
        print("Number of tasks = " + str(number_of_tasks))
        
        #print number of current users
        users_file = open("user.txt", "r")
        usernames = users_file.read() #stores the contents of the .txt file as a string
        users_file.close()
        usernames = usernames.replace(" ","")
        usernames = usernames.replace("\n","")
        users_split = usernames.split(",") #stores usernames in a list
        total_users = round((len(users_split) - 1)/2)
        print("Number of users = " + str(total_users))
    
    #if attempting to use the register feature not as admin, display appropriate message
    elif menu == 's' and username_input != 'admin':
        print("Login as admin to use this feature")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice. Please try again")