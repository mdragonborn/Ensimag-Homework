import csv
import sqlite3

con = sqlite3.Connection('e_coli.sqlite')
cur = con.cursor()
# cur.execute('CREATE TABLE "ancestor" ("start" int, "end" int, "strand" int, "feat_id" varchar(12), "gene" varchar(10), "desc" varchar(128))')
# cur.execute('CREATE TABLE "mutations" ("population" varchar(4), "time" int, "type" varchar(3), "start_position" int, "end_position" int, "mutation" varchar(20), "mutation_category" varchar(32))')

f_m = open('mutations_descendants.csv')
csv_reader_m = csv.reader(f_m, delimiter=',')
cur.executemany('INSERT INTO mutations VALUES (?, ?, ?, ?, ?, ?, ?)', csv_reader_m)

f_a = open('ancestor.csv')
csv_reader_a = csv.reader(f_a, delimiter=',')
cur.executemany('INSERT INTO ancestor VALUES (?, ?, ?, ?, ?, ?)', csv_reader_a)

cur.close()
con.commit()
con.close()
f_m.close()
f_a.close()
