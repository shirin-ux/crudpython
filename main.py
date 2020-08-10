from insert import *
from delete import *
from update import *
from select import *


def print_menu():
    print('1. Show customer')
    print('2. Add customer')
    print('3. Remove customer')
    print('4. Update customer')
    print('5. Quit')
    print('plase any key to show menu')
    print()


def insertcustomer():
    print("Add customer : ")
    customerfname = input("FirstName: ")
    customerlname = input("LirstName: ")
    melicode = input("Melicode : ")
    insert(customerfname, customerlname, melicode)


def updatecustomer():
    print("update customer: ")
    melicode = input("Melicode: ")
    customerfname = input("Pleace Enter new Name: ")
    update(customerfname, melicode)


def selectcustomer():
    print("customer is : ")
    selectCustom()


def deletecustomer():
    print("delete customer: ")
    melicode = input("Plase Enter Melicode : ")
    delete(melicode)



menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = input("Type in a Number (1-5): ")

    if menu_choice == "1":
        selectcustomer()

    elif menu_choice == "2":
        insertcustomer()

    elif menu_choice == "3":
        deletecustomer()

    elif menu_choice == "4":
        updatecustomer()

    elif menu_choice == "5":
        break

    else:
        print_menu()
