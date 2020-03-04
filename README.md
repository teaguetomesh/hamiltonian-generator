# hamiltonian-generator

All molecule data was taken from the NIST Chemistry WebBook
https://webbook.nist.gov/chemistry/

All geometries are taken from the available 3D SDF files in that database
https://webbook.nist.gov/chemistry/3d-structs/

All multiplicity and charge values are taken from the set of molecules used by
Tranter, Love, Mintert, Coveney 2018

All active and occupied spaces are taken from the same paper by dividing the
number of qubits by 2. This is due to the way OpenFermion handles active
spaces.
