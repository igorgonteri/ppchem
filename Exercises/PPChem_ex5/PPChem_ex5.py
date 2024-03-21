from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
IPythonConsole.ipython_useSVG=True


mol2 = Chem.MolFromSmiles('C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](Cc3c2c(c4c(c3O)C(=O)c5cccc(c5C4=O)OC)O)(C(=O)CO)O)N)O')
print(mol2)
AllChem.EmbedMolecule(mol2)

mol_sdf3D = Chem.MolToMolBlock(mol2)
print(mol_sdf3D)

img = Draw.MolToImage((mol2))
img.show()

#ex 3

tylenol_smiles = "CC(=O)NC1=CC=C(C=C1)O"
tylenol = Chem.MolFromSmiles(tylenol_smiles)


for atom in tylenol.GetAtoms():
        print('Atom :',atom.GetSymbol())
        print('Atomic number :',atom.GetAtomicNum())
        print('Atom index :',atom.GetIdx())
        print('Degree :',atom.GetDegree())
        print('Valence :',atom.GetTotalValence())
        print('Hybridization :',atom.GetHybridization())
        print('==========================================')

for bond in tylenol.GetBonds():
        print('Bond:', )
        print('Bond index:', )
        print('Atom 1:',)
        print('Atom 2:',)
        print('Is Conjugated:',)
        print('Is Aromatic:',)
        print('=========================================')

clavulanic_acid_smiles = "O=C2N1[C@H](C(/O[C@@H]1C2)=C/CO)C(=O)O"
clav_mol = Chem.MolFromSmiles(clavulanic_acid_smiles)
for atom in clav_mol.GetAtoms():
        if atom.GetSymbol() == 'N':
                print(f'Atom: {atom.GetSymbol()}, Index: {atom.GetIdx()},Hybridization: {atom.GetHybridization()}, Degree : {atom.GetDegree()}')
                for neighbor in atom.GetNeighbors():
                        print(f'Neighbour: {neighbor.GetIdx(),neighbor.GetSymbol()}')
                        print(f'Bond Order: {clav_mol.GetBondBetweenAtoms(atom.GetIdx(),neighbor.GetIdx()).GetBondType()}')


