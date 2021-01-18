import Bio.SeqIO
import pickle
import matplotlib.pyplot as plt
import sys

# Input: 2 positional arguments
# 1. file name (path to .fna file with the reads) 
# 2. k (for which to count kmer occurences)
# Output: file with a dictionary where keys are kmers and values occurrence counts, serialized with the pickle library. 


# If True, program will print additional info
print_dbg = False

# Counts occurrences of each k-mer, maps distinct k-mers to reads they appear in
def count_kmers(reads, k):
    kmer_to_read_map = {}
    kmers = dict()
    f=True
    for j, read in enumerate(reads):
        read_str = str(read.seq)

        for start in range(len(read_str) - k):
            window = read_str[start : start + k]
            kmers[window] = kmers.get(window, 0) + 1

        if j%100000 == 0:
            print(j/20000,'%')

    print('Done counting')
    return kmers

# Creates a list of all reads that don't contain kmers with occurence count under
# the given threshold
def _filter_reads(reads, kmers, k, threshold):
    clean_reads = []
    for j, read in enumerate(reads):
        read_str = str(read.seq)
        error_found = False
        for start in range(len(read_str) - k):
            window = read_str[start : start + k]
            if kmers[window] < threshold:
                error_found = True
                break
        if not error_found:
            clean_reads.append(read)
    return clean_reads

# Creates a set of all reads that have k-mers, plots all occurrences
def plot_distribution(kmer_counts):
    distribution = dict()
    suma = 0
    for key in kmer_counts:
        suma += kmer_counts[key]
        distribution[kmer_counts[key]] = distribution.get(kmer_counts[key], 0) + 1
    
    i = 0
    suma2 = 0
    while suma2 < suma*0.04:
        i+=1
        suma2+= distribution.get(i, 0)

    
    plt.bar(list(distribution.keys()), distribution.values(), 5, color='g')
    plt.xlim([0, 500])
    print('Close chart to continue.')
    plt.show()

    return i

# Count k-mers, find reads with single occurrence k-mers and plot. Dump results into pickle file.
def kmers_graph(kmer_counts, k=None):
    fp = plot_distribution(kmer_counts)

    if print_dbg and k is not None:
        with open(str(k)+'file.txt', 'w') as f:
            f.write(str(kmer_counts))

    return fp


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough arguments")
    input_file = sys.argv[1]
    k = int(sys.argv[2])

    reads = Bio.SeqIO.parse(input_file,"fasta")
    kmer_counts = count_kmers(reads, k)


    kmers_graph(kmer_counts, k)

    print("Writing kmer counts to "+ input_file.split('.')[-3] + "-all-" + str(k) + ".kmers")
    with open(input_file.split('.')[-3] + "-all-" + str(k) + ".kmers", 'wb') as handle:
        pickle.dump([kmer_counts], handle, protocol=pickle.HIGHEST_PROTOCOL)

    