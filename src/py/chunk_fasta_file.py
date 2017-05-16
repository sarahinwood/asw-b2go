#!/usr/bin/env python3

from Bio import SeqIO
import os

# IO
output_dir = 'output/fasta_chunks'
trinity_fasta = 'data/Trinity.fasta'

# build an index of the fasta file
record_index = SeqIO.index(trinity_fasta, 'fasta')
record_keys = list(record_index.keys())
number_of_records = len(record_index)

# write batch_size records to fasta file
batch_size = 2000
i = 0
for start in range(0, number_of_records, batch_size):
    i += 1
    end = min(number_of_records, start + batch_size)
    file_name = ('trinity_chunk%(num)03i.fasta' % {'num': i})
    file_path = os.path.join(output_dir, file_name)
    keys_to_write = record_keys[start:end]
    records_to_write = (record_index[x] for x in keys_to_write)
    SeqIO.write(sequences=records_to_write,
                handle=file_path,
                format='fasta')
