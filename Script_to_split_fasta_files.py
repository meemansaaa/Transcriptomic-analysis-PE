#Script to split .pep files into multiple smaller files
#pip install biopython (if not already installed)

from Bio import SeqIO
import os

#if you want to explicitly define variables
#input_file = "cdhit_out_95.pep"
#output_prefix = "split_output"

#to just check number of sequences before running + checking if the code runs
'''
records = list(SeqIO.parse(input_file, "fasta"))
total_records = len(records)
print(f"Total sequences found: {total_records}")

'''
#main function
def split_fasta(input_file, output_prefix, sequences_per_file=7000):

    """
    Splits a FASTA file into multiple smaller files.
    
    Arguments:
    - input_file: Path to the input .pep (FASTA) file.
    - output_prefix: Prefix for the output files.
    - sequences_per_file: Number of sequences per output file.
    """

    if not os.path.exists(input_file):  #checking if input file exists
        print(f"File {input_file} does not exist.")
        return

    records = list(SeqIO.parse(input_file, "fasta")) #checking the number of sequences before running
    total_records = len(records)
    print(f"Total sequences found: {total_records}")


    for i in range(0, total_records, sequences_per_file):   #splitting function
        batch = records[i:i+sequences_per_file]
        batch_number = (i // sequences_per_file) + 1
        output_file = f"{output_prefix}_part{batch_number}.pep"
        SeqIO.write(batch, output_file, "fasta")
        print(f"Written {len(batch)} sequences to {output_file}")


# Example usage:
split_fasta("cdhit_out_95.pep", "split_output", sequences_per_file=7000)

