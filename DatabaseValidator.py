class DatabaseValidator:
    """Class to validate database inputs and data types"""
    @staticmethod
    def validate_data_type_input(data_type):
        """
        Validate if the data type is a valid MySQL data type.
        This is a basic validation and can be expanded further.
        """
        valid_types = ["INT", "VARCHAR", "TEXT", "DATE", "FLOAT", "DOUBLE", "DECIMAL", "DATETIME", "TIMESTAMP"]
        return any(valid_type in data_type.upper() for valid_type in valid_types)
    
    @staticmethod
    def validate_data_type(value, data_type):
        """Validate if a value matches the expected data type"""
        if "int" in data_type.lower():
            return value.isdigit()
        elif "varchar" in data_type.lower() or "text" in data_type.lower():
            return True  # Strings are always valid
        elif "float" in data_type.lower() or "double" in data_type.lower():
            try:
                float(value)
                return True
            except ValueError:
                return False
        return True