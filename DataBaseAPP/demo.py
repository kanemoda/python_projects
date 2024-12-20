import psycopg2
import json

def createTable(filename , tableName , ):
    with open(filename , "r") as file:
        config = json.load(file)
    con = psycopg2.connect(**config)
    cur = con.cursor()
    cur.execute("""create table students (
                student_id serial primary key ,
                 name text ,
                 address text ,
                 age int ,
                 number text);""")
    print("Student table created")
    con.commit()
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
    
    

insertData("config.json" , "students" , ["testNam1" , "testAddress1" , 999 , "12345678"])


    







