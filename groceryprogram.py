f = open('grocerylist.txt','r+') #open document in read/write mode
groceries = []
for line in f: #import grocery items to groceries list
        if line == "\n": #skip blank lines
                pass
        elif '\x00' in line: #if way is found to prevent in first place, update this
                pass
        else:
                if "\n" in line: #remove newline character from grocery items
                        groceries.append(str(line.replace("\n", "")))
                else:
                        groceries.append(str(line))
                        
                        ###
def add_again():
        ask = str.lower(input("Add another item?\n"))
        if ask == "yes" or ask == 'y':
                add_to_list()
        else:
                dowhat()
def remove_again():
        ask = str.lower(input("Remove another item?\n"))
        if ask == "yes" or ask == 'y':
                remove()
        else:
                dowhat()
def add_to_list():
        itemget = str.lower(input("Name an item to add to the list.\n"))
        groceries.append(itemget)
        print("Groceries are now as follows:")
        print(groceries)
        f = open('grocerylist.txt', 'w')
        f.truncate(0)
        for item in groceries:
                        f.write(item + '\n')
        f.close()
        add_again()
def remove():
        print(groceries)
        removal = str.lower(input("Which item would you like to remove?\n"))
        try:
                groceries.remove(removal)
                f = open('grocerylist.txt', 'w')
                f.truncate(0)
                for item in groceries:
                        f.write(item + '\n')
                print("Groceries are now as follows:")
                print(groceries)
                f.close()
                remove_again()
        except:
                print("Could not find item.")
                remove_again()

                ###
        
def dowhat(): #main function
        todo = str.lower(input("View list, remove item, or add item? Input 'view','remove', 'add,' or 'exit.'\n"))
        if todo == 'view' or  todo == 'v':
                print(groceries)
                dowhat()
        elif todo == 'add' or todo == 'a':
                add_to_list()
        elif todo == 'remove' or todo == 'r':
                remove()
        elif todo == 'exit' or todo == 'e':
                pass
        else:
                print('huh?')
                dowhat()
dowhat()
f.close()
