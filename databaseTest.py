import sqlite3
conn = sqlite3.connect("gameData.db") #Connect to the database. As none exists, one is auto-created.
c = conn.cursor() #Cursor object allows you to interact with the database.

c.execute("CREATE TABLE profiles (ProfileID, UserName, SongsPlayed, TimePlayed)") #SQL Statement to create table.
c.execute("INSERT INTO profiles VALUES (0, 'example', 0, 23354)") #Add example entry to test.
c.execute(
conn.commit()
conn.close()
