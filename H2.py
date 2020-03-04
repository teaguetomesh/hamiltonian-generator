from test_set_generator import generate_hamiltonians
from util_funcs import get_geometry

name = 'H2'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 2
active_num = 2
geometry = get_geometry('NIST_3D_sdf/1333-74-0-3d.sdf')

generate_hamiltonians(name, charge, multiplicity, description, geometry, occupied_num, active_num)
