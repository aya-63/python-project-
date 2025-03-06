from DatabaseConnection import*
from DatabaseValidator import *
from DatabaseManager import *
from MySQLAutomation import *
from QueryManager import *
from DataManager import *
from TableManager import *

def main():
    mysql_automation = MySQLAutomation()
    
    while True:
        print("\n1. Create Database")
        print("2. Create Table")
        print("3. Insert Data")
        print("4. Update Data")
        print("5. Delete Data")
        print("6. Select Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mysql_automation.create_database()
        elif choice == "2":
            mysql_automation.create_table()
        elif choice == "3":
            mysql_automation.insert_data()
        elif choice == "4":
            mysql_automation.update_data()
        elif choice == "5":
            mysql_automation.delete_data()
        elif choice == "6":
            mysql_automation.select_data()
        elif choice == "7":
            mysql_automation.close_connection()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()