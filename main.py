import sqlite3

connection = sqlite3.connect("itstep_DB.sl3")

cur = connection.cursor()

# cur.execute("CREATE TABLE first_table (name TEXT);")

# cur.execute("INSERT INTO first_table (name) VALUES('Test');")


cur.execute("SELECT rowid, name FROM first_table;")
res = cur.fetchall()

print(res)

for item in res:
    print("Row id:",item[0],"\tName:",item[1])

connection.commit()
connection.close()