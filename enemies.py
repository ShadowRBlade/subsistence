'''
Enemy Engine
'''
import sqlite3
perkCollection = []
conn = sqlite3.connect('test.db')
cursor = conn.execute("SELECT PERK, VALUE from PERKS")
# retreive into array
for row in cursor:
    perkCollection.append(row[1])
print(perkCollection)