#This is the code for the taskmanager.py programme for Capstone Project III/HyperionDev course
#It is effectively a task management system for a business where tasks are assigned to users in the database

#=====Import libraries===========

from datetime import date
from datetime import datetime
from collections import Counter
from pathlib import Path

#=====List of functions=============

def reg_user(new_user):
    '''When called, this function, only if logged in as admin:
            - Requests input of a new username
            - Requests input of a new password
            - Requests input of password confirmation.
            - Checks if the new password and confirmed password are the same.
            - If they are the same, adds them to the user.txt file,
            - Otherwise presents a relevant message.'''

    #read usernames and passwords from the user.txt file. Note that first line of user.txt must read "admin, adm1n, "
    users_file = open("user.txt", "r")
    usernames = users_file.read() #stores the contents of the .txt file as a string
    users_file.close()

    #format usernames and store in a list
    usernames = usernames.replace(" ","")
    usernames = usernames.replace("\n","")
    users_split = usernames.split(",")

    ##adapted logic from previous capstone task to work within this function##
    #checks that a user is not duplicated in the file
    if new_user in users_split:
            print("Username already in database")
    new_pwd = input("Enter a password: ")
    new_pwd_confirm = input("Please confirm the password: ")
    if new_pwd == new_pwd_confirm:
         with open('user.txt', 'a') as users:
          users.write(f"\n{new_user}, {new_pwd},")
          print("User added")
    else:
            print("Please try again")


def add_task(user_task, name_task, description_task, duedate_task):
    '''This function:
            - Prompts a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then gets the current date.
            - Adds the data to the file task.txt and
            - Includes 'No' to indicate that the task is not complete.'''

    today = date.today()
    with open('tasks.txt', 'a') as tasks:
     tasks.write(f"{user_task}, {name_task}, {description_task}, {today}, {duedate_task}, No,\n")
     print("Task added")
    
def view_all():
    '''This function:
            - Reads a line from the file tasks.txt.
            - Splits that line where there is comma and space.
            - Then prints the results in an easy-to-read format
            - Reads the file using a for loop.'''
    tasks = open("tasks.txt", "r")
    all_tasks = tasks.read() #stores the contents of the .txt file as a string
    all_tasks = all_tasks.replace("\n", "")
    all_tasks = all_tasks.split(",") #converts to a list that can be iterated across
    tasks.close() 

    print("All tasks:")
    for i in range (0, len(all_tasks)-1, 6):
         print(f'''
                    The below task is assigned to {all_tasks[i].strip()}
                    The task title is: {all_tasks[i+1].strip()}
                    The task description is: {all_tasks[i+2].strip()}
                    The task was assigned on: {all_tasks[i+3].strip()}
                    The task is due: {all_tasks[i+4].strip()}
                    Is the task complete? {all_tasks[i+5].strip()}

                    ''')
        
