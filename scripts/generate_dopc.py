from rdkit import Chem
from rdkit.Chem import AllChem

# Define DOPC lipid molecule (SMILES representation)
dopc_smiles = "CCCCCCCC=CCCCCCCCCCCOC(=O)CC[N+](C)(C)CCOP(=O)(O)OCC(COC(=O)CCCCCCCC=CCCCCCCCCC)OC"

# Convert SMILES to RDKit molecule
dopc_mol = Chem.MolFromSmiles(dopc_smiles)

# Generate 3D conformation
dopc_mol = Chem.AddHs(dopc_mol)  # Add hydrogens
AllChem.EmbedMolecule(dopc_mol, AllChem.ETKDG())  # Generate 3D conformation
AllChem.UFFOptimizeMolecule(dopc_mol)  # Energy minimization

# Save molecule to SDF format
Chem.MolToMolFile(dopc_mol, "data/dopc_3d.sdf")

print("✅ DOPC 3D structure saved as 'data/dopc_3d.sdf'")
