from test_set_generator import gen_multiple_AS
from util_funcs import get_geometry

name = 'CarbonDioxide'
multiplicity = 1
charge = 0
description = 'NIST'
occupied_num = 15
active_num = 15
geometry = get_geometry('NIST_3D_sdf/carbon_dioxide.sdf')
gen_multiple_AS(name, charge, multiplicity, description, geometry, occupied_num)
