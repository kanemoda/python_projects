import json

def load(file_path, new_table_name, new_attributes):
    """
    Adds a new table and its attributes to the lookup JSON file.

    Parameters:
        file_path (str): Path to the lookup JSON file.
        new_table_name (str): The name of the new table to add.
        new_attributes (list): List of attributes for the new table.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the JSON structure is not as expected.
    """
    try:
        # Load existing JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Ensure the existing data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("Expected the JSON structure to be a dictionary.")

        # Add the new table to the dictionary
        if new_table_name in data:
            print(f"Table '{new_table_name}' already exists in the lookup file.")
        else:
            data[new_table_name] = new_attributes
            print(f"Added table '{new_table_name}' with attributes: {new_attributes}")

        # Write updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: File {file_path} contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
