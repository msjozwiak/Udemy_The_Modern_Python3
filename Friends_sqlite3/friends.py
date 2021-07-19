import sqlite3

conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
# VALUES ('Merriwether', 'Lewis', 7)'''

# BAD! DO NOT DO THIS!
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY!
# form_first = "Mary-Todd2"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)]

# for person in people:
# 	insert that one person

average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]
# print(average / len(people))

# Insert all at once
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# c.execute(query, data)
conn.commit()
conn.close()
