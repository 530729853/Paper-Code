import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy as sy
import pylab as plb
from scipy import integrate
from matplotlib import colors
import os.path
import math
import random
import sympy
from matplotlib.ticker import MultipleLocator


color1 = '#FF6666'
color2 = '#99CC33'
color3 = '#CC9933'
color4 = '#003366'
color5 = '#66CCCC'
color6 = '#9933CC'
color7 = '#FF9900'
color8 = '#663300'
color9 = '#009966'
color10 = '#99CCFF'
color11 = '#CC9999'
color12 = '#99CC33'
color13 = '#FFA07A'
color14 = '#FA8072'
color15 = '#E9967A'
color16 = '#F08080'
color17 = '#CD5C5C'
color18 = '#DC143C'
color19 = '#B22222'
color20 = '#FF0000'
color21 = '#8B0000'
color22 = '#FF7F50'
color23 = '#FF6347'
color24 = '#FF4500'
color25 = '#FFD700'
color26 = '#FFA500'
color27 = '#FF8C00'
color28 = '#7CFC00'
color29 = '#32CD32'
color30 = '#00FF7F'



NON = []



#####################################

plt.yscale('linear')
plt.xscale('linear')
plt.figure(figsize=(5,4.55))

plt.xlim( 0.0,120.0 )
plt.ylim( -0.03, 10.5 )
H = 26.375
Tss = 625

s0 = 1.6*3
s1 = 0.5
s2 = 0.25
s3 = 0.5
s4 = 0.25
s5 = 2
s6 = 4.0*math.sqrt( 2*math.pi )
A = 39
B = 0.7
C = 1

# s1 = C*s1
# s2 = C*s2
# s5 = s5 / C
# A = C*A



x0 = 0
def func(x):
    if x > 0 :
        E = 2.0 * math.sqrt( math.pi ) * ( 1 - math.exp( -s6*x0*math.sqrt(x) ) )
        Aa = s4*math.sqrt(x) + s5 / ( x0*E )
        fx = s0*math.sqrt(Aa)*math.sqrt(Tss)/math.sqrt(s3) - math.pow(x,1/4)*(s0+s1*E*x0*math.sqrt(x))*Aa/s3 + s2*E*x0*math.pow(x,5/4)
    else:
        fx = 0
    return fx

def func2(x):
    x = x - A*x0
    if x > 0 :
        E = 2.0 * math.sqrt( math.pi ) * ( 1 - math.exp( -s6*x0*math.sqrt(x) ) )
        Aa = s4*math.sqrt(x) + s5 / ( x0*E )
        fx = s0*math.sqrt(Aa)*math.sqrt(Tss)/math.sqrt(s3) - math.pow(x,1/4)*(s0+s1*E*x0*math.sqrt(x))*Aa/s3 + s2*E*x0*math.pow(x,5/4)
    else:
        fx = 0
    return fx

def func3(y):
    x = H
    if x > 0 :
        E = 2.0 * math.sqrt( math.pi ) * ( 1 - math.exp( -s6*x0*math.sqrt(x) ) )
        Aa = s4*math.sqrt(x) + s5 / ( x*y*E )
        fx = s0*math.sqrt(Aa)*math.sqrt(Tss)/math.sqrt(s3) - math.pow(x,1/4)*(s0+s1*E*y*math.sqrt(x))*Aa/s3 + s2*E*y*math.pow(x,5/4)
    else:
        fx = 0
    return fx

# def func2(x):
#     fx = x0**3 - x0 - x
#     return fx



start = 0.01
x = np.linspace(start, 4, 1000)
# x = np.linspace(-2, 2, 1000)
Delta_x = x[1] - x[0]
y = []
x2 = []
y2 = []
y3 = []
line1 = []
counter = 0
Zeros = []
Zeros_Z = []
AC = 0
AC_T = 0
# print(sy.optimize.fsolve(func3, 0.1))
# print(sy.optimize.fsolve(func3, 0.8))
# print(sy.optimize.fsolve(func3, 2))

x22 = []
y22 = []

for i in x :
    x0 = i
    root = sy.optimize.fsolve(func, 200)
    # root2 = sy.optimize.fsolve(func2, 10)
    if root[0] < 0 :
        root[0] = 0
        if AC_T == 0 :
            AC = i
        x22.append(i)
        y22.append(0)
    else :
        x22.append(i)
        y22.append(root[0]*B+A*i)
    y2.append(root[0]*B+A*i)
    line1.append( H )

x1 = np.linspace(0,60,100)
x2 = np.linspace(60,120,100)

y1 = 10.0 / ( 1.0 + np.exp( - x1 + 1.5*20.0 ) )
y2 = 10.0 / ( 1.0 + np.exp(   x2 - 4.5*20.0 ) )


plt.plot(x1, y1, color='black',linewidth=3)
plt.plot(x2, y2, color='black',linewidth=3)

# plt.plot(x, line1, color='black')
# plt.plot(X1, L1, color='black',linestyle='--',linewidth=3)
# plt.plot(X2, L2, color='black',linestyle='--',linewidth=3)

# plt.scatter(Zeros[0][0],Zeros[0][1])
# plt.scatter(Zeros[1][0],Zeros[1][1])
# plt.scatter(Zeros[2][0],Zeros[2][1])

ax = plt.gca()
axes = plt.subplot()
axes.minorticks_on()
plt.tick_params(labelsize=15)
# axes.tick_params(axis="both", which="major", direction="in", width=1, length=5)
# axes.tick_params(axis="both", which="minor", direction="in", width=1, length=3)
# axes.xaxis.set_minor_locator(MultipleLocator(0.4))


# plt.grid(True, which="major", linestyle="--", color="gray", linewidth=0.75)
# plt.grid(True, which="minor", linestyle=":", color="lightgray", linewidth=0.75)


plt.xlabel("$x/\sigma$", fontdict={'size': 18}) #title of abscissa
plt.ylabel("$\\tilde{h}(x,y)$", fontdict={'size': 18}) #title of ordinate

# plt.legend(loc='best', ncol=1,fontsize=12)
plt.tight_layout()

plt.savefig('./FigS5.png', dpi=300)
plt.close()

str = 's0='+str(s0)+',s1='+str(s1)+',s2='+str(s2)+',s3='+str(s3)+',s4='+str(s4)+',s5='+str(s5)+',Tss='+str(Tss)+',D_phi=1,D_T='+str(A)

print(str)

# plot_fig()


