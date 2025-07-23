# This module calculates the factorial of the given number
def fact_data(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p