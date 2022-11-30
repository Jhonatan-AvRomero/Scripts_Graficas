# -*- coding: utf-8 -*-
"""
@author: Jhonatan
"""
#%%
"IMPORTAR LIBRERÍAS"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
"LEER REGISTROS"
Registros = pd.read_csv('Registros2.csv')

#%%
"GRAFICAR [FACIES] [RHOB] [DT]"
fig, axs = plt.subplots(1, 3, sharey=False, figsize = (7,8),
                        gridspec_kw={'width_ratios': [1,1,1]})
fig.subplots_adjust(wspace=0.7)

axs[0].set_title('Facies Geológicas', style = 'normal')
facies = np.vstack(Registros.Facies)
axs[0].imshow(facies, aspect = 'auto', 
   extent=[0,1,max(Registros.Depth), min(Registros.Depth)],
   cmap = plt.cm.get_cmap('viridis', 7))
axs[0].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[0].set_xlim(0,1)
axs[0].invert_yaxis()

axs[1].set_title('RHOB', style = 'normal')
axs[1].plot(Registros.RHOB, Registros.Depth)
axs[1].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[1].invert_yaxis()

axs[2].set_title('DT', style = 'normal')
axs[2].plot(Registros.DT, Registros.Depth)
axs[2].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[2].invert_yaxis()

#%%
"CONVERSIÓN DE UNIDADES"
Registros['DT_2'] = Registros['DT'] / 0.3048 #unit convert to µs/m
Registros['RHOB_2'] = Registros['RHOB'] * 1000 #unit convert to kg/m3

#%%
"GRAFICAR [FACIES] [RHOB] [DT] CONVERTIDAS"
fig, axs = plt.subplots(1, 3, sharey=False, figsize = (7,8),
                        gridspec_kw={'width_ratios': [1,1,1]})
fig.subplots_adjust(wspace=0.7)

axs[0].set_title('Facies Geológicas', style = 'normal')
facies = np.vstack(Registros.Facies)
axs[0].imshow(facies, aspect = 'auto', 
   extent=[0,1,max(Registros.Depth), min(Registros.Depth)],
   cmap = plt.cm.get_cmap('viridis', 7))
axs[0].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[0].set_xlim(0,1)
axs[0].invert_yaxis()

axs[1].set_title('RHOB', style = 'normal')
axs[1].plot(Registros.RHOB_2, Registros.Depth)
axs[1].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[1].invert_yaxis()

axs[2].set_title('DT', style = 'normal')
axs[2].plot(Registros.DT_2, Registros.Depth)
axs[2].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[2].invert_yaxis()

#%%
"CREAR RELACIÓN TIEMPO-PROFUNDIDAD"
dt = Registros['DT_2']
dt_iterval = np.nan_to_num(dt) * 0.1524 / 1e6
t_cum =  np.cumsum(dt_iterval) * 2
Registros['TWT'] = t_cum #EN SEGUNDOS
#print(Registros['TWT']) 

#%%
"IMPEDANCIA ACÚSTICA"
Registros['Vsonic'] = 1e6/Registros.DT_2 #(unit: m/s)
Registros['AI'] = Registros['Vsonic'] * Registros['RHOB_2'] #(unit: kg/m2.s)

#%%
"COEFICIENTE DE REFLEXIÓN"
Imp = Registros['AI'].values
Rc=[]
for i in range(len(Imp)-1):
    Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1]))
# to adjust vector size copy the last element to the tail
Rc.append(Rc[-1])
Registros['Rc'] = pd.Series(Rc, index=Registros.index)

#%%
"REMUESTREO EN EL DOMINIO TIEMPO Y CÁLCULO DEL COEFICIENTE DE REFLEXIÓN"
dt = 0.001   #sampleing interval
t_max = 3   # max time to create time vector
t = np.arange(0, t_max, dt)
AI_tdom = np.interp(x=t, xp = Registros.TWT, fp = Registros.AI) #resampling
# again Rc calulation but in reampled time domain
Rc_tdom = []
for i in range(len(AI_tdom)-1):
    Rc_tdom.append((AI_tdom[i+1]-AI_tdom[i])/(AI_tdom[i]+AI_tdom[i+1]))
# to adjust vector size copy the last element to the tail
Rc_tdom.append(Rc_tdom[-1])
print(max(Rc_tdom))
#%%
"ONDÍCULA Y CONVOLUCIÓN"
# define function of ricker wavelet
def ricker(f, length, dt):
    t0 = np.arange(-length/2, (length-dt)/2, dt)
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t0**2)) * np.exp(-(np.pi**2)*(f**2)*(t0**2))
    return t0, y

