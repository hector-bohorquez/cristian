#Metodologia
#importar librerias

import os
import pandas as Pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline =
font = {'size':12}
plt.rc('font',**font)

#Leer analizar y corregir datos N a N en el dataset 
#2
os.chdir ("")
datos = Pd.read_csv("", delimiter = ',')

#3
datos.head()

#4
datos.dtypes

#5
datos.describe()

#6
datos.isna().sum()

#7
mediaEdades = round (datos['Age'].mean())
datos['Age'] = datos['Age'].fillna(mediaEdades)
datos.isna().sum()

#8
datos['Cabin'] = datos['Cabin'].fillna("NE")
datos.isna().sum()

#14
datos['Cabin'].value_counts()

#15
datos['Embarqued'] = datos['Embarqued'].fillna("NE")
datos.isna().sum()

#16
datos['Embarqued'].value_counts
#17
datos.head()

#Para una mejor lectura cambiemos algunos datos
#18
datos ['Survived'] = datos ['Survived'].map({
    0:'No'
    1:'Yes'
})
datos.head()

#19
datos['Embarqued'] = datos['Embarqued'].map({
    'S':'Southampton'
    'C':'Cherbourg'
    'Q':'Queenstown'
})
datos.head()

#Ya preparado el data set, veamos que informacion valiosa podemos obtener del mismo
#20
datos.groupby(['Pclass','Survived'])['Survived'].count
ax = sns.countplot (x = 'Pclass, hue='Survived', palette='Set1', data=datos)
ax.set(title) = 'Estado del pasajero(murio/sobrevio') dado a la clase a la que pertenecia, xlabel='Clase del pasajero', ylabel='Total')
plt.show()

#21
datos.groupby(['Sex', 'Survived'])['Survived'.count()]




