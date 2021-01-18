import sqlite3

con = sqlite3.Connection('e_coli.sqlite')
cur = con.cursor()


cur.execute('''select *, min(time) from mutations 
inner join (select start_position, end_position from mutations where population=="Pop1" and time=30000) as p1
inner join (select start_position, end_position from mutations where population=="Pop8" and time=10000) as p8
where 
(mutations.start_position >= p1.start_position-10 and mutations.start_position <= p1.end_position+10 )
and (mutations.start_position >= p8.start_position-10 and mutations.start_position <= p8.end_position+10)
group by population,type,mutations.start_position,mutation_category
''')

all = cur.fetchall()
print("Mutations that are 20BP around the start positions of mutations in Pop1 time=30000 and Pop8 time=10000")
for a in all:
    print(a)

cur.execute('''select *, min(time) from mutations 
inner join (select start_position, end_position from mutations where population=="Pop1" and time=30000) as p1
inner join (select start_position, end_position from mutations where population=="Pop8" and time=10000) as p8
where 
(mutations.start_position = p1.start_position and mutations.start_position = p1.end_position )
and (mutations.start_position = p8.start_position and mutations.end_position = p8.end_position)
group by population,type,mutations.start_position,mutation_category
''')

all = cur.fetchall()
print("\n\nSame mutations that appear in both Pop1 time=30000 and Pop8 time=10000")
for a in all:
    print(a)


cur.execute(''' select * from ancestor as a inner join
(select distinct(start_position) as pos from (
select *, min(time) from mutations 
inner join (select start_position, end_position from mutations where population=="Pop1" and time=30000) as p1
inner join (select start_position, end_position from mutations where population=="Pop8" and time=10000) as p8
where 
(mutations.start_position >= p1.start_position-10 and mutations.start_position <= p1.end_position+10 )
and (mutations.start_position >= p8.start_position-10 and mutations.start_position <= p8.end_position+10)
group by population,type,mutations.start_position,mutation_category)) as c
where a.start <= c.pos and a.end>= c.pos
''')

all = cur.fetchall()
print("\n\nGenes containing found mutations")
for a in all:
    print(a)

