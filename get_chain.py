from Bio import PDB

# Specify the PDB file path and chain ID
pdb_file = "3k1e.pdb"
chain_id = "A"  # Replace with the desired chain ID

# Parse the PDB file
parser = PDB.PDBParser(QUIET=True)
structure = parser.get_structure("structure", pdb_file)

# Get the model (usually the first model is relevant)
model = structure[0]

# Access the chain by its ID
try:
    chain = model[chain_id]
    print("Chain", chain_id, "successfully retrieved.")
except KeyError:
    print("Chain", chain_id, "not found in the PDB file.")

if chain:  # Check if chain was retrieved successfully
    io = PDB.PDBIO()
    io.set_structure(chain)
    output_filename = f"{structure.get_id()}_{chain.get_id()}.pdb"
    io.save(output_filename)
    print(f"Chain {chain.get_id()} saved to {output_filename}")

# Now you can work with the residues, atoms, etc. within the chain object 'chain'
