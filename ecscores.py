# ecscores.py
#callable function to use within own code
from rdkit import Chem
from rdkit.Chem import RDKFingerprint, DataStructs

def ecscore(initial_smiles, final_smiles): 
    mol_a = Chem.MolFromSmiles(initial_smiles) # compound you want to compare to final compound (e.g. any other intermediate in a total)
    mol_b = Chem.MolFromSmiles(final_smiles) #final compound you compare to (e.g. last step in a total)
    if mol_a is None:
        raise ValueError("Invalid initial_smile: cannot be parsed by RDKit.")
    if mol_b is None:
        raise ValueError("Invalid final_smile: cannot be parsed by RDKit.")
    
    fp_a = RDKFingerprint(mol_a)
    fp_b = RDKFingerprint(mol_b)

    return float(DataStructs.FingerprintSimilarity(fp_a, fp_b))


