# -*- coding: utf-8 -*-
"""
@author: Jhonatan
"""
#%%
'IMPORTAR LIBRERÍAS'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
#%%
#Diccionario de litologías
litología_números = {30000: {'lith':'Sandstone', 'lith_num':1, 'hatch': '..', 'color':'#ffff00'},
                 65030: {'lith':'Sandstone/Shale', 'lith_num':2, 'hatch':'-.', 'color':'#ffe119'},
                 65000: {'lith':'Shale', 'lith_num':3, 'hatch':'--', 'color':'#bebebe'},
                 80000: {'lith':'Marl', 'lith_num':4, 'hatch':'', 'color':'#7cfc00'},
                 74000: {'lith':'Dolomite', 'lith_num':5, 'hatch':'-/', 'color':'#8080ff'},
                 70000: {'lith':'Limestone', 'lith_num':6, 'hatch':'+', 'color':'#80ffff'},
                 70032: {'lith':'Chalk', 'lith_num':7, 'hatch':'..', 'color':'#80ffff'},
                 88000: {'lith':'Halite', 'lith_num':8, 'hatch':'x', 'color':'#7ddfbe'},
                 86000: {'lith':'Anhydrite', 'lith_num':9, 'hatch':'', 'color':'#ff80ff'},
                 99000: {'lith':'Tuff', 'lith_num':10, 'hatch':'||', 'color':'#ff8c00'},
                 90000: {'lith':'Coal', 'lith_num':11, 'hatch':'', 'color':'black'},
                 93000: {'lith':'Basement', 'lith_num':12, 'hatch':'-|', 'color':'#ef138a'}}

df_lito = pd.DataFrame.from_dict(litología_números, orient='index')
df_lito.index.name = 'LITOLOGÍA'
#%%
'CREAR PERFIL LITOLÓGICO'
size_tr = 100
nx_tr, ny_tr = ([size_tr]*2)
nxy_tr = nx_tr * ny_tr
x = np.linspace(0, nx_tr-1, nx_tr)
y = np.linspace(0, ny_tr-1, ny_tr)
xy = np.reshape(np.array([np.meshgrid(x, y, indexing='ij')]), [2,nxy_tr]).T
idx_refl = [49]
refl = np.zeros(ny_tr)
for i in idx_refl:
    refl[i] = 0.30980
refl = np.tile(refl, [25,1])
#%%
'GRÁFICA FINAL'
fig, ax = plt.subplots(1, 3, sharey=False, figsize = (10,5),
                        gridspec_kw={'width_ratios': [0.3,1,1]})
fig.subplots_adjust(wspace=0.1)
#%%
ax[0].imshow(np.reshape(refl,[25,100]).T,cmap=plt.cm.gray_r)
ax[0].set_xticklabels('')
ax[0].set_yticklabels('')
ax[0].set_xlabel('')
ax[0].set_xlim(0,25)
ax[0].set_ylim(0,100)
ax[0].invert_yaxis()
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].plot([6,20],[49,49],color='red',lw=3)
ax[0].plot([6,6],[0,49],color='red',lw=3)
ax[0].plot([20,20],[49,100],color='red',lw=3)
ax[0].fill_betweenx([0,49],0,25,
                 facecolor=litología_números[65000]['color'],
                 hatch=litología_números[65000]['hatch'], alpha = 0.7)
ax[0].fill_betweenx([50,99],0,25,
                 facecolor=litología_números[30000]['color'],
                 hatch=litología_números[30000]['hatch'], alpha = 0.7)
ax[0].annotate('Incremento\nde IA', xy=(15,47), xytext=(32,30),
  color = 'red', fontweight = 'bold', fontsize=12,
  arrowprops={'arrowstyle': '-|>','ec':'r','lw':3},va='center')
ax[0].set_title('Ejemplo\nLitología', fontweight='bold')

#%%
'ONDÍCULA RICKER'
def ricker(f, length = 0.100, dt = 0.001):
    t = np.arange(-length/2, (length-dt)/2, dt)
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y
t0,y = ricker(40)
tiempo = np.arange(0,100,1)
#%%
traza = refl[4]
synthetic = np.convolve(y, traza, mode='same')
ax[1].plot(synthetic,tiempo,lw=2)
ax[1].plot([-0.35,50],[50,0.35],lw=4,c='brown')
ax[1].set_ylim(100,0)
ax[1].set_xlim(-0.35,0.35)
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[1].set_title('SEG: Polaridad Estándar Positiva\nConvención Americana', fontweight='bold')
ax[1].fill_betweenx(tiempo, synthetic, 0, where=(synthetic > 0),color='blue',alpha = 0.8)
ax[1].fill_betweenx(tiempo, synthetic, 0, where=(synthetic < 0.0), color='red', alpha = 0.8)
ax[1].set_xticklabels('')
ax[1].set_yticklabels('')
ax[1].annotate('Interfaz\nEstratigráfica', xy=(0.25,49), xytext=(0.42,30),
  color = 'brown', fontweight = 'bold', fontsize=12,
  arrowprops={'arrowstyle': '-|>','ec':'brown','lw':3},va='center')
ax[1].annotate('-', xy=(0,0), xytext=(-.05,10),
  color = 'red', fontweight = 'bold', fontsize=30)
ax[1].annotate('+', xy=(0,0), xytext=(.01,8),
  color = 'blue', fontweight = 'bold', fontsize=18)
ax[1].patch.set_alpha(0)
ax[1].text(-0.33, 96.4, 'b)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 7})
#%%
size_tr = 100
nx_tr, ny_tr = ([size_tr]*2)
nxy_tr = nx_tr * ny_tr
x = np.linspace(0, nx_tr-1, nx_tr)
y = np.linspace(0, ny_tr-1, ny_tr)
xy = np.reshape(np.array([np.meshgrid(x, y, indexing='ij')]), [2,nxy_tr]).T
idx_refl = [49]
refl = np.zeros(ny_tr)
for i in idx_refl:
    refl[i] = -0.30980
refl = np.tile(refl, [25,1])
t0,y = ricker(40)
tiempo = np.arange(0,100,1)
#%%
traza = refl[4]
synthetic = np.convolve(y, traza, mode='same')
ax[2].plot(synthetic,tiempo,lw=2)
ax[2].plot([-0.35,50],[50,0.35],lw=4,c='brown')
ax[2].set_ylim(100,0)
ax[2].set_xlim(-0.35,0.35)
ax[2].set_xticks([])
ax[2].set_yticks([])
ax[2].set_title('SEG: Polaridad Estándar Negativa\nConvención Europea', fontweight='bold')
ax[2].fill_betweenx(tiempo, synthetic, 0, where=(synthetic > 0),color='blue',alpha = 0.8)
ax[2].fill_betweenx(tiempo, synthetic, 0, where=(synthetic < 0.0), color='red', alpha = 0.8)
ax[2].set_xticklabels('')
ax[2].set_yticklabels('')
ax[2].annotate('', xy=(0.25,49), xytext=(-.09,36),
  color = 'brown', fontweight = 'bold', fontsize=12,
  arrowprops={'arrowstyle': '-|>','ec':'brown','lw':3},va='center')
ax[2].annotate('-', xy=(0,0), xytext=(-.05,10),
  color = 'red', fontweight = 'bold', fontsize=30)
ax[2].annotate('+', xy=(0,0), xytext=(.01,8),
  color = 'blue', fontweight = 'bold', fontsize=18)
ax[2].patch.set_alpha(0)
ax[2].text(-0.33, 96.4, 'b)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 7})

fig.savefig('Figura 8.png',bbox_inches="tight", dpi=1200)