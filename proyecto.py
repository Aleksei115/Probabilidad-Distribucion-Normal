from cmath import exp
from math import factorial

from multiprocessing.reduction import duplicate
from os import sep
from statistics import mode
from tkinter.tix import COLUMN
from unittest import mock
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("./weatherHistory.csv")

datos = pd.DataFrame(df)

# Agregamos una columna que tenga formato de fecha
datos[["Date-Time","TZ"]] = datos["Formatted Date"].str.split("+",expand=True)

# Eliminamos la columna Formatted Date y creamos un nuevo dataset 
datos1 = datos.drop(columns="Formatted Date")\

#Reordeno columnas 
columns_order=["Date-Time","TZ","Summary","Precip Type","Temperature (C)","Apparent Temperature (C)",
                "Humidity","Wind Speed (km/h)","Wind Bearing (degrees)","Visibility (km)","Loud Cover",
                "Pressure (millibars)", "Daily Summary"]

datos1 = datos1.reindex(columns=columns_order)
datos1 = datos1.drop(columns="TZ")

#Doy fomato a las fechas

datos1["Date-Time"] = pd.to_datetime(datos1["Date-Time"])
datos1["Year"] = datos1["Date-Time"].dt.year
datos1["Month"] = datos1["Date-Time"].dt.month
datos1["Day"] = datos1["Date-Time"].dt.day

datos1 = datos1.drop(columns="Date-Time")

columns_order=["Day","Month","Year","Summary","Precip Type","Temperature (C)","Apparent Temperature (C)",
                "Humidity","Wind Speed (km/h)","Wind Bearing (degrees)","Visibility (km)","Loud Cover",
                "Pressure (millibars)", "Daily Summary"]

datos1 = datos1.reindex(columns=columns_order)


#Creo un data frame que solo tenga los 

# print(datos1.head( n = 100))


#Creo un dataFrame con la media por año de la velocidad del viento 
avg_wind_Speed=pd.DataFrame(datos1.groupby("Year")["Wind Speed (km/h)"].mean())

# print(avg_wind_Speed)
print(avg_wind_Speed[["Wind Speed (km/h)"]].describe())
print(avg_wind_Speed[["Wind Speed (km/h)"]].mode())
# print(avg_wind_Speed[["Wind Speed (km/h)"]].std())

#Con estos datos vamos suponer que son mediciones y no medias por año, 
# esto quiere decir que ahora vamos a obtener el promedio de la velocidad del viento por año.
#Esto nos ayudara a obtener una distribucion exponencial y calcular la probabilidad de que la velocidad del viento sea menor a 10.8 km
d_lamda = avg_wind_Speed[["Wind Speed (km/h)"]].mean()

x = np.arange(0, 30, .1)
y = stats.poisson.pmf(x, mu=d_lamda, loc = 1)


# print(stats.poisson.std( mu = d_lamda))
plt.plot(x, y)
plt.title("Poisson distribution with mu=10 and loc=0")
plt.xlabel("Random variable")
plt.ylabel("Probability")
# plt.show()

#Ahora que tenemos la funcion masa de probabilidad responderemos estas preguntas 

#Cual es la probabilidad de que la velocidad sea 10.81

# def probabilidad(x):
#     return math.exp(-d_lamda)*(math.pow(d_lamda,x))/(factorial(x))

# def probabilidad(x):
#     return math.exp(-d_lamda)*(math.pow(d_lamda,x))/(factorial(x))

# p1 = probabilidad(10)
# print(p1)

# Cual es la probabilidad de que la velocidad del viento sea menor a 10 km/h

# def probabilidadAcumuladaI(x):
#     accum = 0
#     for y in range(0,x+1):
#         accum += math.exp(-d_lamda)*(math.pow(d_lamda,y))/(factorial(y))
    
#     return accum

# p2 = probabilidadAcumuladaI(10)
# print(p2)

# Mostrar la funcion de probabilidad acumulada 

# y = stats.poisson.cdf(x, mu=d_lamda)

# plt.plot(x, y)
# plt.title("CDF of Poisson distribution with mu=10")
# plt.xlabel("Random variable")
# plt.ylabel("Cumulative Probability")
# plt.show()

