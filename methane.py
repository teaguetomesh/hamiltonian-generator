from test_set_generator import generate_hamiltonians
from util_funcs import get_geometry

name = 'Methane'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 9
active_num = 9
geometry = get_geometry('NIST_3D_sdf/74-82-8-3d.sdf')
generate_hamiltonians(name, charge, multiplicity, description, geometry, occupied_num, active_num)
