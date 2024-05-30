# README
Este repositorio contiene el código utilizado para procesar  la información obtenida a partir de un oscilómetro digital. La información que resulte de este código complementa al informe para el Trabajo Práctico N°3, correspondiente al *Grupo 3 de la Comisión S*.

> [!TIP]
> [Puede ver el codigo y resultados generados en Google Colab](#google-colab) (en la nube) sin necesidad de tener su entorno configurado para el desarrollo con Python

## Breve introducción
Cuando se realizó el trabajo práctico, notamos que el oscilómetro contaba con un puerto USB, y por pura curiosidad decidimos investigar si era posible obtener los datos de las mediciones realizadas en formato digital. Luego de una búsqueda en internet, encontramos el manual del dispositivo, que indicaba que se guardaban los datos en formato CSV. Pero esto no era suficiente, ya que solo proveia los datos crudos sin ningun tipo de grafico o analisis. Por lo tanto, decidimos realizar un script que permitiera calcular la frecuencia, voltajes pico a pico (Vpp), y los gráficos para cada medida realizada con el instrumento.

Tambien, dado que contabamos con muchas medidas y un gran volumen de datos, pudimos generar un grafico de el voltaje pico a pico en funcion de la frecuencia de la fuente.

### Miembros del grupo: 
* Matias Cuneo Gima
* Lucia Oliveto
* Manuel Othatceguy
* Tomas Pietravallo
* Santiago Sanchez Marostica
* Gregorio Tiscornia
* Máximo Wehncke


## Sobre la utilización de este código
El código se encuentra en el archivo `main.py`. Para ejecutarlo, se debe tener instalado Python 3.* o superior con las librerías `matplotlib` y `pandas` instaladas. Luego, al ejecutarlo en un intérprete acorde, se generarán dos carpetas, una conteniendo los gráficos y otra con los datos obtenidos en formato csv.

### Google Colab
Puede utilizar este link para correr el codigo y ver las imagenes generadas en la nube, sin necesidad de tener Python u otras librerias instaladas en su dispositivo. 

[Utilice este link para acceder a el Notebook en Google Colab](https://colab.research.google.com/drive/1GueU-vnJgkDNZF2O6SDmPRxEswGQP3tA?usp=sharing)
