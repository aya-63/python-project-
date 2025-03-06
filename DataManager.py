from DatabaseValidator import*
class DataManager:
    """Class for data manipulation operations"""
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.validator = DatabaseValidator()
    
    def insert_data(self):
        """Insert data into a table"""
        db_name = input("Enter the database name: ")
        self.db_connection.set_database(db_name)
        table_name = input("Enter the table name: ")

        self.db_connection.cursor.execute(f"DESCRIBE {table_name}")
        schema = {col[0]: col[1] for col in self.db_connection.cursor.fetchall()}
        values = {}

        for col, data_type in schema.items():
            while True:
                value = input(f"Enter value for {col} ({data_type}): ")
                if self.validator.validate_data_type(value, data_type):
                    values[col] = value
                    break
                else:
                    print(f"Invalid data type for column {col}. Expected {data_type}.")

        columns = ", ".join(values.keys())
        val_placeholders = ", ".join([f"'{val}'" for val in values.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({val_placeholders})"
        self.db_connection.cursor.execute(query)
        self.db_connection.commit()
        print("Data inserted successfully.")
    
    def update_data(self):
        """Update data in a table"""
        db_name = input("Enter the database name: ")
        self.db_connection.set_database(db_name)
        table_name = input("Enter the table name: ")
        column_to_update = input("Enter the column to update: ")
        new_value = input("Enter the new value: ")
        condition_column = input("Enter the column for the condition: ")
        condition_value = input("Enter the value for the condition: ")

        query = f"UPDATE {table_name} SET {column_to_update} = '{new_value}' WHERE {condition_column} = '{condition_value}'"
        self.db_connection.cursor.execute(query)
        self.db_connection.commit()
        print("Data updated successfully.")
    
    def delete_entity(self, db_name, table_name):
        """Delete a row from a table"""
        self.db_connection.set_database(db_name)

        # Fetch all column names from the table
        self.db_connection.cursor.execute(f"DESCRIBE {table_name}")
        columns = [col[0] for col in self.db_connection.cursor.fetchall()]

        if not columns:
            print("No columns found in the table.")
            return

        # Display all column names to the user
        print("Available columns in the table:")
        for i, col in enumerate(columns, 1):
            print(f"{i}. {col}")

        # Let the user choose a column
        col_choice = input("Enter the number of the column to use for deletion: ")
        try:
            col_choice = int(col_choice)
            if 1 <= col_choice <= len(columns):
                condition_column = columns[col_choice - 1]
            else:
                print("Invalid choice. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # Let the user enter the value for the condition
        condition_value = input(f"Enter the value for {condition_column} to delete the row: ")

        # Execute the delete query
        query = f"DELETE FROM {table_name} WHERE {condition_column} = '{condition_value}'"
        self.db_connection.cursor.execute(query)
        self.db_connection.commit()
        print("Entity deleted successfully.")