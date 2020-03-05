from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'Cl2'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 18
active_num = 18
geometry = get_geometry('NIST_3D_sdf/Cl2.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
