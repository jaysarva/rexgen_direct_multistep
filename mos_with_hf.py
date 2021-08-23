from pyscf import gto,scf
import openbabel


obConversion = openbabel.OBConversion()
obConversion.SetInAndOutFormats("smi", "xyz")

mol = openbabel.OBMol()
obConversion.ReadString(mol, smilestring)

outXYZ = obConversion.WriteString(mol)
#### maybe need to remove first number from outXYZ because it details number of atoms in molecule??

mol = gto.M(
    atom = outXYZ,
    basis = 'sto-3g',
)


rhf_h2o = scf.RHF(mol)
e_h2o = rhf_h2o.kernel()
