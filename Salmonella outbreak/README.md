# Salmonella outbreak


Installing required libraries:

```
pip install -r requirements.txt
```

## Counting k-mers

To count the occurences of all k-mers `k=20` in a FASTA file, run:
``` 
count_kmers.py salmonella-enterica.reads.fna 20
```
Output: ```pickle``` serialized file with dictionary containing the counts of k-kmers. Displayed distribution chart.

## Removing errors

To remove kmers with sequencing errors from two files (both strains separately) with threshold of `t=10` occurrences, run:
```
filter_kmers.py salmonella-15.kmers salmonella-variant-15.kmers 10
```
Output: two files (eg. salmonella-15-10.kmers and salmonella-variant-15-10.kmers) with kmers with less than `t` occurrences. If no thershold is specified, the program will remove the botton 4% of k-mers.


## Finding SNP

To find k-mers that are potential parts of SNP sequences (unique to one kmers file), run:

```
find_snp.py salmonella-15-10.kmers salmonella-variant-15-10.kmers
```
Output: two files with unique kmers for each file (eg. salmonella-15-10-snp.kmers and salmonella-variant-15-10-snp.kmers)

## Getting reads that contain a sequence

To find all reads in a file containing a certain sequence:

```
find_reads.py salmonella-enterica-variant.read.fna AGCTTCTGGGCGAGGGGACGGGTTGTTAAAC
```

Output: file (salmonella-enterica-variant-subset.read.fna) with a subset of reads that contain the given sequence.