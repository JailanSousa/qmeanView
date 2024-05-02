import re
import pandas as pd

def non_membrane_protein(file):
    with open(file) as f_obj:
        fastas = f_obj.read()

        fastas = fastas.split('\n\n')

        for fasta in fastas:
        
            if 'membrane' in fasta.lower():
                pass
            else:
                pdb = fasta.split(' ')[0]
                #chain = pdb[-1]
                if pdb[1:6]:
                    code = str(pdb[1:5])
                    chain = str(pdb[-1])

                    with open('until_200aa.csv', 'a') as obj:

                        obj.write(f"{code},{chain}\n")

def len_aa_200(file):
    
    with open(file, 'r') as f_obj:
        #fastas = f_obj.read().split('\n\n')
        fastas = f_obj.readlines()

        for fasta in fastas:

            #print(fasta[0])

            if fasta[0] == '>':
                pdb = fasta.split(' ')[0][1:5]

            else:
                seq = (fasta.rstrip('\n'))
                if seq:
                    print(len(seq))
                
                #seq = f"{re.findall(r'(?=]).+', fasta, re.DOTALL)}\n"
                #print(seq)
                
def split_code_chain(file):

    data = pd.read_csv(file)
    reference = []
    for i in range(len(data)):

        struture = {
                    "PDB":data['PDBchain'][i][0:4],
                    "Chain":data['PDBchain'][i][4:]
                    }
        
        reference.append(struture)
    
    reference_set = pd.DataFrame(reference)
    reference_set.to_csv('200aa_reference_set.csv', index=False)

def remove_redundance(file):

    data = pd.read_csv(file)

    data = data.drop_duplicates(subset=['pdb_code'], keep=False)
    data.to_csv('acession_pdb_code.csv', index=False)

file = 'acession_pdb_code.csv'
remove_redundance(file)