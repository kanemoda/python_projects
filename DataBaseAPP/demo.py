import psycopg2
import json


#Not safe for SQl Injections
def createTable(filename , tableName , attributes ,pk=None ):

    """
    Creates a table in the PostgreSQL database with the given attributes.

    Parameters:
        config_file (str): Path to the JSON file containing database configuration.
        table_name (str): Name of the table to create.
        attributes (list): List of attribute definitions (e.g., ["name TEXT", "age INT"]).
        pk (str, optional): Primary key definition (e.g., "id SERIAL PRIMARY KEY").
    
    Raises:
        ValueError: If the attributes list is empty.
        psycopg2.DatabaseError: If there's an error executing the query.
    """
    if not attributes:
        raise ValueError("Attributes list cannot be empty.")
    
    attribute_str = ", ".join(attributes)

    if pk:
        query = f"CREATE TABLE {tableName} ({pk}, {attribute_str});"
    else:
        query = f"CREATE TABLE {tableName} ({attribute_str});"


    #Load database config
    try:
        with open(filename , "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{filename}' not found.")
    
    #Execute query
    try:
        con = psycopg2.connect(**config)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
    except psycopg2.DatabaseError as e:
        print(f"Error creating table '{tableName}': {e}")
        raise
    finally:
        if con:
            con.close()


def insertData(filename , tableName ,values):
    #Load database config
    with open(filename , "r") as file:
        config = json.load(file)

    #Load lookup table
    with open("lookup.json", "r") as lookup_file:
        lookup_table = json.load(lookup_file)

    if (tableName not in lookup_table):
        raise ValueError(f"Table {tableName} not found in lookup table")
    
    
    attributes = lookup_table[tableName]
    attributes_str = ", ".join(attributes)
    placeHolders = ", ".join(["%s"] * len(values))

    query = f"INSERT INTO {tableName} ({attributes_str}) VALUES ({placeHolders})"

    try:
        con = psycopg2.connect(**config)
        cur = con.cursor()
        cur.execute(query,values)
        print("New Tupple Inserted at student table")
        con.commit()
    
    except psycopg2.DatabaseError as e:
        print(f"Error: {e}")
   
    finally:
        if con:
            con.close()
    
    

insertData("config.json" , "Test" , )


    







