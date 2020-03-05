from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'O2'
multiplicity = 1
charge = 0
description = 'NIST_singlet'
occupied_num = 10
active_num = 10
geometry = get_geometry('NIST_3D_sdf/O2.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
