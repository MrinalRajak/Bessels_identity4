
#Bessel's identity
#(4) 1 = jn(0,x)^2 + 2*∑_(n=1)^∞▒〖jn(n,x)^2〗

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=1
s=0.0
term=2*(jn(n,x))**2
LHS=1.0
RHS=(jn(0,x))**2+term
while(abs(LHS-RHS)>1.0e-10):
    term=2*(jn(n,x))**2
    s=s+term
    RHS=(jn(0,x))**2+s
    n=n+1

print("LHS: ",LHS)
print("RHS: ",RHS)
