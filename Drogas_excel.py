import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20
       }
rc('font', **font)

#################################
##		Consumo de Drogas      ##
#################################

drogas = {
    "./xlsx/cannabis.xlsx" : "cannabis",
    "./xlsx/anfetaminas.xlsx" : "anfetaminas",
    "./xlsx/heroina.xlsx" : "heroina",
    "./xlsx/lsd.xlsx" : "lsd"
}

dfs = []

for filename in drogas.keys():
    data = pd.read_excel(filename, index_col=0,
                       header=None,
                      ).T
    data["Droga"] = drogas[filename]
    data.dropna(axis=1, inplace=True)
    dfs.append(data)

df = pd.concat(dfs, sort=True)
df.set_index("Country", inplace=True)
df.index.names = ["Year"]

grp_drg = df.groupby(["Droga"])

fig = plt.figure(figsize=(20, 20))
axs = [fig.add_subplot(221+i) for i in range(4)]

for ax, dr in zip(axs, drogas.values()):
    grp_drg.get_group(dr).plot(ax=ax, title=dr)

plt.show()

#################################
##			Incomepc 		   ##
#################################

incomepc = pd.read_excel("./xlsx/incomepc.xlsx", index_col=0,
                       header=None,
                      ).T

incomepc.set_index("Country", inplace=True)
incomepc.dropna(axis=1, inplace=True)
incomepc.index.names = ["Year"]
incomepc.drop("Unit", inplace=True)

incomepc.plot()
plt.show()

#################################
##		Muertes Por drogas     ##
#################################

muertes = pd.read_excel("./xlsx/muetesdrogas.xlsx", index_col=0,
                       header=None,
                      ).T

muertes.set_index("geo\\time", inplace=True)
muertes.index.names = ["Year"]

muertes.plot()
plt.show()

#################################
##			Por Paises   	   ##
#################################

#------------------------
#	Spain
#------------------------

fig = plt.figure(figsize=(30, 10))
axs = [fig.add_subplot(131+i) for i in range(3)]
pais = "Spain"

fig.suptitle(pais, fontsize=26)
grp_drg[pais].plot(ax=axs[0], title="Drogas")
axs[0].legend()
muertes[pais].plot(ax=axs[1], title="Muertes")
incomepc[pais].plot(ax=axs[2], title="Incomepc")
plt.show()

#------------------------
#	Croatia
#------------------------

fig = plt.figure(figsize=(30, 10))
axs = [fig.add_subplot(131+i) for i in range(3)]
pais = "Croatia"

fig.suptitle(pais, fontsize=26)
grp_drg[pais].plot(ax=axs[0], title="Drogas")
axs[0].legend()
muertes[pais].plot(ax=axs[1], title="Muertes")
incomepc[pais].plot(ax=axs[2], title="Incomepc")
plt.show()

#------------------------
#	Italy
#------------------------

fig = plt.figure(figsize=(30, 10))
axs = [fig.add_subplot(131+i) for i in range(3)]
pais = "Italy"

fig.suptitle(pais, fontsize=26)
grp_drg[pais].plot(ax=axs[0], title="Drogas")
axs[0].legend()
muertes[pais].plot(ax=axs[1], title="Muertes")
incomepc[pais].plot(ax=axs[2], title="Incomepc")
plt.show()

#------------------------
#	Hungary
#------------------------

fig = plt.figure(figsize=(30, 10))
axs = [fig.add_subplot(131+i) for i in range(3)]
pais = "Hungary"

fig.suptitle(pais, fontsize=26)
grp_drg[pais].plot(ax=axs[0], title="Drogas")
axs[0].legend()
muertes[pais].plot(ax=axs[1], title="Muertes")
incomepc[pais].plot(ax=axs[2], title="Incomepc")
plt.show()

#------------------------
#	Sweden
#------------------------

fig = plt.figure(figsize=(30, 10))
axs = [fig.add_subplot(131+i) for i in range(3)]
pais = "Sweden"

fig.suptitle(pais, fontsize=26)
grp_drg[pais].plot(ax=axs[0], title="Drogas")
axs[0].legend()
muertes[pais].plot(ax=axs[1], title="Muertes")
incomepc[pais].plot(ax=axs[2], title="Incomepc")
plt.show()

#------------------------
#	Netherlands
#------------------------

fig = plt.figure(figsize=(30, 10))
axs = [fig.add_subplot(121+i) for i in range(2)]
pais = "Netherlands"

fig.suptitle(pais, fontsize=26)
grp_drg[pais].plot(ax=axs[0], title="Drogas")
axs[0].legend()
muertes[pais].plot(ax=axs[1], title="Muertes")
plt.show()


