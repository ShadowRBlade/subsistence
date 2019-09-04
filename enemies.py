'''
Enemy Engine
'''
import sqlite3

perkTitle = ['Strength    ', 'Perception  ', 'Endurance   ', 'Charisma    ', 'Intelligence', 'Agility     ', 'Luck        ']
perkCollection = []

conn = sqlite3.connect('test.db')
cursor = conn.execute("SELECT PERK, VALUE from PERKS")
for row in cursor:
    perkCollection.append(row[1])

print(perkCollection)