f=40            #wavelet frequency
length= .512    #Wavelet vector length
dt=dt           # Sampling prefer to use smiliar to resampled AI
t0, w = ricker (f, length, dt) # ricker wavelet 
synthetic = np.convolve(w, Rc_tdom, mode='same')

#%%
"GRÁFICA FINAL"
fig, axs = plt.subplots(1, 5, sharey=False, figsize = (11,8),
                        gridspec_kw={'width_ratios': [1,2,2,0.7,2.8]})
fig.subplots_adjust(wspace=0.43)

axs[0].set_title('a) Facies\nGeológicas', style = 'normal', fontweight='bold')
facies = np.vstack(Registros.Facies)
axs[0].imshow(facies, aspect = 'auto', 
   extent=[0,1,max(Registros.Depth), min(Registros.Depth)],
   cmap = plt.cm.get_cmap('viridis', 7))
axs[0].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[0].set_xlim(0,1)
axs[0].invert_yaxis()
axs[0].set_xticks([])

axs[1].plot( AI_tdom, t,'b', alpha=0.8)
axs[1].set_title('b) Impedancia\nAcústica', style = 'normal', fontweight='bold')
axs[1].set_xlabel( r'$kg/m^2s^2$', fontsize = '10')
axs[1].set_yticklabels('')
axs[1].set_ylim(min(Registros['TWT']),max(Registros['TWT']))
axs[1].invert_yaxis()
axs[1].set_yticks([])
axs[1].grid()

axs[2].plot( Rc_tdom, t,'k')
axs[2].plot([0, 0], [t.min(), t.max()], '--', c='blue')
axs[2].set_title('c) Reflectividad\n', style = 'normal', fontweight='bold')
axs[2].set_xlabel( r'Fracción', fontsize = '10')
axs[2].set_xlim(-0.5 , 0.5)
axs[2].set_ylim(min(Registros['TWT']),max(Registros['TWT']))
axs[2].invert_yaxis()
axs[2].set_yticks([])
axs[2].grid()

axs[3].plot( w, t0+1.4,'r', alpha=0.99)
axs[3].fill_betweenx(t0+1.4 , w,  0,  w > 0.0,  color='r')
axs[3].set_title('d) Ondícula\n', style = 'normal', fontweight='bold')
axs[3].set_xlabel('F:'+ str(f)+'Hz' , fontsize = '10')
axs[3].set_yticklabels('')
axs[3].invert_yaxis()
axs[3].set_xticks([])
axs[3].set_yticks([])

offsets=[0.2, 0.4, -0.2, -0.4, -0.6, 0.6]

axs[4].plot( synthetic, t ,'r')
axs[4].fill_betweenx(t, synthetic,  0,  synthetic > 0,  color='r')
axs[4].plot( synthetic+0.2, t ,'k')
axs[4].fill_betweenx(t, offsets[0] , synthetic+0.2, where=(synthetic+0.2>offsets[0]),color='k')
axs[4].plot( synthetic+0.4, t ,'k')
axs[4].fill_betweenx(t, offsets[1] , synthetic+0.4, where=(synthetic+0.4>offsets[1]),color='k')
axs[4].plot( synthetic-0.2, t ,'k')
axs[4].fill_betweenx(t, offsets[2] , synthetic-0.2, where=(synthetic-0.2>offsets[2]),color='k')
axs[4].plot( synthetic-0.4, t ,'k')
axs[4].fill_betweenx(t, offsets[3] , synthetic-0.4, where=(synthetic-0.4>offsets[3]),color='k')
axs[4].plot( synthetic-0.6, t ,'k')
axs[4].fill_betweenx(t, offsets[4] , synthetic-0.6, where=(synthetic-0.6>offsets[4]),color='k')
axs[4].plot( synthetic+0.6, t ,'k')
axs[4].fill_betweenx(t, offsets[5] , synthetic+0.6, where=(synthetic+0.6>offsets[5]),color='k')

axs[4].set_title('e) Sismograma\nSintético (Trazas)', style = 'normal', fontweight='bold')
axs[4].set_xlim(-0.8 , 0.8)
axs[4].set_xticklabels('')
axs[4].set_ylim(min(Registros['TWT']),max(Registros['TWT']))
axs[4].invert_yaxis()
axs[4].set_xticks([])
axs[4].grid()

fig.savefig('Figura 6.png',bbox_inches="tight", dpi=1200)