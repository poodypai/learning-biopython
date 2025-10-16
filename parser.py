from Bio import SeqIO
for record in SeqIO.parse("files/p53-partial-cds.fasta","fasta"):
    print("ID:", record.id)
    print("Sequence:", record.seq)
    print(len(record.seq))
