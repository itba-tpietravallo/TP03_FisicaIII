import csv
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt


def leer_archivo_csv(ruta_archivo):
    indice_inicio = 17
    datos_onda = pd.read_csv(ruta_archivo, skiprows=indice_inicio, usecols=[0], names=['Datos de Onda'])
    return datos_onda['Datos de Onda'].tolist()


def escribir_archivo_csv(ruta_archivo, valores_x, valores_y):
    with open(ruta_archivo, 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Tiempo (ms)', 'Voltaje (V)'])
        for i in range(len(valores_x)):
            escritor.writerow([valores_x[i], valores_y[i]])


def generar_grafico(valores_x, valores_y, nombre_archivo):
    plt.figure(figsize=(10, 6))
    plt.scatter(valores_x, valores_y)
    # plt.title('Tensión en función del tiempo')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Tensión(V)')
    plt.grid(True)
    plt.ylim(-40, 40)
    plt.savefig(nombre_archivo)


# Ruta a la carpeta que contiene los archivos CSV
ruta_carpeta = Path('csv/')
# Crear un nuevo directorio llamado "datos" si no existe
Path('datos').mkdir(exist_ok=True)
# Crear un nuevo directorio llamado "graficos" si no existe
Path('graficos').mkdir(exist_ok=True)

# Leer todos los archivos CSV en la carpeta
archivos_csv = sorted(ruta_carpeta.glob('*.CSV'), key=lambda x: os.path.basename(x))

periodo_muestreo = 4

# Leer y almacenar los datos de waveform data y el periodo de muestreo de cada archivo CSV
for idx, archivo in enumerate(archivos_csv):
    valores_y = leer_archivo_csv(archivo)
    n = len(valores_y)
    valores_x = [i * periodo_muestreo for i in range(n)]

    # Crear un nuevo archivo CSV para almacenar los resultados en el directorio "datos"
    escribir_archivo_csv(Path('datos') / f"{Path(archivo).stem}DatosOnda.csv", valores_x, valores_y)

    # Usar la función para generar gráficos
    generar_grafico(valores_x, valores_y, Path('graficos') / f"{Path(archivo).stem}DatosOnda.png")

    print(f"Archivo #{Path(archivo).stem} terminado")
