from test_set_generator import generate_hamiltonians
from util_funcs import get_geometry

name = 'Ethane'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 16
active_num = 16
geometry = get_geometry('NIST_3D_sdf/74-84-0-3d.sdf')
generate_hamiltonians(name, charge, multiplicity, description, geometry, occupied_num, active_num)
