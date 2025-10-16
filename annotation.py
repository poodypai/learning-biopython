from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

'''
sequence_1 = Seq('ACTGGATCGAACGATTGAC')
S_record = SeqRecord(sequence_1)
S_record.id = 'S_001'
S_record.name = "Biraj's Numero Uno"
S_record.description = "I wanna be the guanine to your cytosine."
S_record.annotations["Source"] = "Trust Me Bro!"
print(S_record)
print(S_record.annotations)
'''
print("Annotations Program!\n")
loop_var = int(input("How many data do you want to annotate?: "))
data = {}
Seq_record = []

for i in range(loop_var):
    print(f"\n--- Entry {i+1} ---")
    d_id = input("Enter ID: ")
    d_name = input("Enter Name: ")
    d_description = input("Enter Description: ")
    d_sequence = input("Enter Sequence: ")

    d_annotation_1 = input("Enter annotation key (e.g., Source): ")
    d_annotation_2 = input(f"Enter value for '{d_annotation_1}': ")

    
    data[d_id] = {
        "Name": d_name,
        "Description": d_description,
        "Sequence": Seq(d_sequence),
        d_annotation_1: d_annotation_2
    }

    
    record = SeqRecord(
        data[d_id]["Sequence"],
        id=d_id,
        name=d_name,
        description=d_description
    )
    record.annotations[d_annotation_1] = d_annotation_2

    Seq_record.append(record)

for record in Seq_record:
    print("\n")
    print(record)
    print("Annotations:", record.annotations)
    print("-" * 50)
