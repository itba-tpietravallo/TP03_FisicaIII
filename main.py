import csv
import pandas as pd
import numpy as np
import os
import math
from pathlib import Path
import matplotlib.pyplot as plt

divisiones_verticales = 8

def leer_archivo_csv(ruta_archivo):
    indice_inicio = 17
    indice_volts = 6
    indice_sampling = 13
    ch1 = int((pd.read_csv(ruta_archivo, skiprows=lambda x: x != indice_volts).columns[1][:-1]))
    sampling = float(pd.read_csv(ruta_archivo, skiprows=lambda x: x != indice_sampling).columns[1].split('u')[0])
    datos_onda = pd.read_csv(ruta_archivo, skiprows=indice_inicio, usecols=[0], names=['Datos de Onda'])
    return list(map(lambda x: x / (ch1 * divisiones_verticales), datos_onda['Datos de Onda'].tolist())), sampling


def escribir_archivo_csv(ruta_archivo, valores_x, valores_y):
    with open(ruta_archivo, 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow([f'Tiempo (\u00B5s)', 'Voltaje (V)'])
        for i in range(len(valores_x)):
            escritor.writerow([valores_x[i], valores_y[i]])


def generar_grafico(valores_x, valores_y, vpp, frecuencia, nombre_archivo):
    plt.figure(figsize=(10, 6))
    plt.scatter(valores_x, valores_y, label=f"Frecuencia: {frecuencia}kHz")
    plt.title(f'Tensión en función del tiempo. Frecuencia: {frecuencia}kHz. Voltaje pico a pico: {vpp}V')
    plt.xlabel(f'Tiempo (\u00B5s)')
    plt.ylabel('Tensión (V)')
    plt.grid(True)
    plt.ylim(-4, 4)
    plt.savefig(nombre_archivo)
    plt.close()

def calcular_frecuencia(valores_x: list[int], valores_y: list[int], periodo_muestreo: float):
    min = []
    max = []
    vpp = []

    prev_value = valores_y[0]
    prev_value_at_p = valores_y[0]
    indices = [0]

    for i, y in enumerate(valores_y):
        if (
            # Bolzano
            y * prev_value < 0 or
            y * prev_value_at_p < 0
            ):
            prev_value_at_p = y
            indices.append(i)

        prev_value = y

    for i, _ in enumerate(indices, 1):
        if i >= len(indices):
            break
        valores = valores_y[indices[i-1]:indices[i]]
        ma = np.max(valores)
        mi = np.min(valores)
        if (abs(ma) > abs(mi)):
            max.append(ma)
        else:
            min.append(mi)

    for ma, mi in zip(max, min):
        vpp.append(ma - mi)

    vpp_value = np.mean(vpp)
    freq_data = indices[1:-1]
    cycles = len(freq_data) / 2 # Half-cycles / 2
    frequency_hz = cycles / ((freq_data[-1] - freq_data[0]) * (periodo_muestreo / 1_000_000 ))
    return round(vpp_value, 2), round(frequency_hz / 1000, 3)

# Ruta a la carpeta que contiene los archivos CSV
ruta_carpeta = Path('csv/')
# Crear un nuevo directorio llamado "datos" si no existe
Path('datos').mkdir(exist_ok=True)
# Crear un nuevo directorio llamado "graficos" si no existe
Path('graficos').mkdir(exist_ok=True)

# Leer todos los archivos CSV en la carpeta
archivos_csv = sorted(ruta_carpeta.glob('*.CSV'), key=lambda x: os.path.basename(x))

vpp_freq = []

# Leer y almacenar los datos de waveform data y el periodo de muestreo de cada archivo CSV
for idx, archivo in enumerate(archivos_csv):
    valores_y, periodo_muestreo = leer_archivo_csv(archivo)
    valores_x = [i * periodo_muestreo for i in range(len(valores_y))]

    # Crear un nuevo archivo CSV para almacenar los resultados en el directorio "datos"
    escribir_archivo_csv(Path('datos') / f"{Path(archivo).stem}DatosOnda.csv", valores_x, valores_y)

    vpp, frecuencia = calcular_frecuencia(valores_x=valores_x, valores_y=valores_y, periodo_muestreo=periodo_muestreo)
    vpp_freq.append([vpp, frecuencia])

    # Usar la función para generar gráficos
    generar_grafico(valores_x, valores_y, vpp, frecuencia, Path('graficos') / f"{Path(archivo).stem}DatosOnda.png")

    if idx % 5 == 0:
        print(f"Archivo #{Path(archivo).stem} terminado")

# Genera un grafico de el VPP en funcion de la frecuencia
plt.figure(figsize=(10, 6))
plt.scatter(list(map(lambda x : x[1],vpp_freq)), list(map(lambda x : x[0],vpp_freq)))
plt.title(f'Vpp en funcion de la Frecuencia')
plt.xlabel('Frecuencia (kHz)')
plt.ylabel('Vpp(V)')
plt.grid(True)
plt.ylim(0, 6)
plt.savefig(Path('graficos') / f"Frecuencia_Vpp.png")
plt.close()