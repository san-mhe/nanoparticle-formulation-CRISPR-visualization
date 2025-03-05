import os

print("🔬 Running Lipid-Based Nanoparticle Formulation Project...")

# Step 1: Generate DOPC
os.system("python scripts/generate_dopc.py")

# Step 2: Visualize DOPC in PyMOL
os.system("python scripts/visualize_dopc.py")
