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
from matplotlib.pyplot import MultipleLocator

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

color_b = (100/255,200/255,1)
color_r = (1,103/255,102/255)
color_g = (128/255,1,155/255)
# color_g = (128/255,1,152/255)

Q = 1.0
K = 1.2



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

def plot(path,color,label,size):
    scaling = 1.4
    ava_dim = 2

    if ( os.path.exists(path) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=",")

        data_x = []
        data_y = []
        FF = 0
        for i in range(len(data2)):
            #if (data2[i][1] != 0 and i > count - 5):
            if (data2[i][2] > -100):
                data_x.append( K*math.sqrt(data2[i][0]) )
                data_y.append( data2[i][2]/Q )
            else :
                FF += 1

                #data_x.append(int(data2[i][0]) * pow(int(label),-0.5 * ava_dim))
                #data_y.append(data2[i][1] / num / data2[i][2] * pow(int(data2[i][0]),scaling))
        for i in range(len(data2)):
            #if (data2[i][1] != 0 and i > count - 5):
            if (data2[i][2] > -100):

                data_x.append( K*math.sqrt(data2[len(data2)-i-1-FF][0]) )
                data_y.append( data2[len(data2)-i-1-FF][3]/Q )

        plt.plot(data_y, data_x, c=color,linewidth=3,marker = '.',markerfacecolor='none',markeredgecolor='black',markeredgewidth=5)
        # plt.scatter(data_x, data_y, c=color, s=15)
        #plt.plot(data_x, data_y, c=color)

def plot2(path,color,label,size):
    scaling = 1.4
    ava_dim = 2

    if ( os.path.exists(path) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=",")

        data_x = []
        data_y = []
        for i in range(len(data2)):
            #if (data2[i][1] != 0 and i > count - 5):
            if (data2[i][1] > -100):

                data_x.append( K*math.sqrt(data2[i][0]) )
                data_y.append( data2[i][1]/Q )

                #data_x.append(int(data2[i][0]) * pow(int(label),-0.5 * ava_dim))
                #data_y.append(data2[i][1] / num / data2[i][2] * pow(int(data2[i][0]),scaling))

        plt.plot(data_y, data_x, c=color,linewidth=3,marker = '.',markerfacecolor='none',markeredgecolor='black',markeredgewidth=5)
        # plt.scatter(data_x, data_y, c=color, s=15)
        #plt.plot(data_x, data_y, c=color)

def fill(path,color):
    scaling = 1.4
    ava_dim = 2

    if ( os.path.exists(path) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=",")

        data_x = []
        data_y = []

        data_x.append( 100 )
        data_y.append( 0.01 )

        for i in range(len(data2)):
            if (data2[i][1] > -100):

                data_x.append( K*math.sqrt(data2[i][0]) )
                data_y.append( data2[i][1]/Q )

        plt.fill_between( data_y, 0, data_x, facecolor=color )

def fill2(path,color):
    scaling = 1.4
    ava_dim = 2

    if ( os.path.exists(path) ) :
        file_path = path
        with open(file_path, 'r') as f:
            data2 = np.loadtxt(f, delimiter=",")

        data_x = []
        data_y = []
        FF = 0
        for i in range(len(data2)):
            #if (data2[i][1] != 0 and i > count - 5):
            if (data2[i][2] > -100):
                data_x.append( K*math.sqrt(data2[i][0]) )
                data_y.append( data2[i][2]/Q )
            else :
                FF += 1

                #data_x.append(int(data2[i][0]) * pow(int(label),-0.5 * ava_dim))
                #data_y.append(data2[i][1] / num / data2[i][2] * pow(int(data2[i][0]),scaling))
        for i in range(len(data2)):
            #if (data2[i][1] != 0 and i > count - 5):
            if (data2[i][2] > -100):

                data_x.append( K*math.sqrt(data2[len(data2)-i-1-FF][0]) )
                data_y.append( data2[len(data2)-i-1-FF][3]/Q )

        plt.fill_between( data_y, data_x, 100, facecolor=color )
#--------------------------------------------------------------------
#---------------------------------------



plt.figure(figsize=(5,5))

plt.xscale('linear')
plt.yscale('linear')
# plt.xscale('log')
#plt.yscale('log')
plt.minorticks_on()

plt.xlim(0.01, 1.1547)
plt.ylim(5.4, 13.45)

x = [0.01, 10]
y = [25, 25.0]
# plt.fill_between(x, y, 0.05, facecolor='lightcoral' )
plt.fill_between(x, y, 0.05, facecolor=color_r )

plot2('./curve.csv', 'black', 1, 1)
# fill('./curve.csv', 'lightblue')
fill('./curve.csv', color_b)
# plot('./ab.csv', 'black', 1, 1)
# fill('./ab.csv', 'lightblue')

plot('./curve.csv', 'black', 1, 1)
# fill2('./curve.csv', 'lightgreen')
fill2('./curve.csv', color_g)
# fill('./curve.csv', 'lightgreen')

# x_major_locator=MultipleLocator(0.02)
ax = plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
plt.xticks([0.4, 0.8])
plt.tick_params(labelsize=20)
# ax.tick_params(top=True)

plt.xlabel("$\phi_0$", fontdict={'size': 25})
plt.ylabel("$\Omega/\epsilon$", fontdict={'size': 25}) #title of ordinate

# plt.legend(loc='best', ncol=1)
plt.tight_layout()

plt.savefig('./Fig2d.png', dpi=500,)
plt.close()
