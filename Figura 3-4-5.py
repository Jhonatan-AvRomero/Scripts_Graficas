# -*- coding: utf-8 -*-
"""
@author: Jhonatan
"""
#Registro Sónico
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Registros = pd.read_csv('Registros2.csv')

"Conversión de unidades"
Registros['DT_2'] = Registros['DT'] / 0.3048   #unit convert to µs/m
Registros['RHOB'] = Registros['RHOB'] * 1000  #unit convert to kg/m3

fig, axs = plt.subplots(1, 3, sharey=False, figsize = (8,8),
                        gridspec_kw={'width_ratios': [1,1,1]})
fig.subplots_adjust(wspace = 1.5)

axs[0].plot(Registros.DT, Registros.Depth, alpha = 0.5)
axs[0].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[0].set_xlabel( r'$\mu s/ft $', fontsize = '12', fontweight = 'bold')
axs[0].grid()
axs[0].set_title('DT', fontweight = 'bold', fontsize = 13)
axs[0].invert_yaxis()

axs[1].plot(Registros.DT_2, Registros.Depth)
axs[1].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[1].set_xlabel( r'$\mu s/m $', fontsize = '12', fontweight = 'bold')
axs[1].grid()
axs[1].set_title('DT', fontweight = 'bold', fontsize = 13)
axs[1].invert_yaxis()

"Relación tiempo-profundidad-------------------------------------------------------"
log_start = min(Registros['Depth'])              # Depth of logging starts(m) from header
kb = 15
gap_int = log_start - kb
repl_vel = 2632                # this is from VSP data knowledge (m/s)
log_start_time = 2.0 * gap_int / repl_vel        # 2 for twt

dt = Registros['DT']
dt_iterval = np.nan_to_num(dt) * 0.1524 / 1e6
t_cum =  np.cumsum(dt_iterval) * 2
Registros['TWT'] = t_cum + log_start_time

""
Registros['Vsonic'] = 1e6/Registros.DT #(unit: m/s)

axs[2].plot(Registros.Vsonic, Registros.Depth, 'r', alpha = 0.7)
axs[2].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[2].set_xlabel( r'$ m/s $', fontsize = '12', fontweight='bold')
axs[2].grid()
axs[2].set_title('Velocidad sónica',fontweight = 'bold', fontsize = 13)
axs[2].invert_yaxis()
fig.savefig('Figura 3.png',bbox_inches="tight", dpi=1200)

Registros['AI'] = Registros['Vsonic'] * Registros['RHOB']#(unit: kg/m2.s)

fig, axs = plt.subplots(1, 3, sharey=False, figsize = (8,8),
                        gridspec_kw={'width_ratios': [1,1,1]})
fig.subplots_adjust(wspace = 1.5)

axs[0].plot(Registros.Vsonic, Registros.Depth, 'r', alpha = 0.7)
axs[0].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[0].set_xlabel( r'$ m/s $', fontsize = '12')
axs[0].grid()
axs[0].set_title('Velocidad\nSónica',fontweight = 'bold', fontsize = 13)
axs[0].invert_yaxis()

axs[1].plot(Registros.RHOB, Registros.Depth)
axs[1].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[1].set_xlabel( r'$kg/m^3 $', fontsize = '12')
axs[1].grid()
axs[1].set_title('RHOB\n',fontweight = 'bold', fontsize = 13)
axs[1].invert_yaxis()
axs[1].set_xticklabels([2000,2250,2500,2750],rotation = 25,ha="right")

axs[2].plot(Registros.AI, Registros.Depth, 'purple', alpha = 0.7)
axs[2].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[2].set_xlabel( r'$kg/m^2s    $', fontsize = '12')
axs[2].grid()
axs[2].set_title('Impedancia\nAcústica',fontweight = 'bold', fontsize = 13)
axs[2].invert_yaxis()

fig.savefig('Figura 4.png',bbox_inches="tight", dpi=1200)
"Coeficiente de reflexión"
Imp = Registros['AI'].values
Rc=[]
for i in range(len(Imp)-1):
    Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1]))

# to adjust vector size copy the last element to the tail
Rc.append(Rc[-1])

Registros['Rc'] = pd.Series(Rc, index=Registros.index)

"Graficar"
fig, axs = plt.subplots(1, 2, sharey=False, figsize = (5,8),
                        gridspec_kw={'width_ratios': [1,1]})
fig.subplots_adjust(wspace = 1.5)

axs[0].plot(Registros.AI, Registros.Depth, 'purple', alpha = 0.7)
axs[0].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[0].set_xlabel( r'$kg/m^2s    $', fontsize = '12')
axs[0].grid()
axs[0].set_title('Impedancia\nAcústica',fontweight = 'bold', fontsize = 13)
axs[0].invert_yaxis()

axs[1].plot(Registros.Rc, Registros.Depth,'k', alpha = 0.7)
axs[1].set_ylim(min(Registros.Depth), max(Registros.Depth))
axs[1].set_xlabel( r'Fracción', fontsize = '12')
axs[1].grid()
axs[1].set_title('Serie de\nReflectividad',fontweight = 'bold', fontsize = 13)
axs[1].invert_yaxis()
fig.savefig('Figura 5.png',bbox_inches="tight", dpi=1200)