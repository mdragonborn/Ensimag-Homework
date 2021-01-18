import sqlite3

con = sqlite3.Connection('e_coli.sqlite')
cur = con.cursor()

# Here we are getting the counts for all mutations and ony AT->CG mutations to compare how many of the total mutations are the AT->CG ones

base_query_acgt = '''select population, count(*) from mutations 
where (population=="Pop1" or population=="Pop8") and time={} and (mutation="A->C" or mutation="T->G")
group by population order by population'''

base_query = '''select population, count(*) from mutations 
where (population=="Pop1" or population=="Pop8") and time={}
group by population order by population'''

times = [500, 1000, 1500, 2000, 5000, 10000, 15000, 20000, 30000, 40000, 50000]

mutation_cnt_acgt = [[],[]]
mutation_cnt = [[],[]]
for j, time in enumerate(times):
    cur.execute(base_query_acgt.format(time))
    count = cur.fetchall()
    print(time)
    for i, row in enumerate(count):
        if row[0] == "Pop1":
            mutation_cnt_acgt[0].append(row[1])
        else:
            mutation_cnt_acgt[1].append(row[1])
    for cnt in mutation_cnt_acgt:
        if len(cnt)<j+1:
            cnt.append(0)

    cur.execute(base_query.format(time))
    count = cur.fetchall()
    for i, row in enumerate(count):
        if row[0] == "Pop1":
            mutation_cnt[0].append(row[1])
        else:
            mutation_cnt[1].append(row[1])
    for cnt in mutation_cnt:
        if len(cnt)<j+1:
            cnt.append(0)


print("Pure mutations Pop1")
for a in mutation_cnt[0]:
    print(a)
print("Pure mutations Pop8")
for a in mutation_cnt[1]:
    print(a)

print("Filtered mutations Pop1")
for a in mutation_cnt_acgt[0]:
    print(a)
print("Filtered mutations Pop8")
for a in mutation_cnt_acgt[1]:
    print(a)