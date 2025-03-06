import mysql.connector
class QueryManager:
    """Class for data query operations"""
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def select_data(self):
        """Select and display data from a table"""
        db_name = input("Enter the database name: ")
        self.db_connection.set_database(db_name)
        table_name = input("Enter the table name: ")

        # Fetch all column names from the table
        self.db_connection.cursor.execute(f"DESCRIBE {table_name}")
        columns = [col[0] for col in self.db_connection.cursor.fetchall()]

        if not columns:
            print("No columns found in the table.")
            return

        # Ask the user what they want to do
        print("\nSelect Options:")
        print("1. Select all ")
        print("2. Select a specific column ")
        print("3. Select a specific row ")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Select all columns
            query = f"SELECT * FROM {table_name}"
        elif choice == "2":
            # Display all available columns
            print("Available columns in the table:")
            for i, col in enumerate(columns, 1):
                print(f"{i}. {col}")

            # Let the user choose columns
            selected_columns = input("Enter the numbers of the columns to select (comma-separated): ")
            try:
                selected_indices = [int(idx.strip()) for idx in selected_columns.split(",")]
                selected_columns = [columns[idx - 1] for idx in selected_indices if 1 <= idx <= len(columns)]
                if not selected_columns:
                    print("No valid columns selected. Aborting.")
                    return
                columns_query = ", ".join(selected_columns)
                query = f"SELECT {columns_query} FROM {table_name}"
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")
                return
        elif choice == "3":
            # Select a specific row based on a column value
            print("Available columns in the table:")
            for i, col in enumerate(columns, 1):
                print(f"{i}. {col}")

            # Let the user choose a column
            col_choice = input("Enter the number of the column to filter by: ")
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
            condition_value = input(f"Enter the value for {condition_column} to filter rows: ")

            # Construct the query
            query = f"SELECT * FROM {table_name} WHERE {condition_column} = '{condition_value}'"
        else:
            print("Invalid choice. Please try again.")
            return

        # Execute the query and display results
        try:
            self.db_connection.cursor.execute(query)
            results = self.db_connection.cursor.fetchall()
            if not results:
                print("No data found.")
            else:
                print("\nSelected Data:")
                for row in results:
                    print(row)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
