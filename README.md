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
 


## Setup Instructions
To run this project, you need Conda and the required dependencies.


# Create and activate conda environment/ Run Scripts

```bash
conda create --name lipid_env python=3.9 rdkit pymol -c conda-forge
conda activate lipid_env
python scripts/generate_dopc.py
python scripts/visualize_dopc.py
python scripts/visualize_crispr.py
  
