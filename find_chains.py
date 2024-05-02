import re
import pandas as pd

from Bio import PDB
from glob import glob
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

files = 'shorts_ref/*.pdb'

structure_info = []
for file in tqdm(glob(files)):
    pdb_file = "".join(re.findall(r'[A-Z0-9]{4}', file))

    parse = PDB.PDBParser()
    structure = parse.get_structure(pdb_file, f"shorts_ref/{pdb_file}.pdb")
    model = structure[0]
    ppbuid = PDB.PPBuilder()
    polypeptyde = ppbuid.build_peptides(model)
    

    for pp, chain in zip(polypeptyde, model):
        seq = pp.get_sequence()
        if len(seq) <= 40:
            structure_data = {
                'PDB' : pdb_file, 
                'Chain' : chain.get_id(), 
                'Length' : len(seq)
                }
            
            structure_info.append(structure_data)


df = pd.DataFrame(structure_info)
df.to_csv('short_ref_info.csv', index=False)