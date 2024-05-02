
import urllib
import os
import pandas as pd
from tqdm import tqdm

def get_ref(file):

        """Download strutucture in pdb format."""
        ref = pd.read_csv(file)
        
        
        for i in tqdm(range(len(ref))):
            
            pdb_id = ref.pdb_code[i]
            print(pdb_id)
        
            try:
                     
                URL = f'https://files.rcsb.org/download/{pdb_id}.pdb'
                os.system(f'wget -P shorts_ref/ {URL}')
                    
            except (urllib.error.HTTPError, urllib.error.URLError):
                
                log_msg = f"pdb file {pdb_id} not found (download: error 404)\n"
                with open('shorts_ref/log_error.txt', 'a+') as obj:
                     obj.write(log_msg)

file = 'acession_pdb_code.csv'
get_ref(file)

file = '/home/jssousa/Documentos/peps_minor_than_40.csv'

data = pd.read_csv(file)

shorts_seqs = data[data['Length'] <= 40]

shorts_seqs.to_csv('shorter_seqs.csv', index=False)