def view_mine(username_input):
    '''This function:
            - Reads a line from the file
            - Splits the line where there is comma and space.
            - Checks if the username of the person logged in is the same as the username that was
            read from the file [and assigned to a task].
            - If they are the same the task is printed in an easy-to-read format 
            - Then allow an option to edit the username or the due date of the task if task has not been completed already'''

    tasks = open("tasks.txt", "r")
    all_tasks = tasks.read() #stores the contents of the .txt file as a string
    all_tasks = all_tasks.replace("\n", "") 
    all_tasks = all_tasks.split(",") #converts str to a list that can be iterated across
    tasks.close() 

    print(f"The following tasks are assigned to {username_input}: ")
    n = 1 #task index
    for i in range (0, len(all_tasks)-1, 6):
        if all_tasks[i] == username_input: #added if loop to only display sub-set of all tasks
            print(f'''\nTask number {n}
                    The task title is: {all_tasks[i+1].strip()}
                    The task description is: {all_tasks[i+2].strip()}
                    The date task was assigned is: {all_tasks[i+3].strip()}
                    The task is due: {all_tasks[i+4].strip()}
                    Is the task complete? {all_tasks[i+5].strip()}

                    ''')
            n += 1 #update index

    #define a variable to hold the selected task
    option = input("If you would like to view a specific task enter the task number. If not enter -1: ")
    if (option == '-1') or (option.lower() == 'no'):
        print('''
        Returning to main menu...
        
        ''') #returns to main menu
    
    else:
                option = int(option)
                #print(all_tasks)
                print(f''' You have selected task number {option}:
                           
                           The task title is: {all_tasks[(option-1)*6].strip()}
                           The task description is: {all_tasks[(option-1)*6 + 1].strip()}
                           The date task was assigned is: {all_tasks[(option-1)*6+2].strip()}
                           The task is due: {all_tasks[(option-1)*6+3].strip()}
                           Is the task complete? {all_tasks[(option-1)*6+4].strip()}
                           
                           ''')

                complete = input("Would you like to mark the task as complete? Enter 'Yes' or 'No': ")
                if complete == 'Yes':

                    #needs code to open tasks.txt, read the relevant task, edit all_tasks[option+4] to be "Yes" and close file
                    #retrieve the contents of the file as before
                    tasks = open("tasks.txt", "r") 
                    all_tasks = tasks.read() #stores the contents of the .txt file as a string
                    print(all_tasks)
                    all_tasks = all_tasks.replace("\n", "")
                    all_tasks = all_tasks.split(",") #converts to a list that can be iterated across
                    tasks.close() 
                    print(all_tasks)

                    #update value in the list for the selected task
                    all_tasks[option+4] = 'Yes' 
                    print(all_tasks)

                    #write the updated list to the tasks.txt file
                    with open('tasks.txt', 'w') as tasks:
                        print(len(all_tasks))
                        tasks.write(f"") # remove previous contents of file [NB: There must be a better way to do it than deleting the contents each time!]
                        for i in range(0,len(all_tasks)-1,6):
                         tasks.write(f"{str(all_tasks[i])}, {str(all_tasks[i+1]).strip()}, {str(all_tasks[i+2]).strip()}, {str(all_tasks[i+3]).strip()}, {str(all_tasks[i+4]).strip()}, {str(all_tasks[i+5])},\n")
                         #Note that tasks file is ordered by 'username','task title', 'description', 'assigned date', 'due date', 'status')
                    print('''
                             Task list updated

                             ''')


                else:
                    option2 = input("Would you like to edit the task? Enter 'Yes' or 'No': ")
                    option2 = option2.lower()
                    tasks = open("tasks.txt", "r") #read file
                    all_tasks = tasks.read() #stores the contents of the .txt file as a string
                    all_tasks = all_tasks.replace("\n", "")
                    all_tasks = all_tasks.split(",") #converts to a list that can be iterated across
                    #print(all_tasks) #checkpoint
                    #print(all_tasks[option + 4].lstrip())
                    
                    #checks if task is complete i.e. does all_tasks[option + 4] == 'Yes', if 'No':
                    if (option2 == 'yes') and (all_tasks[option + 4].lstrip() == 'Yes'):
                        print("Sorry. Task is already complete and cannot be edited.")
                        exit()

                    elif (option2 == 'yes') and (all_tasks[option + 4].lstrip() == 'No'):
                        #offer to change the username assigned to the task
                        user_change = input("Would you like to change the user assigned to the task? Type 'Yes' or 'No': ")
                        user_change = user_change.lower()
                        if user_change == 'yes':
                            print("\n[X]This function will soon be available!\n")
                        else:
                        #insert call to function to change username
                        #offer to change the due date
                         date_change = input("Would you like to change the user assigned to the task? Type 'Yes' or 'No': ")
                         date_change = date_change.lower()
                         if date_change == 'yes':
                            print("\n[X]This function will soon be available!\n")
                         else:
                            print("Returning to main menu")
                        #insert call to function to change due date

                    else:
                        print('''
                        Returning to main menu...
                        ''')

def generate_report_task():
    '''This function will generate two text files task_overview.txt and user_overview.txt
    
    task_overview.txt will contain
    - the total number of tasks generated and tracked by task_manager.py
    - the total number of completed tasks
    - the total number of uncompleted tasks
    - the total number of overdue tasks i.e. uncompleted and past the due date
    - the percentage of incomplete tasks
    - the percentage of overdue tasks'''

#Open tasks.txt and extract the information needed
    tasks = open("tasks.txt", "r")
    all_tasks = tasks.read() #stores the contents of the .txt file as a string
    tasks.close()
    all_tasks = all_tasks.replace("\n", "")
    all_tasks = all_tasks.split(",") #converts str to a list that can be iterated across
    number_of_tasks = round((len(all_tasks))/6)
#print(f"Total number of tasks = {number_of_tasks}") #checkpoint

#Check how many tasks are completed
    completed_tasks = 0
    for i in range (5, len(all_tasks), 6):
     if all_tasks[i].lstrip() == "Yes":
        completed_tasks +=1
#print(f"Number of completed tasks = {completed_tasks}") #checkpoint

