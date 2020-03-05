from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'Methanal'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 12
active_num = 12
geometry = get_geometry('NIST_3D_sdf/methanal.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
