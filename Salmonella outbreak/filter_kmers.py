import pickle
import sys
from count_kmers import kmers_graph

def filter_kmers(kmer_counts, threshold):
    clean_kmers = dict()
    for kmer in kmer_counts:
        if kmer_counts[kmer] >= threshold:
            clean_kmers[kmer] = kmer_counts[kmer]
    return clean_kmers


if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments")
    input_files = [sys.argv[1], sys.argv[2]]

    for input_file in input_files:
        with open(input_file, 'rb') as f:
            pickled_data = pickle.load(f)
            kmer_counts = pickled_data[0]
        
        if len(sys.argv) == 3:
            first_percentile = kmers_graph(kmer_counts)
            threshold = first_percentile
        else:
            threshold = int(sys.argv[3])

        clean_kmers = filter_kmers(kmer_counts, threshold)
            
        print('Creating chart of k-mers from clean data')
        # kmer_counts_clean = count_kmers(reads, k)
        with open(input_file.split('.')[-2] + '-' + str(threshold) + ".kmers", 'wb') as handle:
            pickle.dump([clean_kmers], handle, protocol=pickle.HIGHEST_PROTOCOL)
        kmers_graph(clean_kmers)

