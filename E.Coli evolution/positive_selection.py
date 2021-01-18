import sqlite3

con = sqlite3.Connection('e_coli.sqlite')
cur = con.cursor()

cur.execute('''
select * from (
    select population, feat_id, 
    sum(case when mutation_category == "snp_nonsynonymous" then 1 else 0 end) as NonSynonymous,
    sum(case when mutation_category == "snp_synonymous" then 1 else 0 end) as Synon,
    gene, desc
    from mutations left join ancestor on start<=start_position and end>=start_position
    where time == 50000 
    group by population, feat_id order by population, feat_id)
where NonSynonymous>=1 and Synon>=1 and NonSynonymous>Synon''')
# Finding genes with evidence of positive selection by checking the dS/dN ratio

all = cur.fetchall()
cnt = 0
print('Popuplation', 'FeatureID', 'NonSynonymousCount', 'SynonymousCount', 'Gene', 'Desc')
for a in all:
    p, f_id, n, s, g, d = a
    print(p, ";", f_id, ";", n, ";", s, ";", g, ";", d, ";", a[2]/a[3])

print(len(all))