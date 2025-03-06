from DatabaseValidator import*
class DatabaseManager:
    """Class for database management operations"""
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.validator = DatabaseValidator()
    
    def create_database(self):
        """Create a new database"""
        db_name = input("Enter the name of the database: ")
        self.db_connection.cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in self.db_connection.cursor.fetchall()]

        if db_name in databases:
            print("Database already exists.")
        else:
            self.db_connection.cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully.")
    
    def delete_database(self, db_name):
        """Delete a database"""
        self.db_connection.cursor.execute(f"DROP DATABASE {db_name}")
        print(f"Database '{db_name}' deleted successfully.")
