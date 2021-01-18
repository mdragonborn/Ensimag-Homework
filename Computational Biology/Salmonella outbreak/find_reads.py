import Bio.SeqIO
import sys

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments")
    input_file = sys.argv[1]
    sequence = sys.argv[2]

    reads = Bio.SeqIO.parse(input_file,"fasta")

    print("Writing results to " + input_file.split('.')[-3] +'-subset.reads.fna')
    with open(input_file.split('.')[-3] +'-subset.reads.fna', 'w') as f:
        for j, read in enumerate(reads):
            read_str = str(read.seq)
            if read_str.find(sequence) >= 0:
                f.write('>'+str(j)+'\n'+read_str+'\n')