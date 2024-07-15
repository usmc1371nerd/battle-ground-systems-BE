import sqlite3

# First thing to do is establish a connection

connection = sqlite3.connect("gcs.db")

#Set communications with the database

cursor = connection.cursor()

"""
Things needed to do for the backend and databases.
Figure out what tables is needed and create a diagram
wire frame or anything allowing for organization. Some tables 
will need to be created that will allow for input from user such as
nineline and sitrep answers..??

Need think about future of app will this sustain small use? 
How will I deploy? Option is Python Anywhere..


"""

#Table SQL connection example
#cursor.excute("creatle table nineline ()")

#test data to check connections

"""
First you must excute the connection
Second create the table *note* (name column type, etc..)
Then we will need to execute many!
"""
#here we wil create a table
cursor.execute("create table test_data (numbers integer, text_1 text, text_2 text, text_3 text)")
#test data that will need to be inserted into db columns
test_data = [
    (1234, "Test data", "Test data", "Test data"),
    (1234, "Test data", "Test data", "Test data"),
    (1234, "Test data", "Test data", "Test data"),
]


#create a connection to add many columns to test
cursor.executemany("INSERT INTO test_data VALUES (?,?,?,?)", test_data)

# If you establish a connection you must close the connection
""" 
If you are not using something to view the test data example 
I'm using VS Code and extension for SQL lite you need to create 
print statement example: for row in cursor.execute(select * from 
test_data) print(row)

"""

connection.commit()
connection.close()

