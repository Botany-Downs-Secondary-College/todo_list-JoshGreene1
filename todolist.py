import datetime

to_dolist = ["Launch the Cruise Missiles", "Launch Revolutions at the Coal Mines", "Feed the Cat"]

x = datetime.datetime.now()
y = 1
global hello

print("Hello")
name = input("Please enter your name: ")
print("Hello", name)


def add():
    print("Please type below task you would like to add to your list")
    add1 = input("Insert New Task: ")
    to_dolist.append(add1)
    print("Your list is now", to_dolist)
    print("Your most recent task was''", (to_dolist[-1]), "''and was added at", (x))


def view():
    print(to_dolist)


def exec():
    print("Would you like to add something your 'To Do list?' or would you like to view your to do list?")
    print("Add (Used to task to to the 'to do list') View (Used to view the 'to do list')")
    while y >= 1:
        option = input("Option Insert: ")
        if option == "Add":
            y + 1
            add()
        elif option == "View":
            y + 1
            view()
        else:
            print("Enter a Correct Response Please")


exec()
