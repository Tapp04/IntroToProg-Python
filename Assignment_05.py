# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Tram Pham, 2/16/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = []
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strFile = "ToDoList.txt"

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "r")
for row in objFile:
  lstRow = row.split(",")
  dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
  lstTable.append(dicRow)
objFile.close()
print(lstTable)

print("Your current data is: ")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Task"], dicRow["Priority"], sep=", " )


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input("What task would you like to add? "))
        strPriority = str(input("What is the priority of the task? "))
        dicRow = {"Task":strTask, "Priority":strPriority}
        lstTable.append(dicRow)


    # Step 5 - Remove a new item from the list/Table
    elif (strChoice == '3'):
        strDelete = input("Which Task would you like to delete? ")
        BInItemRemoved = False
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(strDelete == str(list(dict(lstTable[intRowNumber]).values())[0])):
                del lstTable[intRowNumber]
                bInItemRemoved = True

            intRowNumber +=1


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):

        objFile = open(strFile, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + '\n')

        objFile.close()

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        break