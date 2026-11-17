import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as m
import pandas as pd

def forward_diff(f, x, h):  return (f(x + h) - f(x)) / h
def backward_diff(f, x, h): return (f(x) - f(x - h)) / h
def central_diff(f, x, h):  return (f(x + h) - f(x - h)) / (2 * h)   # fixed
"""
def double_diff(f, x, h):   return (f(x + h) - 2 * f(x) + f(x - h)) / h**2

t = sp.symbols("t", positive=True)
T = 30 + 58 * sp.exp(-0.075 * t)
T_diff = sp.diff(T, t)

def f(x): return 30 + 58 * math.exp(-0.075 * x)

# 1
exact = float(T_diff.subs(t, 5))
print(sp.N(T_diff.subs(t, 5), 6))             # about -2.98963

# 2
h = [10.0**(-i) for i in range(13)]            # 1, 0.1, ..., 1e-12
forward  = [forward_diff(f, 5, i)  for i in h]
backward = [backward_diff(f, 5, i) for i in h]
central  = [central_diff(f, 5, i)  for i in h]

err_f = [abs(v - exact) for v in forward]
err_b = [abs(v - exact) for v in backward]
err_c = [abs(v - exact) for v in central]

m.loglog(h, err_f, "o-", label="forward diff")
m.loglog(h, err_b, "s-", label="backward diff")
m.loglog(h, err_c, "^-", label="central diff")
m.xlabel("step size h")
m.ylabel("absolute error")
m.legend()
m.grid(True, which="both")
m.show()

t=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
s=np.array([0,0.9,3.6,8.1,14.4,22.5,32.4,43.3,54.0,64.8,75.6,85.2,92.2,96.7,98.8])
v=np.zeros(15)
v[0]=s[1]-s[0]
v[-1]=s[-1]-s[-2]
v[1:-1]=(s[2:]-s[:-2])/2
print(v)

a=(v[2:]-v[:-2])/

df=pd.read_csv(r"C:\Users\Harshini.M\OneDrive\Desktop\course\computing in mech\lift.csv")
print(df.shape)
print(pd.DataFrame(df))
print(df.head())
t=df["t"].values
z=df["z"].values
v=np.zeros(len(z))
v[0]=(z[1]-z[0])/(t[1]-t[0])
v[-1]=(z[-1]-z[-2])/(t[-1]-t[-2])
v[1:-1]=(z[2:]-z[:-2])/(t[2:]-t[:-2])
"""


m=[0,50,100,150,200,250,300,350]
e=[0.4,20.8,40.9,60.9,80.1,100.9,121.7,140.0]
f=[i*9.81 for i in m]