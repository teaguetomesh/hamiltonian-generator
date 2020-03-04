import sys
import os
from pathlib import Path
from openfermion.hamiltonians import MolecularData
from openfermion.transforms import get_fermion_operator, get_interaction_operator
from openfermionpsi4 import run_psi4
from openfermion.transforms import (jordan_wigner, bravyi_kitaev, bravyi_kitaev_fast, bravyi_kitaev_tree,
                                    binary_code_transform, reverse_jordan_wigner)
from openfermion.transforms._binary_codes import parity_code


def generate_and_save(geometry, basis, multiplicity, charge, description, mfilename):
    # initialize the molecule
    molecule = MolecularData(geometry,basis,multiplicity,charge,description=description,filename=mfilename)
    molecule.save()

    # compute the active space integrals
    print('-computing integrals-')
    molecule = run_psi4(molecule,run_mp2=True,run_cisd=True,run_ccsd=True,run_fci=True)

    print(molecule.filename)
    print(molecule.two_body_integrals)
    print(molecule.canonical_orbitals)
    molecule.save()
    print('Successful generation')


def load_and_transform(filename, orbitals, transform):
    # Load data
    print('--- loading molecule ---')
    molecule = MolecularData(filename=filename)

    print('filename: {}'.format(molecule.filename))
    #print('n_atoms: {}'.format(molecule.n_atoms))
    #print('n_electrons: {}'.format(molecule.n_electrons))
    #print('n_orbitals: {}'.format(molecule.n_orbitals))
    #print('Canonical Orbitals: {}'.format(molecule.canonical_orbitals))
    #print('n_qubits: {}'.format(molecule.n_qubits))

    # get the Hamiltonian for a specific choice of active space
    # set the Hamiltonian parameters
    occupied_orbitals, active_orbitals = orbitals

    molecular_hamiltonian = molecule.get_molecular_hamiltonian(
                 occupied_indices=range(occupied_orbitals),
                 active_indices=range(active_orbitals))

    # map the operator to fermions and then qubits
    fermion_hamiltonian = get_fermion_operator(molecular_hamiltonian)

    # get interaction operator
    interaction_hamiltonian = get_interaction_operator(fermion_hamiltonian)

    if transform is 'JW':
        qubit_h = jordan_wigner(fermion_hamiltonian)
        qubit_h.compress()
    elif transform is 'BK':
        qubit_h = bravyi_kitaev(fermion_hamiltonian)
        qubit_h.compress()
    elif transform is 'BKSF':
        qubit_h = bravyi_kitaev_fast(interaction_hamiltonian)
        qubit_h.compress()
    elif transform is 'BKT':
        qubit_h = bravyi_kitaev_tree(fermion_hamiltonian)
        qubit_h.compress()
    elif transform is 'PC':
        qubit_h = binary_code_transform(fermion_hamiltonian, parity_code(2*active_orbitals))
        qubit_h.compress()
    else:
        print('ERROR: Unrecognized qubit transformation: {}'.format(transform))
        sys.exit(2)

    return qubit_h


def write_to_file(filename, name, hamiltonian, description):
    # write the resulting qubit H to file
    print('\n\n~~ writing Qubit Hamiltonian to file~~\n')
    print('filename: {}'.format(filename))
    with open(filename, 'w') as H_file:
        H_file.write('{} Qubit Hamiltonian\n'.format(name))
        hstring = '{}'.format(hamiltonian)
        terms = hstring.split('\n')
        for t in terms:
            t2 = t.split('[')
            if len(t2) is 2:
                coef = t2[0]
                paul = t2[1].split(']')[0]
                # Check for identity operator
                if paul is '':
                    paul = 'I0'

                # Write coefficients and operators to file
                H_file.write('{0:17s} {1}\n'.format(coef,paul))

            else:
                print('ERROR: Something went wrong parsing string')
    print('Successful write\n')


def get_geometry(filename):
    with open(filename, 'r') as molfile:
        allLines = molfile.readlines()
        startidx = 0
        for i, line in enumerate(allLines):
            if 'Copyright' in line:
                startidx = i+1
                break

        num_atoms = int(allLines[startidx].split()[0])
        geometry = []
        for n in range(startidx+1,startidx+1+num_atoms):
            xcoord, ycoord, zcoord, atom = allLines[n].split()[:4]
            geometry.append((atom, (float(xcoord), float(ycoord), float(zcoord))))
    return geometry











