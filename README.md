# Laboratorio 4 Procesamiento de señales: Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet 
Autores: Fabián Alberto López Lemus y Tania Angélica Sandoval Ramírez
## Introducción
El propósito de este laboratorio es analizar la variabilidad de la frecuencia cardíaca (HRV) utilizando la transformada wavelet para identificar cambios en las frecuencias características y analizar la dinámica temporal de la señal cardíaca. Esto teniendo en cuenta caracteristicas del entorno en el que sera tomada la señal y lo que indican las caracteristicas de esta:
### Actividad simpática y parasimpática del sistema nervioso autónomo
  * **Actividad Simpática**: Prepara al cuerpo para situaciones de "lucha o huida". Libera neurotransmisores como la noradrenalina, lo que aumenta la frecuencia cardíaca, la presión arterial y la dilatación de las pupilas. Esto ocurre, por ejemplo, durante el estrés o el         ejercicio intenso.
  * **Actividad Parasimpática**: Promueve el estado de "reposo y digestión". Se activa en situaciones de calma y se asocia con la liberación de acetilcolina, lo que reduce la frecuencia cardíaca y promueve la digestión y la relajación.
### Efecto de la actividad simpática y parasimpática en la frecuencia cardiaca
  El efecto de la actividad **simpatica** incrementa la frecuencia cardíaca y la contractilidad del corazón, por otro lado la actividad **parasimpatica** disminuye la frecuencia cardíaca, facilitando un estado de calma y recuperación.
### Variabilidad de la frecuencia cardiaca (HRV)
 Se refiere a las fluctuaciones en el intervalo R-R (el tiempo entre latidos sucesivos del corazón). Un alto nivel de HRV indica una buena capacidad de adaptación del sistema nervioso y un equilibrio entre las actividades simpáticas y parasimpáticas, tiene frecuencias de  interes: 
  * **Baja Frecuencia (LF)**: Asociada con la actividad simpática.
  * **Alta Frecuencia (HF)**: Asociada con la actividad parasimpática.
  * La relación LF/HF puede indicar el balance entre ambas actividades.
### Transformada Wavelet 
 La transformada wavelet es una herramienta matemática utilizada para analizar señales en diferentes escalas de tiempo y frecuencia. Se aplica en el análisis de señales biológicas, como la ECG, para estudiar variaciones en la frecuencia cardíaca, detectar anomalías, y     descomponer señales complejas en componentes más simples, tiene los siguientes tipos de interes: 
  * **Wavelets de Daubechies**: Las wavelets de Daubechies son una familia de wavelets que se caracterizan por su buena resolución temporal y frecuencial, definidas por un número específico de coeficientes polinómicos. Su estructura ortogonal permite descomponer señales    sin    pérdida de información, lo que las hace especialmente útiles en el análisis de señales no estacionarias, como el ECG.
    
    <img src="https://github.com/user-attachments/assets/aa065fac-adeb-45ef-9ee0-3ceabdf676df" alt="Descripción de la imagen" width="500"/>

  * **Wavelets de Haar**: Las wavelets de Haar son las más simples y se basan en funciones escalonadas que representan cambios abruptos en una señal. Aunque su resolución temporal es limitada, son fáciles de implementar y se utilizan comúnmente en la detección de           discontinuidades, así como en aplicaciones de compresión de datos y análisis de imágenes.

     <img src="https://github.com/user-attachments/assets/852f21f5-d7b2-49bd-abc1-ddcffe1af9d9" alt="Descripción de la imagen" width="500"/>

  * **Wavelets de Morlet**: La wavelet de Morlet combina una onda sinusoidal con una envolvente gaussiana, ofreciendo buena resolución en tiempo y frecuencia. Son ideales para el análisis de señales biomédicas, permitiendo identificar patrones oscilatorios y captar tanto   información temporal como frecuencial, lo que las convierte en una herramienta valiosa en el estudio de la variabilidad de la frecuencia cardíaca.

     <img src="https://github.com/user-attachments/assets/c21c7bd4-cde8-42d2-a2c5-030ce8bf3516" alt="Descripción de la imagen" width="500"/>


Para la adquisición de la señal, se utilizó un sensor AD8232, junto con un ARDUINO para realizar la conversión analógica-digital (ADC) de la señal y transferir los datos al entorno de Python. El análisis de la señal se realizó utilizando Python, donde se importaron, visualizaron y procesaron los datos.

