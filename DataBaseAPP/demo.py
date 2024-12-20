import psycopg2
import json

with open("config.json", "r") as file:
    config = json.load(file)

con = psycopg2.connect(**config)

cur = con.cursor()

cur.execute("create table students(student_id serial primary key , name text , address text , age int , number text);")
print("Student table created")
con.commit()
con.close()