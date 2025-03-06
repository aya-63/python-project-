import mysql.connector
from DatabaseValidator import*
class TableManager:
    """Class for table management operations"""
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.validator = DatabaseValidator()
    
    def create_table(self):
        """Create a new table in the database"""
        db_name = input("Enter the database name: ")
        self.db_connection.cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in self.db_connection.cursor.fetchall()]

        if db_name not in databases:
            print("Database does not exist.")
            return

        self.db_connection.set_database(db_name)
        table_name = input("Enter the table name: ")
        columns = []
        while True:
            col_name = input("Enter column name (or type 'done' to finish): ")
            if col_name.lower() == 'done':
                break

            # Provide examples of valid data types
            print("Examples of valid data types: INT, VARCHAR(255), TEXT, DATE, FLOAT, etc.")
            col_type = input(f"Enter data type for column '{col_name}': ")

            # Validate the data type
            if not self.validator.validate_data_type_input(col_type):
                print(f"Invalid data type: {col_type}. Please enter a valid MySQL data type.")
                continue

            columns.append(f"{col_name} {col_type}")

        if not columns:
            print("No columns added. Table creation aborted.")
            return

        columns_query = ", ".join(columns)
        query = f"CREATE TABLE {table_name} ({columns_query})"
        try:
            self.db_connection.cursor.execute(query)
            print(f"Table '{table_name}' created successfully in database '{db_name}'.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def delete_table(self, db_name, table_name):
        """Delete a table from the database"""
        self.db_connection.set_database(db_name)
        self.db_connection.cursor.execute(f"DROP TABLE {table_name}")
        print(f"Table '{table_name}' deleted successfully.")
    
    def delete_column(self, db_name, table_name, column_name):
        """Delete a column from a table"""
        self.db_connection.set_database(db_name)
        self.db_connection.cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
        print(f"Column '{column_name}' deleted from table '{table_name}'.")