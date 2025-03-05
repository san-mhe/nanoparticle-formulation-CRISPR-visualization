# Nanoparticle Formulation & CRISPR Visualization

## Overview
This project models and visualizes a DOPC lipid nanoparticle interacting with CRISPR-Cas9.  
It explores lipid-based delivery systems for CRISPR by **structurally positioning the nanoparticle near Cas9**.

Generated & visualized a lipid nanoparticle (DOPC)  
Loaded & positioned CRISPR-Cas9 (PDB: 5F9R)  
Measured distances between lipid & Cas9 active site  

# Key Findings
DOPC was successfully generated and visualized.
CRISPR-Cas9 was loaded and positioned near the lipid.
Measured interaction distance to study lipid-based CRISPR delivery.


## References & Attributions

### Datasets & Structures
- CRISPR-Cas9 Protein Structure (PDB: 5F9R)
- Source: [Protein Data Bank (PDB)](https://www.rcsb.org/structure/5F9R)  
- Citation:  
  *Nishimasu, H., Ran, F. A., Hsu, P. D., Konermann, S., Shehata, S. I., Dohmae, N., Ishitani, R., Zhang, F., & Nureki, O. (2014). Crystal structure of catalytically-active Streptococcus pyogenes CRISPR-Cas9 in complex with single-guided RNA and double-stranded DNA primed for target DNA cleavage. Protein Data Bank.  
- DOI: [10.2210/pdb5F9R/pdb](https://doi.org/10.2210/pdb5F9R/pdb)

- Lipid Nanoparticle (DOPC) SMILES Data  
  - Source: [PubChem](https://pubchem.ncbi.nlm.nih.gov/)  
  - DOPC SMILES: `"CCCCCCCC=CCCCCCCCCC(=O)OC(C[N+](C)(C)COP(=O)(O)OCC(COC(=O)CCCCCCCC=CCCCCCCCCC)OCC)"`  
  - Citation:  
    National Center for Biotechnology Information. (2024). DOPC - PubChem Compound Summary. 

### Tools & Software
- RDKit (Molecular Modeling)  
  - Source: [RDKit Documentation](https://www.rdkit.org/)  
- PyMOL (Molecular Visualization)  
  - Source: [PyMOL by Schrödinger](https://pymol.org/)  
- Python (v3.9) & Conda Environment  
  - Dependencies: `rdkit`, `pymol`, `numpy`, `matplotlib` 


## Setup Instructions
To run this project, you need Conda and the required dependencies such as RDkit and PyMOL.


# Create and activate conda environment/ Run Scripts

```bash
conda create --name lipid_env python=3.9 rdkit pymol -c conda-forge
conda activate lipid_env
python scripts/generate_dopc.py
python scripts/visualize_dopc.py
python scripts/visualize_crispr.py
  
