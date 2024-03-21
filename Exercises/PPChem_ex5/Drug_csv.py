import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
import mordred

drugs = pd.read_csv("chembl_drugs.csv", sep= ";")
df = pd.DataFrame(drugs)
drugs_filtered = df[df['Phase']==4]


drugs_filtered_2 = drugs_filtered[pd.notna(drugs_filtered['Smiles'])]


approved_drugs = drugs_filtered_2[~drugs_filtered_2["Smiles"].str.contains("\.")]
approved_drugs.reset_index(inplace = True, drop = True)

approved_drugs["My_Mol"] = approved_drugs["Smiles"].apply(Chem.MolFromSmiles)

# Use smiles directly, wihtout storing Mol Objects
approved_drugs["number of atoms"] = approved_drugs["Smiles"].apply(lambda x: Chem.MolFromSmiles(x).GetNumAtoms())
print(approved_drugs)

approved_drugs['NumRotatableBonds'] = approved_drugs['My_Mol'].apply(lambda x: Descriptors.NumRotatableBonds(x))
approved_drugs['NumHDonors'] = approved_drugs['My_Mol'].apply(lambda x: Descriptors.NumHDonors(x))
approved_drugs['NumHAcceptors'] = approved_drugs['My_Mol'].apply(lambda x: Descriptors.NumHAcceptors(x))
approved_drugs['MolWt'] = approved_drugs['My_Mol'].apply(lambda x: Descriptors.MolWt(x))
approved_drugs['MolLogP'] = approved_drugs['My_Mol'].apply(lambda x: Descriptors.MolLogP(x))
approved_drugs['NumValenceElectrons'] = approved_drugs['My_Mol'].apply(lambda x: Descriptors.NumValenceElectrons(x))

print(approved_drugs)

from rdkit import Chem
from mordred import Calculator, AtomCount

# Only calculate AtomCount descriptors
calc = Calculator(AtomCount, ignore_3D = True)

# Apply the calculator to the molecules
mordred_df = calc.pandas(approved_drugs["My_Mol"])

# Only extract the number of halogens
approved_drugs = pd.concat([approved_drugs, mordred_df[["nF", "nBr", "nCl", "nI"]]], axis = 1)

# Add the total number of halogens
approved_drugs["nX"] = approved_drugs[["nF", "nBr", "nCl", "nI"]].sum(axis = 1)

print(approved_drugs)