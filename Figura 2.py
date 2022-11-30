# -*- coding: utf-8 -*-
"""
@author: Jhonatan
"""
import matplotlib.pyplot as plt
import numpy as np
#%%
'ONDÍCULA RICKER'
def ricker(f, length = 0.100, dt = 0.001):
    t = np.arange(-length/2, (length-dt)/2, dt)
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y
t0,w = ricker(20)

#%%
fig, (ax1,ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8,4), 
      gridspec_kw = {'width_ratios':[1,1]})
      #subplot_kw = {'xticks':[], 'yticks':[]})
ax1.plot([0,.5,1],[1,.3,1],c='black')
ax1.plot([0,1],[0.3,0.3],c='brown')
ax1.plot([0.5,0.5],[1,0],'--',c='grey')
#%%
ax1.annotate('Onda\nIncidente', xy=(0.15, 0.8), xytext=(0.2, 0.9), fontweight='bold',
            arrowprops=dict(facecolor='black', shrink=0.05))
ax1.annotate('Onda\nReflejada', xy=(.85, 0.8), xytext=(0.55, 0.9), fontweight='bold',
            arrowprops=dict(facecolor='black', shrink=0.05))
ax1.annotate(r'$C R=+0.2$', xy=(0.1, 0.4), xytext=(0.04, 0.33))
ax1.annotate(r'$(\rho_1<\rho_2\ &\ V_1<V_2)$', xy=(0.1, 0.2), xytext=(0.04, 0.2))
ax1.annotate(r'$Z_1 = \rho_1\ \ V_1$', xy=(0.1, 0.2), xytext=(0.7, 0.33))
ax1.annotate(r'$Z_2 = \rho_2\ \ V_2$', xy=(0.1, 0.2), xytext=(0.7, 0.23))
#
left, bottom, width, height = [0.15, 0.45, 0.03, 0.3]
ax11 = fig.add_axes([left, bottom, width, height])
#mini ondicula 1
y = [0,0,0,0,0,0,0,0.30980,0,0,0,0,0,0,0]
tiempo = [.01,.02,.03,.04,.05,.06,.07,.08,.09,.1,.11,.12,.13,.14,.15]
synthetic = np.convolve(w, y, mode='same')
ax11.plot(synthetic, t0, lw=2)
ax11.fill_betweenx(t0, synthetic, 0, where=(synthetic>0), color = 'red')
ax11.fill_betweenx(t0, synthetic, 0, where=(synthetic<0), color = 'blue')
ax11.patch.set_alpha(0)
ax11.axis('off')
ax11.set_xticklabels('')
ax11.set_yticklabels('')
#
left, bottom, width, height = [0.425, 0.45, 0.03, 0.3]
ax12 = fig.add_axes([left, bottom, width, height])
#mini ondicula 2
y = [0,0,0,0,0,0,0,-0.30980,0,0,0,0,0,0,0]
tiempo = [.01,.02,.03,.04,.05,.06,.07,.08,.09,.1,.11,.12,.13,.14,.15]
synthetic = np.convolve(w, y, mode='same')
ax12.plot(synthetic, t0, lw=2)
ax12.fill_betweenx(t0, synthetic, 0, where=(synthetic>0), color = 'blue')
ax12.fill_betweenx(t0, synthetic, 0, where=(synthetic<0), color = 'red')
ax12.patch.set_alpha(0)
ax12.axis('off')
ax12.set_xticklabels('')
ax12.set_yticklabels('')
#
ax1.set_xlim(0,1)
ax1.set_ylim(0,1)
ax1.set_yticklabels('')
ax1.set_xticklabels('')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.text(.038, .046, 'a)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})

#%%
ax2.plot([0,.5,1],[1,.3,1],c='black')
ax2.plot([0,1],[0.3,0.3],c='brown')
ax2.plot([0.5,0.5],[1,0],'--',c='grey')
#%%
ax2.annotate('Onda\nIncidente', xy=(0.15, 0.8), xytext=(0.2, 0.9), fontweight='bold',
            arrowprops=dict(facecolor='black', shrink=0.05))
ax2.annotate('Onda\nReflejada', xy=(.85, 0.8), xytext=(0.55, 0.9), fontweight='bold',
            arrowprops=dict(facecolor='black', shrink=0.05))
ax2.annotate(r'$CR=-0.2$', xy=(0.1, 0.4), xytext=(0.04, 0.33))
ax2.annotate(r'$(\rho_1>\rho_2\ &\ V_1>V_2)$', xy=(0.1, 0.2), xytext=(0.04, 0.2))
ax2.annotate(r'$Z_1 = \rho_1\ \ V_1$', xy=(0.1, 0.2), xytext=(0.7, 0.33))
ax2.annotate(r'$Z_2 = \rho_2\ \ V_2$', xy=(0.1, 0.2), xytext=(0.7, 0.23))
#
left, bottom, width, height = [0.575, 0.45, 0.03, 0.3]
ax21 = fig.add_axes([left, bottom, width, height])
#mini ondicula 1
y = [0,0,0,0,0,0,0,0.30980,0,0,0,0,0,0,0]
tiempo = [.01,.02,.03,.04,.05,.06,.07,.08,.09,.1,.11,.12,.13,.14,.15]
synthetic = np.convolve(w, y, mode='same')
ax21.plot(synthetic, t0, lw=2)
ax21.fill_betweenx(t0, synthetic, 0, where=(synthetic>0), color = 'red')
ax21.fill_betweenx(t0, synthetic, 0, where=(synthetic<0), color = 'blue')
ax21.patch.set_alpha(0)
ax21.axis('off')
ax21.set_xticklabels('')
ax21.set_yticklabels('')
#
left, bottom, width, height = [0.85, 0.45, 0.03, 0.3]
ax22 = fig.add_axes([left, bottom, width, height])
#mini ondicula 2
y = [0,0,0,0,0,0,0,0.30980,0,0,0,0,0,0,0]
tiempo = [.01,.02,.03,.04,.05,.06,.07,.08,.09,.1,.11,.12,.13,.14,.15]
synthetic = np.convolve(w, y, mode='same')
ax22.plot(synthetic, t0, lw=2)
ax22.fill_betweenx(t0, synthetic, 0, where=(synthetic>0), color = 'blue')
ax22.fill_betweenx(t0, synthetic, 0, where=(synthetic<0), color = 'red')
ax22.patch.set_alpha(0)
ax22.axis('off')
ax22.set_xticklabels('')
ax22.set_yticklabels('')
#
ax2.set_xlim(0,1)
ax2.set_ylim(0,1)
ax2.set_yticklabels('')
ax2.set_xticklabels('')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.text(.034, .046, 'b)', fontsize = 12, style='italic', 
             fontweight = 'bold',
             bbox={'facecolor': 'white', 'alpha': 1, 'pad': 7})

fig.savefig('Figura 2.png',bbox_inches="tight", dpi=1200)