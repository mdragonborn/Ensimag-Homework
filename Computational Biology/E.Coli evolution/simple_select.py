import sqlite3

con = sqlite3.Connection('e_coli.sqlite')
cur = con.cursor()

cur.execute('''select * from mutations where population=="Pop1" and time=30000''')

all = cur.fetchall()
cnt = 0
for a in all:
    print(a)
