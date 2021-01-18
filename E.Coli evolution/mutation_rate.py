import sqlite3
from pandas import DataFrame
import numpy as np
con = sqlite3.Connection('e_coli.sqlite')
cur = con.cursor()

def prettyprint(cnts):
    print(DataFrame([[c for c in row.tolist()] for row in cnts]))

times = np.array([500, 1000, 1500, 2000, 5000, 10000, 15000, 20000, 30000, 40000, 50000])
counts = [times] # Print column headers

count = False # Choice: Caluclate synonymous SNP as 25% of all SNP mutations or count detected synonymous snp mutations
unique = False # Choice: Count all mutations that exist in the generation or just ones that didn't appear in previous generations

for pop in range(1,9):
    # Set of mutations that already appeared in this population
    existing_mutations = set()
    mutations = np.zeros((11))
    last_cnt = 0
    for i, time in enumerate(times):
        if count:
            # Get number of all SNPs and calculate synonymous as 25% of that number
            cur.execute('''select start_position, mutation, mutation_category from mutations
            where population=='Pop{}'
            and time=={} and mutation_category=="snp_synonymous"'''.format(pop, time))
        else:
            # Count detected synonymous snp mutations from the mutation file
            cur.execute('''select start_position, mutation, mutation_category from mutations
                where population=='Pop{}'
                and time=={} and type="SNP"'''.format(pop, time))

        new_mutations = cur.fetchall()
        if not unique:
            # Count all mutations in generation
            mutations[i] =  len(new_mutations)
        else:
            # Count only mutations that appear in this generation for the first time
            encoded_mutations = [str(a[0])+str(a[1]) for a in new_mutations]
            new_count = 0
            for encoding in encoded_mutations:
                if encoding not in existing_mutations:
                    existing_mutations.add(encoding)
                    new_count+=1
            mutations[i] = new_count

    counts.append(mutations)


prettyprint(counts)