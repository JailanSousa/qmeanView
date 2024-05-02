import re
import pandas as pd
from glob import glob
from tqdm import tqdm
from Bio import PDB

import warnings
warnings.filterwarnings("ignore")

def remove_hatatm():

    results = "pdb_reference_set/"
    path = 'shorts_ref/*.pdb'
    monomers = pd.read_csv('short_ref_info.csv')

    for i in tqdm(glob(path)):
        pdb_file = "".join(re.findall(r'[A-Z0-9]{4}', i))

        for j in range(len(monomers)):
            pdb_code = monomers.PDB[j]
            chain_id = monomers.Chain[j]

            if str(pdb_file) == str(pdb_code):

                class NonHetSelect(PDB.Select):
                    def accept_residue(self, residue):
                        return 1 if residue.id[0] == " " else 0

                try: 
                    pdb = PDB.PDBParser().get_structure(pdb_file, 
                                                    f"shorts_ref/{pdb_file}.pdb")
                    model = pdb[0]

                    try:
                        chain = model[chain_id]
                        print("Chain", chain_id, "successfully retrieved.")
                    except KeyError:
                        print("Chain", chain_id, "not found in the PDB file.")

                        with open('log.txt', 'a') as f_obj:
                            f_obj.write(f"There is no {chain_id} in {pdb_file}.\n")

                    if chain:
                        io = PDB.PDBIO()
                        io.set_structure(chain)
                        output_filename = f"{pdb.get_id()}_{chain.get_id()}.pdb"
                        io.save(f"{results}{output_filename}", NonHetSelect())
                except ValueError:
                    print(f"{pdb_file} is empty")
                    with open('log_info_error.txt', 'a+') as f_obj:
                            f_obj.write(f"{pdb_file} is empty.\n")



remove_hatatm()