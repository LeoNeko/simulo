import sqlite3
in_file = "slovar.txt"
out_file = "slovar.txt"
data_file = []

conn = sqlite3.connect('base.db3')
c = conn.cursor()
number = 0
"""
with open(in_file, 'r') as read_file:
    for line in read_file:
        divided = line.split('–')
        print(divided[0])

        c.execute("INSERT INTO RU_BY VALUES (?,?,?)", (number,divided[0], divided[1]))
        #Сохраняем изменения
        conn.commit()

        number = number + 1
"""

c.execute("INSERT INTO RU_BY VALUES (?,?,?)")
#Сохраняем изменения
# conn.commit()

number = number + 1