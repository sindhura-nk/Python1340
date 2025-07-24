'''
Modules
'''
# import fact_data function from the module:fact
from fact import fact_data
factdata = fact_data(10)
print(f"Using from and Import method: {factdata}")

import root
square_root = root.sq_root(16)
print(f"Using Import method: {square_root}")
cube_root = root.cube_root(64)
print(f"Using Import method: {cube_root}")

# for above scenario, instead of using root.sq_root and root.cube_root you can use from import
from root import sq_root,cube_root
# If you would like to import everything, then you can use import *
from root import *

# ----------------------------------------------------------
'''
Packages
'''
import calculations
print(f"Importing from package: {calculations.fact2.fact(10)}")

# we can also use from import method
from calculations import squareroot
print(f"Importing from package using from-import : {squareroot.square_root(36)}")

# we can also import in below fashion
from calculations.squareroot import square_root
print(f"Importing from package using from-import2 : {square_root(100)}")
