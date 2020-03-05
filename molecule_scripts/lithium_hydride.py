from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'LithiumHydride'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 6
active_num = 6
geometry = get_geometry('NIST_3D_sdf/lithium_hydride.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