**Recomendaciones para terceros:** Se recomienda el software "Anaconda Navigator" con su herramienta "Spyder" para el análisis en Python. Al final de este repositorio, se incluyen las instrucciones detalladas para la correcta utilización del código.

**_El paciente del que se obtuvieron los datos, ha autorizado su uso y distribución_**

## Procedimiento 

### Primera parte

Ya una vez que se hizo la investigación teórica, se realizó un diagrama de flujo como se puede ver en la imágen que describe todo el procedimiento del laboratorio, en donde al principio se captura la señal de ECG durante un periodo de 5 minutos a una frecuencia de muestreo de 1500 Hz para obtener una señal suficientemente detallada, la señal capturada se pasa a través de un filtro pasa bajo con una frecuencia de corte de 10 Hz. Este filtro elimina las frecuencias más altas para reducir el ruido y centrarse en el rango de interés para el análisis de frecuencia cardíaca. Después, la señal se pasa por un filtro pasa alto con una frecuencia de corte de 150 Hz, este filtro elimina las componentes de frecuencia no deseadas. A partir de la señal filtrada, se detectan los intervalos R-R (tiempo entre picos R consecutivos en el ECG). Estos intervalos son esenciales para calcular la variabilidad de la frecuencia cardíaca. Se calculan la media y la desviación estándar de los intervalos R-R para obtener medidas de la variabilidad de la frecuencia cardíaca en el dominio del tiempo, complementando el análisis en el dominio de frecuencia. Se aplica la transformada wavelet continua (CWT) para obtener una representación en el dominio del tiempo-frecuencia de la señal, lo que permite identificar las variaciones de frecuencia en el tiempo. Los coeficientes de la CWT se utilizan para dividir la señal en dos: la de baja Frecuencia (0.04-0.15 Hz), asociada con la actividad simpática y la alta Frecuencia (0.15-0.4 Hz), asociada con la actividad parasimpática. Finalmente, se realiza una comparación de los resultados obtenidos de ambos dominios (tiempo y frecuencia) para analizar y evaluar el estado de la actividad autónoma del corazón (actividad simpática y parasimpática).


<img src="https://github.com/user-attachments/assets/7013e1ca-2999-40ee-9a1e-43c8435c57c1" alt="Descripción de la imagen" width="500"/>

### Segunda parte

Se usaron unos electrodos superficiales que estaban en una configuración como se muestra en la imágen (capturando la señal del corazón ) que estan conectados al sensor AD8232 y este tiene 3 PINES conectados al ARDUINO, uno para los 3.3V del sensor, otro GROUND del sensor y el último esta conectado al OUTPUT del sensor.

![image](https://github.com/user-attachments/assets/67966a6d-6c70-4438-ab34-38bc9ad8634b)

### Tercera parte

Para poder recoger los datos de la señal se realizó un programa "ECG.ino" para que captura una frecuencia de muestreo de 1000 Hz ya que las señales ECG se encuentran en 150 Hz, y como dice el teorema de muestreo de Nyquist la frecuencia de muestreo debe ser mayor que el doble del de interés de frecuencia más alta en la señal medida.

En ARDUINO, ese valor de 1000 microsegundos representa el periodo (T) entre cada muestra para una frecuencia de muestreo de aproximadamente 1000 Hz

```c++
delayMicroseconds(1000);
```

### Cuarta parte
Despúes se realizó un programa de python "Toma_Datos.py" en donde se conecta a un puerto serie configurado a 500,000 baudios y durante 300 segundos lee continuamente los datos disponibles, imprimiéndolos y guardándolos en un archivo de texto. Luego, cierra el puerto serie una vez completada la operación. Se estableció el puerto de comunicación COM4  y una velocidad de transmisión de 500,000 baudios. Duerante este tiempo el paciente estuvo hablando y riendo.
```python
com_port = 'COM4'
baud_rate = 500000
duration = 300  
```
Se abre un archivo llamado datos.txt para almacenar los datos recibidos.
```python
with open('datos.txt', 'w') as file:
```
Al finalizar la captura de datos, se cierra la conexión del puerto serie.
```python
ser.close()
print("Lectura completada y datos guardados en 'datos_ecg.txt'.")
```

### Quinta parte
El código "Lab_3_ Señales.py" se importaron las librerías necesarias para el procesamiento de señales, análisis estadístico y graficación.
```python
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pywt
```
