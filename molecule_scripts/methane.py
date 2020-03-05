from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'Methane'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 9
active_num = 9
geometry = get_geometry('NIST_3D_sdf/methane.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
