# README
> Este repositorio contiene el código utilizado para procesar  la información obtenida a partir de un oscilómetro digital.

La información que resulte de este código complementa al informe para el Trabajo Práctico n°3, correspondiente al grupo 2 de la comisión S.

## Breve introducción
Cuando se realizó el trabajo práctico, notamos que el oscilómetro contaba con un puerto USB, y por pura curiosidad decidimos investigar si era posible obtener los datos de las mediciones realizadas en formato digital. Luego de una búsqueda en internet, encontramos el manual del dispositivo, que indicaba que se guardaban los datos en formato CSV. Pero esto no era suficiente, ya que no se podía generar un gráfico o entender lo que estábamos viendo sin interpretar los datos. Por lo tanto, decidimos realizar un script que permitiera generar los gráficos e interpretar los datos, dejándolos como pares (x,y).


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
