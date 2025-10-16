from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
# Reading annotaions from file.
record = SeqIO.read("files/rhi-gene.gb", "genbank")

for data in record.annotations:
    print(f"{data} :  {record.annotations[data]}")

#Editing Annotation.
record.annotations["comment"] = "Edited by Biraj Thapa"
record.annotations["source"] = "Trust Me Bro!"

#Writing a new file
submit = SeqIO.write(record, "edited.gb", "genbank")

#Read the new file.
record = SeqIO.read("edited.gb", "genbank")

#Print to check
print(record.annotations["comment"], record.annotations["source"])

