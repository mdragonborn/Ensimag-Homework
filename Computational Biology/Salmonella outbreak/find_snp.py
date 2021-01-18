import sys
import pickle

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough arguments")
    input_file_original = sys.argv[1]
    input_file_mutated = sys.argv[2]

    with open(input_file_original, 'rb') as f:
        pickled_data = pickle.load(f)
        kmer_counts_org = pickled_data[0]
    
    with open(input_file_mutated, 'rb') as f:
        pickled_data = pickle.load(f)
        kmer_counts_mut = pickled_data[0]

    snp_org = []
    for kmer in kmer_counts_org:
        if kmer not in kmer_counts_mut:
            snp_org.append((kmer, kmer_counts_org[kmer]))

    snp_mut = []
    for kmer in kmer_counts_mut:
        if kmer not in kmer_counts_org:
            snp_mut.append((kmer, kmer_counts_mut[kmer]))

    print("Writing results to " + input_file_original.split('.')[-2] +'-snp.txt and ' + input_file_mutated.split('.')[-2] +'-snp.txt')
    with open(input_file_original.split('.')[-2] +'-snp.txt', 'w') as f:
        for snp in snp_org:
            f.write(snp[0] + '      ' + str(snp[1]) + '\n')
    with open(input_file_mutated.split('.')[-2] +'-snp.txt', 'w') as f:
        for snp in snp_mut:
            f.write(snp[0] + '      ' + str(snp[1]) + '\n')
