from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'Ethene'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 14
active_num = 14
geometry = get_geometry('NIST_3D_sdf/ethene.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
