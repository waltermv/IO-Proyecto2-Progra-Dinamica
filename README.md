# Investigación de Operaciones - Proyecto #2 Programación Dinámica
Proyecto programado del curso de Investigación de Operaciones, código IC-6400. 

El proyecto consta de dos partes: la primera es el programa computacional que resuelve y genera los problemas de mochila o de alineamiento de secuencias, la segunda parte es un reporte escrito con los resultados de los experimentos ejecutados.

## Solucionador

Programa para solucionar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.
Para la resolver cada uno de los problemas se brindan dos opciones: utilizar un algoritmo de fuerza bruta o uno de
programación dinámica (esto deberá ser especificado en los parámetros de la aplicación).
Este programa fue creado como solución al proyecto programdo del curso de Investigación de Operaciones en el segundo
semestre del año 2020 dado en el Instituto Tecnológico de Costa Rica.

### Uso del programa:

`python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO`

Donde:
- El parámetro -h es opcional y muestra la forma de utilización del programa.
- PROBLEMA será el número 1 o 2; 1 si se desea resolver un problema de mochila y 2 si es de alineamiento.
- ALGORITMO es un valor de 1 o 2; si se desea solucionar mediante fuerza bruta 1 y si se requiere usar
programación dinámica 2.
- ARCHIVO es el nombre del archivo de entrada el cual se obtendrán los datos del problema. Deberá encontrarse
en el directorio raíz del proyecto.
    - En el caso de que se use mochila:
        - Línea 1: Peso máximo soportado por el contenedor. Ej: 50
        - Línea i: Elemento en la posición i (peso, beneficio, cantidad). Ej: 5,20,4
                                                                              15,50,3
                                                                              10,60,3

    - En el caso de ser un problema de alineamiento:
        - Línea 1: Primera secuencia a alinear. Ej: ATTGTGATCC
        - Línea 2: Segunda secuencia a alinear. Ej: TTGCATCGGC

### Salida del programa:
- En el caso de mochila:
    - Línea 1: Beneficio máximo posible. Ej: 260
    - Línea j: Posición original del artículo: i, cantidad de unidades. Ej: 1,4
                                                                            3,3

- En el caso de alineamiento:
    - Línea 1: Indica el "score" final de los alineamientos. Ej: -2
    - Línea 2: Hilera resultado para la primer secuencia.
    - Línea 3: Hilera resultado para la segunda secuencia.
    * En el caso de que se utilizara programación dinámica para resolver el problema, el programa generará
    un archivo csv con la matriz resultado, se utilizará el nombre del archivo de donde se obtuvieron los datos
    junto con el sufijo "_solution" para este fin.
    
## Generador

Programa para generar problemas de contenedor (o también llamados mochila) y de alineamiento de secuencias.
Se recibirán especificaciones de cómo deberán ser los parámetros y la aplicación deberá generar problemas que cumplan
con estas delimitaciones. Para ambos problemas el archivo generado aparecerá en la carpeta raíz del proyecto.
Este programa fue creado como solución al proyecto programdo del curso de Investigación de Operaciones en el segundo
semestre del año 2020 dado en el Instituto Tecnológico de Costa Rica.

### Uso del programa:

`python3 generator.py [-h] PROBLEMA ARCHIVO PARÁMETROS`

Donde:
- El parámetro -h es opcional y muestra la forma de utilización del programa.
- PROBLEMA será el número 1 o 2; 1 si se desea obtener un problema de mochila y 2 si es de alineamiento.
- ARCHIVO será el nombre del archivo con los problemas resultantes.
- PARÁMETROS limitaciones que deberá cumplir el programa.
    - Si se requieren problemas de mochila será:
        W N  minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad

        W: Peso soportado por el contenedor.
        N: Cantidad de elementos a trabajar.
        minPeso: Límite inferior para los pesos de los objetos para la mochila.
        maxPeso: Límite superior para asignar los pesos de los elementos.
        minBeneficio: Valor mínimo que puede tener de beneficio un elemento.
        maxBeneficio: Número máximo para el beneficio de los elementos.
        minCantidad: Mínima cantidad disponible de un elemento.
        maxCantidad: Máxima cantidad disponible para un objeto para la mochila.
    *Ejemplo: python3 generator.py 1 salida.txt 50 3 5 15 20 60 3 4

    - Si se necesitan problemas de alineamiento de secuencias será:
        largoH1 largoH2

        largoH1: Largo específico de la primera secuencia.
        
        largoH2: Largo de la segunda secuencia.

    *Ejemplo: python3 generator.py 2 salida.txt 10 10

### Salida del programa:
La salida en ambos casos será un archivo .txt capaz de ser utilizado como entrada en el programa solver.py
de este mismo proyecto.
