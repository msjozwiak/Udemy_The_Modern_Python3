import sqlite3

conn = sqlite3.connect("my_users.db")
c = conn.cursor()

# c.execute("CREATE TABLE users (username TEXT, password TEXT);")
# people = [
#     ("Roald", "Amundsen"),
#     ("Rosa", "Parks"),
#     ("Henry", "Hudson"),
#     ("Neil", "Armstrong"),
#     ("Daniel", "Boone")]
#
# c.executemany("INSERT INTO users VALUES (?,?)", people)

u = input("please enter your username...")
p = input("please enter your password...")
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query, (u, p))

result = c.fetchone()
if result:
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()
