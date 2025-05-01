#Script to split .pep files into multiple smaller files - limiting residues
#pip install biopython (if not already installed)

from Bio import SeqIO
import os

# defining input and output
input_file = "cdhit_out_95.pep"           # Your input .pep (FASTA) file
output_prefix = "my_out"          # The prefix for output files
max_residues_per_file = 99999       # Max residues per output file

def split_fasta_by_residues(input_file, output_prefix, max_residues=100000):
    """
    Splits a FASTA file into multiple smaller files such that
    total residues in each file <= max_residues.

    Args:
    - input_file: Path to the input .pep (FASTA) file.
    - output_prefix: Prefix for the output files.
    - max_residues: Maximum total residues per output file.
    """

    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return

    records = list(SeqIO.parse(input_file, "fasta"))
    total_sequences = len(records)
    print(f"Total sequences found: {total_sequences}")

    batch = []
    batch_residues = 0
    batch_number = 1

    for record in records:
        seq_length = len(record.seq)

        # If adding this sequence exceeds max residues, write current batch
        if batch_residues + seq_length > max_residues and batch:
            output_file = f"{output_prefix}_part{batch_number}.pep"
            SeqIO.write(batch, output_file, "fasta")
            print(f"Written {len(batch)} sequences ({batch_residues} residues) to {output_file}")
            batch_number += 1
            batch = []
            batch_residues = 0

        batch.append(record)
        batch_residues += seq_length

    # Write the last batch if it has any sequences
    if batch:
        output_file = f"{output_prefix}_part{batch_number}.pep"
        SeqIO.write(batch, output_file, "fasta")
        print(f"Written {len(batch)} sequences ({batch_residues} residues) to {output_file}")

# example run
split_fasta_by_residues(input_file, output_prefix, max_residues_per_file)
