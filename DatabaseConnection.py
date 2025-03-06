import mysql.connector

class DatabaseConnection:
    """Class to handle database connection and cursor management"""
    def __init__(self, host="localhost", user="root", password="iti@1234"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()
    
    def close(self):
        """Close database connection and cursor"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
    def commit(self):
        """Commit transactions to the database"""
        self.connection.commit()
        
    def set_database(self, db_name):
        """Set the active database"""
        self.connection.database = db_name
