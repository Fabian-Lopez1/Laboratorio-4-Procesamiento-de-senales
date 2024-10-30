# Laboratorio 4 Procesamiento de señales: Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet 
Autores: Fabián Alberto López Lemus y Tania Angélica Sandoval Ramírez
## Introducción
El propósito de este laboratorio es analizar la variabilidad de la frecuencia cardíaca (HRV) utilizando la transformada wavelet para identificar cambios en las frecuencias características y analizar la dinámica temporal de la señal cardíaca. Esto teniendo en cuenta caracteristicas del entorno en el que sera tomada la señal y lo que indican las caracteristicas de esta:
### Actividad simpática y parasimpática del sistema nervioso autónomo
  * **Actividad Simpática**: Prepara al cuerpo para situaciones de "lucha o huida". Libera neurotransmisores como la noradrenalina, lo que aumenta la frecuencia cardíaca, la presión arterial y la dilatación de las pupilas. Esto ocurre, por ejemplo, durante el estrés o el         ejercicio intenso.
  * **Actividad Parasimpática**: Promueve el estado de "reposo y digestión". Se activa en situaciones de calma y se asocia con la liberación de acetilcolina, lo que reduce la frecuencia cardíaca y promueve la digestión y la relajación.
### Efecto de la actividad simpática y parasimpática en la frecuencia cardiaca
  El efecto de la actividad **simpatica** incrementa la frecuencia cardíaca y la contractilidad del corazón, por otro lado la actividad **parasimpatica** disminuye la frecuencia cardíaca, facilitando un estado de calma y recuperación.
###Variabilidad de la frecuencia cardiaca (HRV)
 Se refiere a las fluctuaciones en el intervalo R-R (el tiempo entre latidos sucesivos del corazón). Un alto nivel de HRV indica una buena capacidad de adaptación del sistema nervioso y un equilibrio entre las actividades simpáticas y parasimpáticas, tiene frecuencias de  interes: 
  * **Baja Frecuencia (LF)**: Asociada con la actividad simpática.
  * **Alta Frecuencia (HF)**: Asociada con la actividad parasimpática.
  * La relación LF/HF puede indicar el balance entre ambas actividades.
### Transformada Wavelet 
 La transformada wavelet es una herramienta matemática utilizada para analizar señales en diferentes escalas de tiempo y frecuencia. Se aplica en el análisis de señales biológicas, como la ECG, para estudiar variaciones en la frecuencia cardíaca, detectar anomalías, y     descomponer señales complejas en componentes más simples, tiene los siguientes tipos de interes: 
  * **Wavelets de Daubechies**: Las wavelets de Daubechies son una familia de wavelets que se caracterizan por su buena resolución temporal y frecuencial, definidas por un número específico de coeficientes polinómicos. Su estructura ortogonal permite descomponer señales    sin    pérdida de información, lo que las hace especialmente útiles en el análisis de señales no estacionarias, como el ECG.
  * **Wavelets de Haar**: Las wavelets de Haar son las más simples y se basan en funciones escalonadas que representan cambios abruptos en una señal. Aunque su resolución temporal es limitada, son fáciles de implementar y se utilizan comúnmente en la detección de           discontinuidades, así como en aplicaciones de compresión de datos y análisis de imágenes.
  * **Wavelets de Morlet**: La wavelet de Morlet combina una onda sinusoidal con una envolvente gaussiana, ofreciendo buena resolución en tiempo y frecuencia. Son ideales para el análisis de señales biomédicas, permitiendo identificar patrones oscilatorios y captar tanto   información temporal como frecuencial, lo que las convierte en una herramienta valiosa en el estudio de la variabilidad de la frecuencia cardíaca.

Para la adquisición de la señal, se utilizó un sensor AD8232, junto con un ARDUINO para realizar la conversión analógica-digital (ADC) de la señal y transferir los datos al entorno de Python. El análisis de la señal se realizó utilizando Python, donde se importaron, visualizaron y procesaron los datos.

**Recomendaciones para terceros:** Se recomienda el software "Anaconda Navigator" con su herramienta "Spyder" para el análisis en Python. Al final de este repositorio, se incluyen las instrucciones detalladas para la correcta utilización del código.
