import sys 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle 
from matplotlib.pyplot import MultipleLocator
  

plt.figure(figsize=(6,5))
# plt.xlim( 0, 1.5 )
# plt.ylim( -0.5, 0.5 )
plt.xlim( 0, 0.2 )
plt.ylim( -0.2, 0.2 )
  
# Grid of x, y points 
nx, ny = 100, 100
x = np.linspace( 0, 0.2, nx ) 
y = np.linspace( -0.2, 0.2, ny ) 
X, Y = np.meshgrid(x, y) 

epsilon = 0.1
epsilon_plus = epsilon + 2
u = X * ( epsilon - 1.5 * X / ( Y + 1 ) / ( Y + 1) )
v = 2 * Y + 0.5 * X / ( 1 + Y )
  
# Plotting the streamlines with  
# proper color and arrow 
ax = plt.gca()
# color = 2 * np.log(np.hypot(Ex, Ey)) 

ax.streamplot(x, y, u, v,  
              linewidth = 1, cmap = plt.cm.inferno, color = 'royalblue',
              density = 1.5, arrowstyle ='->',  
              arrowsize = 1.5, zorder = 1) 

plt.scatter( 0, 0, s = 50, c = 'black', zorder = 3, label = 'G' )
plt.scatter( 2 * epsilon / 3, - epsilon / 6, s = 50, c = 'red', zorder = 3, label = '$P_2$' )
# plt.scatter( 2 * epsilon_plus / 3, - epsilon_plus / 6, s = 50, c = 'red', zorder = 3, label = '$P_2$' )
# plt.scatter( 2 * epsilon / 3, - epsilon / 6, s = 50, c = 'blue', zorder = 3, label = '$WF$' )

# plt.plot( y*0 + 2 * epsilon / 3, y, color = 'red', linewidth = 3, zorder = 2, alpha = 0.5 )
# plt.plot( x, - x / 4, color = 'red', linewidth = 3, zorder = 2, alpha = 0.5 )

plt.plot( y*0 + 2 * epsilon / 3, y, color = 'red', linewidth = 3, zorder = 2, alpha = 0.5 )
plt.plot( x, - x / 4, color = 'red', linewidth = 3, zorder = 2, alpha = 0.5 )


x_major_locator=MultipleLocator(0.02)
ax = plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
plt.tick_params(labelsize=15)
ax.tick_params(top=True,labeltop=True,labelright=True)

# plt.xlabel("$\sigma$", fontdict={'size': 16})
# plt.ylabel("$P(x>x_c)$", fontdict={'size': 16}) 

# plt.xlabel("$u$", fontdict={'size': 16})
# plt.ylabel("$T-T_{C0}$", fontdict={'size': 16}) #title of ordinate

plt.xlabel("$\\bar{u}$", fontdict={'size': 16})
plt.ylabel("$\\bar{r}$", fontdict={'size': 16}) #title of ordinate

plt.legend(loc='upper right', ncol=1)
plt.tight_layout()
# ax.set_aspect('equal')
plt.savefig('./FigS4.png', dpi=300,)
plt.close()
