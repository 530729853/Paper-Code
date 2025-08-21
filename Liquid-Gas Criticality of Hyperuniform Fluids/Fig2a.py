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
Gamma_t = 1.0
size1 = 10
size2 = 20
A = 1
Fac = 4.0
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color ="#"+''.join([random.choice(colorArr) for i in range(6)])
    return color

def fit(data_x,cut):
    lenth = int( len(data_x)/cut)
    m = 0
    x_bar = 0
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0
    for i in range(lenth):
        x = data_x[i][0]
        if(x > 0):
            x_bar = x + x_bar
            m = m + 1
    x_bar = x_bar / m

    for i in range(lenth):
        x = data_x[i][0]
        y = data_x[i][1]
        if (x > 0):
            sum_yx += y * (x - x_bar)
            sum_x2 += x ** 2

    w = sum_yx / (sum_x2 - m * (x_bar ** 2))

    for i in range(m):
        x = data_x[i][0]
        y = data_x[i][1]
        sum_delta += (y - w * x)
    b = sum_delta / m
    return w, b

def plot(path, path2):
    if ( os.path.exists(path) and os.path.exists(path2) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=" ")

        file_path2 = path2
        with open(file_path2, 'r') as f:
            data4 = np.loadtxt(f, delimiter=" ")

        Et = 0
        count0 = 0
        for i in range(len(data4)):
            if (data4[i][0] > -1):
                Et += data4[i][1]
                count0 += 1

        N = data2[0][3]
        phi = data2[0][1]
        Tt = Et/count0/N
        Bar_Z = 0
        count = 0
        for i in range(len(data2)):
            if (data2[i][0] > 50000):
                Bar_Z += data2[i][4]
                count += 1
        STR = [ phi, Tt, Bar_Z/count/N ]
        F = open( 'bar_Z.txt', 'a' )
        print( STR[0], file = F, end = ' ' )
        print( STR[1], file = F, end = ' ' )
        print( STR[2], file = F )
        F.close()

def plot_F(path):
    scaling = 1.4
    ava_dim = 2

    if ( os.path.exists(path) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=" ")
        data_x0 = []
        data_x1 = []
        data_y1 = []
        data_y2 = []
        data_y3 = []
        data_y4 = []
        for i in range(len(data2)):
            x = data2[i][0]*math.sqrt(data2[i][1])
            xx = math.sqrt(data2[i][1])
            data_x1.append( x )
            if i <= 10 or i == len(data2) - 1 :
                if i % 5 == 0 or i == len(data2) - 1 :
                    data_x0.append( x ) #( 1 - math.exp(-x) ) * x
                    data_y1.append( data2[i][2]/0.002 )
            elif i % 20 == 0 :
                data_x0.append( x ) #( 1 - math.exp(-x) ) * x
                data_y1.append( data2[i][2]/0.002 )
            if Gamma_t > 0 :
                data_y2.append( 3.545*( 1 - math.exp(-Fac*math.sqrt(2*math.pi)*x/Gamma_t) ) * x )
            data_y3.append( 4*( 1 - math.exp(-x) ) * x + 0.172 )
            # data_y4.append( 10*( 1 - math.exp(-x) ) * x )

        plt.plot(data_x0, data_y1, c=color1,label='Fix $\phi_0$',linewidth=5,marker = 'o',markerfacecolor='none',markeredgecolor=color1,ms=12,markeredgewidth=3)
        # plt.scatter(data_x0, data_y1, c=color1, s=50)
        if Gamma_t > 0 :
            plt.plot(data_x1 , data_y2 ,c='black', label="Theory", linestyle='--',linewidth=3)
        
        # plt.plot(data_x1 , data_y3 ,c='black', label="$theory+ 0.172$", linestyle='-.',linewidth=1.5)
        # plt.plot(data_x1 , data_y4 ,c='black', label="$theory$", linestyle='-',linewidth=1.5)


def plot_F2(path):
    scaling = 1.4
    ava_dim = 2

    if ( os.path.exists(path) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=" ")
        data_x0 = []
        data_x1 = []
        data_y1 = []
        data_y2 = []
        data_y3 = []
        data_y4 = []
        for i in range(len(data2)):
            x = data2[i][0]*math.sqrt(data2[i][1])
            xx = math.sqrt(data2[i][1])
            data_x1.append( x )

            data_x0.append( x ) #( 1 - math.exp(-x) ) * x
            data_y1.append( data2[i][2]/0.002 )
            
            if Gamma_t > 0 :
                data_y2.append( 3.545*( 1 - math.exp(-Fac*math.sqrt(2*math.pi)*x/Gamma_t) ) * x )
            data_y3.append( 4*( 1 - math.exp(-x) ) * x + 0.172 )
            # data_y4.append( 10*( 1 - math.exp(-x) ) * x )

        plt.plot(data_x0, data_y1, c=color2,label='Fix $\Omega$',linewidth=5,marker = 'o',markerfacecolor='none',markeredgecolor=color2,markeredgewidth=7)
        # plt.scatter(data_x0, data_y1, c=color1, s=50)
        # if Gamma_t > 0 :
            # plt.plot(data_x1 , data_y2 ,c='black', label="theory", linestyle='--',linewidth=3)
        
        # plt.plot(data_x1 , data_y3 ,c='black', label="$theory+ 0.172$", linestyle='-.',linewidth=1.5)
        # plt.plot(data_x1 , data_y4 ,c='black', label="$theory$", linestyle='-',linewidth=1.5)
#--------------------------------------------------------------------

NON = []

# plt.xlim(0,1)
# plt.ylim(0,2.2)
plt.figure(figsize=(5,5.2))

# if ( os.path.exists('bar_Z.txt') ) :
#  	os.remove( 'bar_Z.txt' )

# for i in range(200):
# 	plot( './pro'+str(i+1)+'/Z.dat', './pro'+str(i+1)+'/Energy.dat' )

plot_F2('bar_Z_A.txt')
plot_F('bar_Z.txt') 


PHI = 0
if ( os.path.exists('bar_Z.txt') ) :
	file_path = 'bar_Z.txt'
	with open(file_path, 'r') as f:
    		dataX = np.loadtxt(f, delimiter=" ")
	PHI = dataX[0][0]

K=4
temp_x = np.arange(0.0, 0.85, 0.001)
temp_y = []
temp_y2 = []
for i in range(len(temp_x)):
	temp_y.append( temp_x[i]*K*PHI )
# plt.plot(temp_x , temp_y ,c='b', label="$y=4x$", linestyle='--',linewidth=1.5)
for i in range(len(temp_x)):
	temp_y2.append( (temp_x[i])*2.0*math.sqrt(math.pi) )
# plt.plot(temp_x , temp_y2 ,c='b', label="$Z=2\sqrt{\pi}\phi T_t^{1/2}$", linestyle='-.',linewidth=1.5)

ax = plt.gca()
axes = plt.subplot()
axes.minorticks_on()
plt.tick_params(labelsize=20)
plt.xticks([0.2, 0.4, 0.6, 0.8])
plt.yticks([1, 2, 3])
# ax.tick_params(top=True,labeltop=True,labelright=True,labelsize=20)

plt.xlabel("$\phi_0 T_{t0}^{1/2}/\epsilon^{1/2}$", fontdict={'size': 25}) #title of abscissa
plt.ylabel("$Z$", fontdict={'size': 25}) #title of ordinate

plt.legend(loc='best', ncol=1,fontsize=15)
plt.tight_layout()

plt.savefig('./Fig2a.png', dpi=300,)
plt.close()

#####################################

