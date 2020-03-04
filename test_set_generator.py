import sys
import os
from pathlib import Path
from util_funcs import *


def generate_hamiltonians(name, charge, multiplicity, description, geometry, occupied_num, active_num):
    """Generate 2 Hamiltonians for the given molecule:
    JW encoding + STO-3G basis
    BK encoding + STO-3G basis
    """
    if multiplicity == 1:
        mult = 'singlet'
    elif multiplicity == 2:
        mult = 'doublet'
    elif multiplicity == 3:
        mult = 'triplet'
    elif multiplicity == 4:
        mult = 'quartet'
    else:
        raise Exception('Unknown Multiplicity')

    if not os.path.isdir('molecule_data/'):
        os.mkdir('molecule_data/')

    for basis in ['sto-3g']:
        molecule_file = 'molecule_data/{}_{}_{}_{}'.format(name,basis,mult,description)

        print('--- Generate Molecule: {}_{}_{} ---'.format(name,basis,description))

        generate_and_save(geometry, basis, multiplicity, charge, description, molecule_file)

        # Load the molecule and perform qubit transformation
        orbitals = (occupied_num, active_num)

        for transform in ['JW', 'BK']:
            qubit_h = load_and_transform(molecule_file, orbitals, transform)

            # Write the qubit hamiltonian to file
            folder = 'testset_hamiltonians/'
            if not os.path.isdir(folder):
                os.mkdir(folder)

            fn = '{}_{}_{}_{}_AS{}.txt'.format(name,basis,transform, description,active_num)
            write_to_file(folder+fn,name,qubit_h,description)