#Check how many tasks are incomplete and then incomplete and overdue
    incomplete_tasks = 0
    overdue_tasks = 0
    today = date.today()
    for i in range(5, len(all_tasks), 6):
     if all_tasks[i].lstrip() == "No":
        incomplete_tasks += 1
    for i in range(4, len(all_tasks), 6):
     if datetime.strptime(all_tasks[i].lstrip(), '%d %b %Y') > datetime.today():
        overdue_tasks += 1
    total_overdue_tasks = overdue_tasks - completed_tasks
    percentage_incomplete = ((incomplete_tasks) / (number_of_tasks))*100
    percentage_overdue = ((total_overdue_tasks) / (number_of_tasks))*100
    tasks.close() 

#===== Create a new file and write the results of this section to the file ======
    f = open("task_overview.txt", "w")
    f.write(f''' 

----Task Report----

Total number of tasks = {int(number_of_tasks)}
Number of completed tasks = {int(completed_tasks)}
Number of incomplete tasks = {int(incomplete_tasks)}
Number of incomplete and overdue tasks = {int(total_overdue_tasks)}
Percentage incomplete tasks = {int(percentage_incomplete)}%
Percentage overdue tasks = {int(percentage_overdue)}%

''')
    f.close()


def generate_report_user():
    '''This function will generate a file 'user_overview.txt' -

    user_overview.txt will contain
    - total number of users
    - total number of tasks
    for each user:
    - the number of tasks assigned to that user
    - the percentage of the total number of tasks that have been assigned to that user
    - [X] the percentage of tasks assigned to that user that have been completed
    - [X] the percentage of tasks assigned to that user yet to be completed
    - [X] the percentage of tasks assigned to that user that have not been completed and are overdue'''
    #Find total number of users by reading user.txt
    users_file = open("user.txt", "r")
    usernames = users_file.read() #stores the contents of the .txt file as a string
    users_file.close()
    
    #Format usernames and store in a list
    usernames = usernames.replace(" ","")
    usernames = usernames.replace("\n","")
    users_split = usernames.split(",")
    users_split.pop()
    #calculate total number of users from elements in the list
    total_number_of_users = len(users_split[::2])

    #Create a list to store user details in
    user_lst = []
    with open('user.txt', 'r+') as user_file:
     for line in user_file:
      users = line.split(", ")[0::]
      user_lst.append(users)

    #Open tasks.txt and extract total number of tasks
    tasks = open("tasks.txt", "r")
    all_tasks = tasks.read() #stores the contents of the .txt file as a string
    tasks.close()
    all_tasks = all_tasks.replace("\n", "")
    all_tasks = all_tasks.split(",") #converts str to a list that can be iterated 
    #calculate the total number of tasks
    total_number_of_tasks = round(len(all_tasks)/6)

    #Create a list to store task details in
    task_lst = []
    with open('tasks.txt', 'r+') as task_file:
     for line in task_file:
      tasks = line.split(", ")[0::]
      task_lst.append(tasks)


#===== Create new file and write the results of each section to the file ======
    f = open("user_overview.txt", "w") 
    f.write(f''' 

----User Report----

Total number of users = {int(total_number_of_users)}
Total number of tasks = {int(total_number_of_tasks)}

''')
    f.close()


    #This section of code iterates through the users and then iterates through the tasks
    for u in range(0, len(user_lst)):
     # declare and initialise values to calculate for each user
     total_user_tasks = 0
     # add the rest of the values
     for t in range(0, len(task_lst)):
     # check if user is in user_lst and in task_lst
      if user_lst[u][0] == task_lst[t][0]:
     # if so, then the total_user_tasks for each user increments
       total_user_tasks += 1
    #Now extend the logic above to display % of tasks assigned to each user that have been completed
    #and the % of tasks that still need to be completed
    #and the % of tasks that have not been completed and are overdue
     total_complete_tasks = 0
     for t in range(0, len(task_lst)):
      if task_lst[t][5] == "Yes":
        total_complete_tasks += 1
     total_overdue_tasks = 0
     for t in range(0, len(task_lst)):
        if (datetime.strptime(task_lst[t][4].lstrip(), '%d %b %Y') > datetime.today()) and (task_lst[t][5] == "No"):
            total_overdue_tasks += 1
     # add the rest of the logic for incomplete and overdue tasks for each user
     # write the calculated tasks for each user to the user overview text file
     # as the write statement is inside the outer for loop, it will write the total
     # number of tasks assigned to each user.
     with open('user_overview.txt', 'a') as user_overview:
      user_overview.write(f"Total number of tasks assigned to {user_lst[u][0]}: {total_user_tasks}\n")
      if total_user_tasks > 0:
       percentage_all_tasks = round(100*(total_user_tasks/total_number_of_tasks))
      else:
        percentage_all_tasks = 0
      user_overview.write(f"Percentage of all tasks assigned to {user_lst[u][0]}: {round(percentage_all_tasks)}%\n")
      if total_user_tasks > 0:
        percentage_completed_tasks = round(100*(total_complete_tasks/total_user_tasks))
      else:
        percentage_completed_tasks = 0
      user_overview.write(f"Percentage of completed tasks assigned to {user_lst[u][0]}: {round(percentage_completed_tasks)}%\n")
      if total_user_tasks > 0:
       total_incomplete_tasks_percent = 100*((total_user_tasks - total_complete_tasks)/(total_user_tasks))
      else:
        total_incomplete_tasks_percent = 0
      user_overview.write(f"Percentage of incomplete tasks assigned to {user_lst[u][0]}: {round(total_incomplete_tasks_percent)}%\n")
      user_overview.write(f"Number of incomplete and overdue tasks assigned to {user_lst[u][0]}: {total_overdue_tasks}\n")
      user_overview.write(f"\n")


