import sqlite3 

c = sqlite3.connect("database.db")
 
rows = c.execute("""SELECT username, password_hash FROM users ORDER BY username""").fetchall()

print(*rows, sep="\n")

c.close()