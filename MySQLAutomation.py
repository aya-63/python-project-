from DatabaseManager import*
from DataManager import*
from TableManager import*
from QueryManager import*
from DatabaseConnection import*

class MySQLAutomation:
    """Main class that orchestrates database operations"""
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.db_manager = DatabaseManager(self.db_connection)
        self.table_manager = TableManager(self.db_connection)
        self.data_manager = DataManager(self.db_connection)
        self.query_manager = QueryManager(self.db_connection)
    
    def create_database(self):
        """Create a new database"""
        self.db_manager.create_database()
    
    def create_table(self):
        """Create a new table"""
        self.table_manager.create_table()
    
    def insert_data(self):
        """Insert data into a table"""
        self.data_manager.insert_data()
    
    def update_data(self):
        """Update data in a table"""
        self.data_manager.update_data()
    
    def delete_data(self):
        """Delete database objects or data"""
        print("\nDelete Options:")
        print("1. Delete a Database")
        print("2. Delete a Table")
        print("3. Delete a Column")
        print("4. Delete an Entity (Row)")
        choice = input("Enter your choice: ")

        if choice == "1":
            db_name = input("Enter the database name to delete: ")
            self.db_manager.delete_database(db_name)
        elif choice == "2":
            db_name = input("Enter the database name: ")
            table_name = input("Enter the table name to delete: ")
            self.table_manager.delete_table(db_name, table_name)
        elif choice == "3":
            db_name = input("Enter the database name: ")
            table_name = input("Enter the table name: ")
            column_name = input("Enter the column name to delete: ")
            self.table_manager.delete_column(db_name, table_name, column_name)
        elif choice == "4":
            db_name = input("Enter the database name: ")
            table_name = input("Enter the table name: ")
            self.data_manager.delete_entity(db_name, table_name)
        else:
            print("Invalid choice. Please try again.")
    
    def select_data(self):
        """Select and display data from a table"""
        self.query_manager.select_data()
    
    def close_connection(self):
        """Close the database connection"""
        self.db_connection.close()