def display_statistics():
    'This function simply prints to the terminal the contents of the two files generated by the two generate_report___() functions'
    with open('task_overview.txt', 'r') as task_overview:
        print(task_overview.read())
    with open('user_overview.txt', 'r') as user_overview:
        print(user_overview.read())

#====Login Section====

'''This section of code allows a user to login.
    - This code reads usernames and password from the user.txt file
    - A list or dictionary could be used to store a list of usernames and passwords from the file.
    - A while loop is used to validate username and password.
'''
#Read usernames and passwords from the user.txt file. On first use of programme user.txt must read "admin, adm1n, "
users_file = open("user.txt", "r")
usernames = users_file.read() #stores the contents of the .txt file as a string
users_file.close()

#format usernames and store in a list
usernames = usernames.replace(" ","")
usernames = usernames.replace("\n","")
users_split = usernames.split(",")
users_split.pop()
print(f"Current username and password list: {users_split}")

#Ask user for their username store in variable
username_input = input("Please enter your username: ")
#check if username is in database and allow login if it matches the password
while username_input not in users_split:
    print("User not found")
    username_input = input("Please enter your username: ")

while username_input in users_split:
 password_input = input("Please enter your password: ")
 if password_input == users_split[users_split.index(username_input) + 1]:
  print(f'''

  Login successful. Welcome {username_input.title()}!
  ''')
  break
 else:
  print("Username or password are incorrect. Try again")
  username_input = input("Please enter your username: ")


while True:
    #present the menu to the user and convert the user input to lower case
    menu = input('''\nSelect one of the following options below to continue:

r - Register a user (admin only)
a - Add a task
va - View all tasks
vm - View my task
s - View stats (admin only)
gr - Generate reports
ds - Display statistics
e - Exit

: ''').lower()

    if menu == 'r' and username_input == 'admin':
        pass
        new_user = input("Enter a new username: ")
        #call function reg_user()
        reg_user(new_user)

    #if user attempting to use the register feature not logged in as admin, displays appropriate message
    elif menu == 'r' and username_input != 'admin':
        print("Login as admin to use this feature")
        #returns to main menu

    elif menu == 'a':
        pass
        user_task = input("Enter the username of the person whom the task is assigned to: ")
        name_task = input("Enter the name of the task: ")
        description_task = input("Enter a description of the task: ")
        duedate_task = input("When is the task due? dd Month [as 3 letters] YYYY e.g. 27 Mar 1999: ")
        #call function add_task()
        add_task(user_task, name_task, description_task, duedate_task)
        #returns to main menu

    elif menu == 'va':
        pass
        #call function view_all()
        view_all()
        #returns to main menu

    elif menu == 'vm':
        pass
    #call function view_mine()
        view_mine(username_input)
    #returns to main menu

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
        #print(all_tasks) #checkpoint
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
    
    #if user is attempting to use the register feature not as admin, code displays appropriate message
    elif menu == 's' and username_input != 'admin':
        print("Login as admin to use this feature")

    elif menu == 'gr':
        pass
        generate_report_task()
        generate_report_user()
        print("\nReports generated\n\nReturning to main menu...\n")
    
    elif menu == 'ds':
        pass
        path = Path('user_overview.txt')
        if path.is_file():
            path = Path('task_overview.txt')
            if path.is_file():
                display_statistics()
            else:
                print(f"Please first use the generate reports function")
        else:
            print(f"Please first use the generate reports function")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("An error has occurred. Please try again")