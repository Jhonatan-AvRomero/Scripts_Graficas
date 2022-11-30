# -*- coding: utf-8 -*-
"""
@author: Jhonatan
"""
#%%
'IMPORTAR LIBRERÍAS'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
'DICCIONARIO DE LITOLOGÍAS'
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
'ONDÍCULA RICKER'
def ricker(f, length, dt):
    t0 = np.arange(-length/2, (length-dt)/2, dt)
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t0**2)) * np.exp(-(np.pi**2)*(f**2)*(t0**2))
    return t0, y
dt = 0.01   #sampleing interval
#%%
'EJEMPLO DE SISMOGRAMA SINTÉTICO'
lenght_prof = np.arange(0,4.5,0.01)
Rc_tdom = []
for i in lenght_prof:
    if i == 3.5 or i == 2.0:
        Rc_tdom = np.append(Rc_tdom,0.5)
    else:
        Rc_tdom = np.append(Rc_tdom,0.2)
'CONVOLUCIÓN DEL SISMOGRAMA'
f=3            #frecuencia de la ondícula
length= 4.5   #longitud del vector ondícula
dt=dt           # Sampling prefer to use smiliar to resampled AI
t0, w = ricker (f, length, dt) #ondícula Ricker
synthetic = np.convolve(w, Rc_tdom, mode='same')
i=0
for s in synthetic:
    synthetic[i] = s + 11
    i = i +1
#%%
'PROFUNDIDAD DE LOS ESTRATOS'
ancho_estratos = [0,1] #X
profundidad_estratos = ([0,0.5],[0.5,0.9],[0.9,1.2]) #Y
#%%
'GRÁFICA FINAL'
fig, (ax1,ax2,ax3,ax4) = plt.subplots(ncols=1, nrows=4, figsize=(8,4), 
      gridspec_kw = {'height_ratios':[1,2,1.5,1]},
      subplot_kw = {'xticks':[], 'yticks':[]})
#%%
'ESPACIO AZUL'
ax1.set_xlim(0,12)
ax1.set_ylim(1,0)
prof1 = [0,1]
ax1.fill_betweenx(prof1, 0, 10,
                 facecolor='blue', alpha=0.5)
ax1.text(1, 0.8, 'Fuente sísmica', style ='italic',fontweight ='bold',
        fontsize = 10, color ="black",bbox ={'facecolor':'white','pad':5})
ax1.text(6.7, 0.8, 'Receptor sísmico', style ='italic',fontweight ='bold',
        fontsize = 10, color ="black",bbox ={'facecolor':'white','pad':5})
ax1.text(9.8, 0.8, 'Traza sísmica', style ='italic',fontweight ='bold',
        fontsize = 10, color ="black",bbox ={'facecolor':'white','pad':5})
#%%
'GRAFICAR VIAJE DE ONDAS, FUENTE'
x2 = [2,5,8] #Primera reflexión
y2 = [0,3.5,0] #Primera reflexión
x2_2 = [2,5,8] #Segunda reflexión
y2_2 = [0,2,0] #Segunda reflexión
fuente = [2,0]#Punto de la fuente
receptor = [8,0]#Punto del receptor
ax2.plot(x2,y2,'g-',linewidth = 4) #Graficar recorrido de Onda
ax2.plot(x2_2,y2_2,linewidth = 4)
ax2.plot(fuente[0],fuente[1],'v',markersize='30')
'ESTILO ESTRATO 1'
ax2.text(1, 1, 'Estrato 1', style ='italic',fontweight ='bold',
        fontsize = 10, color ="Blue",bbox ={'facecolor':'white','pad':5})
ax2.text(11.3, 1.5, 'Reflexiones de la\n'+'base del estrato 1', style ='italic',fontweight ='bold',
        fontsize = 8, color ="Blue",bbox ={'facecolor':'white','pad':5})
'GRAFICAR RECEPTOR'
ax2.plot(receptor[0],receptor[1],'o',markersize='20')
ax2.plot(synthetic, lenght_prof, '-', color='black')
ax2.set_xlim(0,12)
ax2.set_ylim(2,0)
prof2 = [0,2]
ax2.fill_betweenx(prof2, 0, 10,
                 facecolor=litología_números[65000]['color'],
                 hatch=litología_números[65000]['hatch'], alpha = 0.7)
ax2.text(8, 1, r'$v_1 * \rho_1 = IA_1$', style ='italic',fontweight ='bold',
        fontsize = 10, color ="Blue",bbox ={'facecolor':'white','pad':5})
#%%
'GRAFICAR VIAJE DE ONDAS'
x3 = [2,5,8] #Primera reflexión
y3 = [-2,1.5,-2] #Primera reflexión
ax3.plot(x3,y3,'g-',linewidth = 4) #Graficar recorrido de Onda
ax3.set_xlim(0,12)
ax3.set_ylim(1.5,0)
ax3.set_ylabel('Tiempo de viaje doble (s)', fontsize = 12, fontweight = 'bold')
'GRAFICAR ESTRATO 2'
ax3.text(1, 0.75, 'Estrato 2', style ='italic',fontweight ='bold',
        fontsize = 10, color ="Blue",bbox ={'facecolor':'white','pad':5})
ax3.text(11.3, 1, 'Reflexiones de la\n'+'base del estrato 2', style ='italic',fontweight ='bold',
        fontsize = 8, color ="Blue",bbox ={'facecolor':'white','pad':5})
i = 0
for p in lenght_prof:
    lenght_prof[i] = p - 2
    i = i + 1
ax3.plot(synthetic, lenght_prof, '-', color='black')

prof3 = [0,1.5]
ax3.fill_betweenx(prof3, 0, 10,
                 facecolor=litología_números[30000]['color'],
                 hatch=litología_números[30000]['hatch'], alpha = 0.6)
ax3.text(8, 0.75, r'$v_2 * \rho_2 = IA_2$', style ='italic',fontweight ='bold',
        fontsize = 10, color ="Blue",bbox ={'facecolor':'white','pad':5})

ax4.set_xlim(0,12)
ax4.set_ylim(1,0)
ax4.text(1, 0.5, 'Estrato 3', style ='italic',fontweight ='bold',
        fontsize = 10, color ="Blue",bbox ={'facecolor':'white','pad':5})
i = 0
for p in lenght_prof:
    lenght_prof[i] = p - 1.5
    i = i + 1
ax4.plot(synthetic, lenght_prof, '-', color='black')

prof4 = [0,1]
ax4.fill_betweenx(prof4, 0, 10,
                 facecolor=litología_números[70000]['color'],
                 hatch=litología_números[70000]['hatch'])

fig.suptitle('Método sísmico de reflexión', fontsize=16, fontweight='bold',style='italic')
plt.subplots_adjust(hspace = 0)
plt.show()
fig.savefig('Figura 1.png',bbox_inches="tight", dpi=1200)