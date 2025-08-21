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
plt.figure(figsize=(5,5.1))

plt.xlim( 0.01, 2.5 )
plt.ylim( 5.7, 33.0 )
H = 28.3
Tss = 156.25

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

# plt.yscale('log')

start = 0.02
x = np.linspace(start, 4, 10000)
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
    root = sy.optimize.fsolve(func, 6)
    # root2 = sy.optimize.fsolve(func2, 10)
    if root[0] < 0 :
        root[0] = 0
        if AC_T == 0 :
            AC = i
    else :
        x22.append(i)
        y22.append(root[0]*B+A*i)
    y2.append(root[0]*B+A*i)
    line1.append( H )

Tss = 69.4444444444
x33 = []
y33 = []
for i in x :
    x0 = i
    root = sy.optimize.fsolve(func, 6)
    # root2 = sy.optimize.fsolve(func2, 10)
    if root[0] < 0 :
        root[0] = 0
        if AC_T == 0 :
            AC = i
    else :
        x33.append(i)
        y33.append(root[0]*B+A*i)

Tss = 17.3611111111
x44 = []
y44 = []
for i in x :
    x0 = i
    root = sy.optimize.fsolve(func, 6)
    # root2 = sy.optimize.fsolve(func2, 10)
    if root[0] < 0 :
        root[0] = 0
        if AC_T == 0 :
            AC = i
    else :
        x44.append(i)
        y44.append(root[0]*B+A*i)

#第一个零点
First_Zero = 0
for k in range( len(x) ):
    Difference_y = math.fabs( y2[k] - line1[k] )
    if Difference_y <  0.01 :
        Zero = [ k*Delta_x+start , y2[k] ]
        Zeros.append( Zero )
        Zeros_Z.append( k )
        First_Zero = k*Delta_x+start
        break

#后两个零点
Zero_x = First_Zero
for k in range( len(x) ):
    Difference_y = math.fabs( y2[k] - line1[k] )
    Difference_x = math.fabs( k*Delta_x+start - Zero_x )
    if Difference_y <  0.01 and Difference_x > 0.05 :
        Zero_x = k*Delta_x+start
        Zero = [ k*Delta_x+start , y2[k] ]
        Zeros.append( Zero )
        Zeros_Z.append( k )

S1 = 0
S2 = 0
X1 = []
Y1 = []
L1 = []
X2 = []
Y2 = []
L2 = []
for k in range( len(x) ):
    if k > Zeros_Z[0] and k <= Zeros_Z[1] :
        S1 += (y2[k]-line1[k])*Delta_x
        X1.append( k*Delta_x+start )
        Y1.append( y2[k] )
        L1.append(H)
    if k > Zeros_Z[1] and k <= Zeros_Z[2] :
        S2 += (y2[k]-line1[k])*Delta_x
        X2.append( k*Delta_x+start )
        Y2.append( y2[k] )
        L2.append(H)

print( AC )
print( Zeros )
print( Zeros[0] )
print( Zeros[0][0] )

print( Zeros_Z )
print( Zeros_Z[0] )
print(Zeros)
print( S1 )
print( S2 )
str1 = '面积差比 = ' + str( (S1 + S2) / S1 ) 
str2 = '吸收态相变密度 = ' + str( AC )
str3 = '气相-液相密度 = (' + str( Zeros[0][0] ) + ', ' + str( Zeros[2][0] ) + ')'
print( str1 )
print( str2 )
print( str3 )


plt.fill_between( X1, L1, Y1, facecolor='lightgrey' )
plt.fill_between( X2, Y2, L2, facecolor='lightgrey' )


plt.plot(x22, y22, color='red', label='$\Omega=15\epsilon$',linewidth=3)
plt.plot(x33, y33, color='green', label='$\Omega=10\epsilon$',linewidth=3)
plt.plot(x44, y44, color='blue', label='$\Omega=5\epsilon$',linewidth=3)
# plt.plot(x, line1, color='black')
plt.plot(X1, L1, color='black',linestyle='--',linewidth=3)
plt.plot(X2, L2, color='black',linestyle='--',linewidth=3)

# plt.scatter(Zeros[0][0],Zeros[0][1])
# plt.scatter(Zeros[1][0],Zeros[1][1])
# plt.scatter(Zeros[2][0],Zeros[2][1])

ax = plt.gca()
axes = plt.subplot()
axes.minorticks_on()
plt.xticks([0.5, 1.0, 1.5, 2.0])
plt.tick_params(labelsize=20)
# axes.tick_params(axis="both", which="major", direction="in", width=1, length=5)
# axes.tick_params(axis="both", which="minor", direction="in", width=1, length=3)
# axes.xaxis.set_minor_locator(MultipleLocator(0.4))


# plt.grid(True, which="major", linestyle="--", color="gray", linewidth=0.75)
# plt.grid(True, which="minor", linestyle=":", color="lightgray", linewidth=0.75)


plt.xlabel("$\phi_0$", fontdict={'size': 25}) #title of abscissa
plt.ylabel("$\mu_b/\epsilon$", fontdict={'size': 25}) #title of ordinate

plt.legend(loc='best', ncol=1,fontsize=15)
plt.tight_layout()

plt.savefig('./Fig2c.png', dpi=300)
plt.close()

str = 's0='+str(s0)+',s1='+str(s1)+',s2='+str(s2)+',s3='+str(s3)+',s4='+str(s4)+',s5='+str(s5)+',Tss='+str(Tss)+',D_phi=1,D_T='+str(A)

print(str)

# plot_fig()


