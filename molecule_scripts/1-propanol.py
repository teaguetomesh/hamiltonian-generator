from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = '1-propanol'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 28
active_num = 28
geometry = get_geometry('NIST_3D_sdf/1-propanol.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
