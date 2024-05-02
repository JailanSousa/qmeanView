import re
import pandas as pd
from glob import glob
from tqdm import tqdm
import shutil


def get_monomers():

    reference = pd.read_csv('until_200aa.csv')
    files = '/*.pdb'

    for i in tqdm(glob(files)):
        pdb_file = "".join(re.findall(r'[A-Z0-9]{4}', i))

        for j in range(len(reference)):
            pdb_code = reference.PDB[j]
            chain = reference.Chain[j]

            try:
                if str(pdb_file) == str(pdb_code):
                    shutil.move(f"pdb_reference_set/{pdb_file}_{chain}.pdb", 'monomers/')
    
            except FileNotFoundError:
                with open('log_error.txt', 'a+') as f_obj:
                    f_obj.write(f"{pdb_file}_{chain}.pdb\n")


get_monomers()
print('Done!')