from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
# Simple Sequence conversions
seq_1 = Seq("ATCGTGGCATGGCATTGCCCCGCCGCGATTGATGCCATG")
print("Sequence:",seq_1)
print(f"GC Content: {gc_fraction(seq_1)}")
print(f"Transcribed: {seq_1.transcribe()}")
print(f"Translated: {seq_1.transcribe().translate()}")

seq_2 = Seq("ACGATTGACCCAT")
seq_3 = Seq("ATCGCATTGACTA")

seq_concatenate = seq_2 + seq_3
print(f"Adding: {seq_2} & {seq_3} \n Result:{seq_concatenate}")
print("Complementing Sequence 2:")
print(f"{seq_2}\n{seq_2.complement()}")



