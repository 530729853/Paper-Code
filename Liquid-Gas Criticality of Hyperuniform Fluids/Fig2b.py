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
# from proplot import rc

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
size1 = 1
size2 = 5

NON = []



#####################################

# plt.yscale('linear')
plt.xscale('linear')
plt.yscale('log')
plt.figure(figsize=(5,5))

# plt.ylim( 0,7 )
H = 18.7
Tss = 100.0

s0 = 1.6*3
s1 = 0.6
s2 = 0.057
s3 = 2*s2
s4 = 0.45
s5 = 2
s6 = 4.0*math.sqrt( 2*math.pi )
A = 39*0+6.79
B = 3.45
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

# def func(x):
#     fx = x0**3 - x0 - x
#     return fx

# plt.xlim(0,2)

# rc["font.family"] = "Microsoft Arial"

# plt.xscale('log')
plt.xlim( 0.0, 1.1547 )
# plt.yscale('log')
# plt.figure(figsize=(5.4,5))
start = 0.03
x = np.linspace(start, 4, 10000)
# x = np.linspace(-2, 2, 1000)
Delta_x = x[1] - x[0]
y = []
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

for i in x :
    x0 = i
    root = sy.optimize.fsolve(func, 2)
    # root2 = sy.optimize.fsolve(func2, 10)
    if root[0] < 0 :
        root[0] = 0
        if AC_T == 0 :
            AC = i
    counter += (root[0]*B+A*i)*Delta_x
    y.append(root[0])

start = 0.05
x2 = np.linspace(start, 4, 10000)
y2 = []
Tss = 69.44445
for i in x2 :
    x0 = i
    root = sy.optimize.fsolve(func, 0.4)
    # root2 = sy.optimize.fsolve(func2, 10)
    if root[0] < 0 :
        root[0] = 0
        if AC_T == 0 :
            AC = i
    counter += (root[0]+A*i)*Delta_x
    y2.append(root[0])

start = 0.02
x3 = np.linspace(start, 4, 10000)

y3 = []
Tss = 17.361
for i in x3 :
    x0 = i
    if i < 0.1 :
        root[0] = 0
    else :
        root = sy.optimize.fsolve(func, 0.08)
        # root2 = sy.optimize.fsolve(func2, 10)
        if root[0] < 0 :
            root[0] = 0
            if AC_T == 0 :
                AC = i
    counter += (root[0]+A*i)*Delta_x
    y3.append(root[0])
dataX = []
data_xx = []
data_yy = []
if ( os.path.exists('bar_Z2.txt') ) :
	file_path = 'bar_Z2.txt'
	with open(file_path, 'r') as f:
            dataX = np.loadtxt(f, delimiter=" ")

for m in range(len(dataX)):
    if m <= 10 or m == len(dataX) - 1 :
        data_xx.append( dataX[m][0] ) 
        data_yy.append( dataX[m][1] )
    elif m % 4 == 0 :
        data_xx.append( dataX[m][0] ) 
        data_yy.append( dataX[m][1] )

plt.plot(data_xx, data_yy,linestyle='--', c='red',linewidth=3, label='$\Omega=15\epsilon~$(Simulation)',marker = '.',markerfacecolor='none',markeredgecolor='red',ms=20,markeredgewidth=3)
plt.plot(x, y, color='red', linewidth=3,label='$\Omega=15\epsilon~$(Theory)')
plt.plot(x2, y2, color='green', linewidth=3,label='$\Omega=10\epsilon~$(Theory)')

plt.plot(x3, y3, color='blue', linewidth=3,label='$\Omega=5\epsilon~$(Theory)')



# plt.scatter(data_xx, data_yy, c=color4, s=50)


ax = plt.gca()
axes = plt.subplot()
axes.minorticks_on()
plt.xticks([0.5, 1.0])
plt.tick_params(labelsize=20)
# plt.tick_params(which='major',width=2)
# plt.tick_params(which='minor',length=2.5)
# axes.tick_params(axis="both", which="major", direction="in", width=1, length=5)
# axes.tick_params(axis="both", which="minor", direction="in", width=1, length=3)
# axes.xaxis.set_minor_locator(MultipleLocator(0.4))


# plt.grid(True, which="major", linestyle="--", color="gray", linewidth=0.75)
# plt.grid(True, which="minor", linestyle=":", color="lightgray", linewidth=0.75)


plt.xlabel("$\phi_0$", fontdict={'size': 25}) #title of abscissa
plt.ylabel("$T_{t0}/\epsilon$", fontdict={'size': 25}) #title of ordinate

plt.legend(loc='best', ncol=1,fontsize=15)
# plt.legend(loc='best', ncol=1,fontsize=15)
plt.tight_layout()

plt.savefig('./Fig2b.png', dpi=300)
plt.close()

str = 's0='+str(s0)+',s1='+str(s1)+',s2='+str(s2)+',s3='+str(s3)+',s4='+str(s4)+',s5='+str(s5)+',Tss='+str(Tss)+',D_phi='+str(A)+',D_T=1'

print(str)

# plot_fig()


