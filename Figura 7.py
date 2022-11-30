# -*- coding: utf-8 -*-
"""
@author: Jhonatan
"""
#%%
'IMPORTAR LIBRERÍAS'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
#%%
'DEFINIR FUNCIÓN RIKER'
def ricker(f, length = 0.512, dt = 0.001):
    t = np.arange(-length/2, (length-dt)/2, dt)
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y
#%%
'DEFINIR FUNCIÓN FRECUENCIA MEDIA'
V = np.arange(0,100,1)
def VM(M):
    F = (2/np.sqrt(np.pi))*((V**2)/(M**3))*np.exp((-V**2)/(M**2))
    return F
#%%
'ELEMENTOS DE LA ONDÍCULA RICKER'
TD = np.sqrt(6)/(np.pi*5)
TR = TD/np.sqrt(3)
#%%
'GRÁFICA FINAL'
fig = plt.figure(figsize=(7, 10))
gs = GridSpec(nrows=5, ncols=2)
fig.subplots_adjust(wspace=0)

ax0 = fig.add_subplot(gs[:-3, :])

t, y = ricker(5)
ax0.plot(t, y, lw=2, color='black', alpha=0.5)
ax0.fill_between(t, y, 0,  y > 0.0, color='blue', alpha = 0.5)
ax0.fill_between(t, y, 0, y < 0.0, color='red', alpha = 0.5)
ax0.set_title('Geometría de la Ondícula Ricker', fontsize = 16)
#Elementos geométricos
ax0.plot([TD/2,TD/2],[min(y),1.2],'--',color='k',alpha=0.6)
ax0.plot([-TD/2,-TD/2],[min(y),1.2],'--',color='k',alpha=0.6)
ax0.annotate('', xy=(TD/2,1.2), xytext=(-TD/2,1.2),
            arrowprops={'arrowstyle': '<->'}, va='top')
ax0.annotate(r'$T_D$', xy=(0,1.2), xytext=(-0.005,1.2), va='bottom')
ax0.plot([TR/2,TR/2],[0,-1],'--',color='k',alpha=0.6)
ax0.plot([-TR/2,-TR/2],[0,-1],'--',color='k',alpha=0.6)
ax0.annotate('', xy=(TR/2,-0.6), xytext=(-TR/2,-0.6),
            arrowprops={'arrowstyle': '<->'}, va='top')
ax0.annotate(r'$T_R$', xy=(0,-0.6), xytext=(-0.005,-0.6), va='bottom')
#
ax0.set_ylabel('Amplitud', fontsize = 14)
ax0.set_xlabel('Tiempo de viaje doble [TWT] (s)', fontsize = 14)
ax0.set_ylim((-1.1,1.4))
ax0.set_xlim((min(t),max(t)))
ax0.text(-0.25, 1.23, 'a)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 7})
ax0.grid()

t,y = ricker(5)
ax1 = fig.add_subplot(gs[2, 0])
ax1.plot(t, y, lw=2, color='black', alpha=0.5)
ax1.fill_between(t, y, 0,  y > 0.0, color='blue', alpha = 0.5)
ax1.fill_between(t, y, 0, y < 0.0, color='red', alpha = 0.5)
ax1.set_title('Ondícula Ricker: 5 Hz', style = 'normal')
ax1.set_xticklabels('')
ax1.text(-0.27, 0.8, 'b1)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})
ax1.set_xticks([])
ax1.grid()
#
F=VM(5)
ax2 = fig.add_subplot(gs[2, 1])
ax2.plot(V,F,lw=2)
ax2.plot([5,5],[0,max(F)],'--',color='r')
ax2.set_title(r'$V_M = 5 Hz$', style = 'normal')
ax2.set_yticklabels('')
ax2.set_xticks([5,25,50,75,100])
ax2.text(90, 0.07, 'b2)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})
ax2.set_yticks([])
ax2.grid()

t,y = ricker(20)
ax3 = fig.add_subplot(gs[3, 0])
ax3.plot(t, y, lw=2, color='black', alpha=0.5)
ax3.fill_between(t, y, 0,  y > 0.0, color='blue', alpha = 0.5)
ax3.fill_between(t, y, 0, y < 0.0, color='red', alpha = 0.5)
ax3.set_title('Ondícula Ricker: 20 Hz', style = 'normal')
ax3.set_xticklabels('')
ax3.text(-0.27, 0.8, 'c1)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})
ax3.set_xticks([])
ax3.grid()
#
F=VM(20)
ax4 = fig.add_subplot(gs[3, 1])
ax4.plot(V,F, lw=2)
ax4.plot([20,20],[0,max(F)],'--',color='r')
ax4.set_title(r'$V_M = 20 Hz$', style = 'normal')
ax4.set_yticklabels('')
ax4.set_xticks(np.arange(0,100,10))
ax4.text(90, 0.0175, 'c2)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})
ax4.set_yticks([])
ax4.grid()

t,y = ricker(40)
ax5 = fig.add_subplot(gs[4, 0])
ax5.plot(t, y, lw=2, color='black', alpha=0.5)
ax5.fill_between(t, y, 0,  y > 0.0, color='blue', alpha = 0.5)
ax5.fill_between(t, y, 0, y < 0.0, color='red', alpha = 0.5)
ax5.set_title('Ondícula Ricker: 40 Hz', style = 'normal')
ax5.set_xticklabels('')
ax5.set_xticks([])
ax5.text(-0.27, 0.8, 'd1)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})
ax5.grid()
#
F=VM(40)
ax6 = fig.add_subplot(gs[4, 1])
ax6.plot(V,F,lw=2)
ax6.plot([40,40],[0,max(F)],'--',color='r')
ax6.set_title(r'$V_M = 40 Hz$', style = 'normal')
ax6.set_yticklabels('')
ax6.set_yticks([])
ax6.set_xticks(np.arange(0,100,10))
ax6.text(90, 0.009, 'd2)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})
ax6.grid()

plt.tight_layout(pad=0.4,h_pad=0.3)
fig.savefig('Figura 7.png',bbox_inches="tight", dpi=1200)