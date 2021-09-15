from pymatgen import Structure
import pymatgen.io
from pymatgen.io.vasp.inputs import Poscar, Potcar

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cif', type=str, required=True, help='give the path of .cif file')
parser.parse_args()

if __name__ == '__main__':
	args = parser.parse_args()
	cif_path = args.cif	
	struc = Structure.from_file(cif_path)
	poscar = Poscar(struc)
	poscar.write_file('./POSCAR')
	potcar = Potcar(['Li', 'O', 'C'], functional='PBE')
	potcar.write_file('./POTCAR')


