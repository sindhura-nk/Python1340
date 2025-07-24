import calculations.fact2
import fact
op1 = fact.fact_data(5)
print(op1)

from fact import fact_data
op2 = fact_data(10)
print(op2)

import root
sq = root.sq_root(64)
cb = root.cube_root(27)
print(sq,cb)

from root import sq_root
sq2 = sq_root(144)
print(sq2)
#cb2 = cube_root(216)

print("=============================")
print("Packages Revision")
# packages
import calculations
f1 = calculations.fact2.fact(10)
print(f1)

from calculations import squareroot
s3 = squareroot.square_root(9)
print(s3)

from calculations.squareroot import square_root
s4 = square_root(16)
print(s4)