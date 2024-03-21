from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw


mol2 = Chem.MolFromSmiles('C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](Cc3c2c(c4c(c3O)C(=O)c5cccc(c5C4=O)OC)O)(C(=O)CO)O)N)O')

AllChem.EmbedMolecule(mol2)

mol_sdf3D = Chem.MolToMolBlock(mol2)
print(mol_sdf3D)

img = Draw.MolToImage((mol2))
img.show()
