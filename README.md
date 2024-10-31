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
El código "Lab_4_ Señales.py" se importaron las librerías necesarias para el procesamiento de señales, análisis estadístico y graficación.
```python
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pywt
```
La librería de scipy.signal, contiene funciones para procesar señales, como el filtrado y la detección de picos. La de matplotlib.pyplot, se usa para graficar los resultados y la de pywt ayuda para transformadas wavelet.

### Sexta parte

Se hace la lectura de la Señal y se define la Frecuencia de Muestreo.

```python
ecg_signal = np.loadtxt('datos2.txt')
fs = 1000
```
### Séptima parte

Se define un filtro pasa banda de Butterworth para filtrar la señal entre 10 Hz y 150 Hz. Y se crean dos funciones butter_bandpass para calcular los coeficientes del filtro y apply_filter para aplicar el filtro a la señal.

```python
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_filter(data, lowcut, highcut, fs):
    b, a = butter_bandpass(lowcut, highcut, fs, order=4)
    y = filtfilt(b, a, data)
    return y
```
Se definieron los valores del filtro pasabanda con:
-3 dB de atenuación en 10 Hz y 450 Hz.
-20 dB de atenuación en 2.5Hz y 5 KHz.

<img src="https://github.com/user-attachments/assets/0577f77c-ebbb-40c6-aebf-ef738c78662a" alt="Descripción de la imagen" width="400"/>

Y se calcularon las frecuencias características del filtro convirtiendolas a radianes por segundo:

Ω1=2𝜋×5Hz=31.416 rad/s

Ω2=2𝜋×300Hz=1884.96 rad/s

Ω𝐿=2𝜋×10Hz=62.83 rad/s

Ωu=2𝜋×150Hz=942.478rad/s

Después se calcularon A y 𝐵 para conocer la frecuencia del paso bajo:

$$A=\frac{\Omega_{1}^2 - \Omega_{L}\Omega_{u}}{\Omega_{1}(\Omega_{u} - \Omega_{L})}$$

$$B=\frac{\Omega_{2}^2 - \Omega_{L}\Omega_{u}}{\Omega_{2}(\Omega_{u} - \Omega_{L})}$$

El valor de A da un resultado de 2,052 y el valor de B da un resultado de 2,052, entonces se toma el valor de 2,052:

$$
n = \frac{\log_{10} \left( \frac{10^{(k1/10)}-1}{10^{(k2/10)}-1} \right)}{2 \log_{10} \left( \frac{ \Omega_{1}}{ \Omega_{2}} \right)} = 3,199
$$


Dando como resultado que el orden del filtro sea 4. Debido a esto se va a escoger un polimio característico como se puede observar en el código de MATLAB "filtro_pasabanda.m":
```matlab
H_original = 1 / ((s^2 + 0.76536*s + 1) * (s^2 + 1.84776*s + 1));
```
Se crea una transformación para 𝑠. En donde se va a  reemplazar la variable s en la función de transferencia original que se mostró anteriormente.

```matlab
s_subs = (s^2 + 59215.89274) / (879.648 * s);
```

Y se gráfico para combrobar que los valores establecidos si se cumplieran.

![image](https://github.com/user-attachments/assets/69d9e6a9-106c-4350-bfc9-f57bc5dc8158)


### Octava parte
Vamos a visualizar la señal original y filtrada.

```python
plt.figure(figsize=(12, 6))

# Señal original
plt.subplot(2, 1, 1)
plt.plot(time, ecg_signal, label='Señal Original', color='blue')

# Señal filtrada
plt.subplot(2, 1, 2)
plt.plot(time, filtered_ecg, label='Señal Filtrada', color='red')
plt.show()

```
Primero la vamos a observar con una duración de 20 segundos para poder observar la forma de la señal:

![image](https://github.com/user-attachments/assets/5c962ccc-1260-4c2d-b976-62e94f5bb680)

Ahora, en esta imágen ya vemos como se ve durante esos 5 minutos:

![image](https://github.com/user-attachments/assets/1d7f7ad8-26eb-4d0a-9d9b-ae0f302541c5)

La señal tiene un rango de amplitud entre aproximadamente 1000 y 4000 en la señal sin filtrar, y entre -1000 y 1500 en la señal filtrada, la señal filtrada muestra un rango de frecuencias de 10 a 150 Hz, eliminando el ruido de baja frecuencia y frecuencias superiores que no son relevantes para el análisis de picos R.

### Novena parte
Detectamos los picos R en la señal filtrada.

```python
Amplitud_picos = 500
distancia_estimada = int(fs * 0.4)
peaks, _ = find_peaks(filtered_ecg, distance=distancia_estimada, height=Amplitud_picos)

# Obtener tiempos de los picos R
r_peaks_time = time[peaks]
```
find_peaks, detecta de picos con una separación mínima (distance) y un valor mínimo (height).

### Décima parte

Calculamos la diferencia entre tiempos de picos R (rr_intervals), dando los intervalos R-R, también calculamos la media y desviación estándar de los intervalos R-R.

```python
rr_intervals = np.diff(r_peaks_time)
media = np.mean(rr_intervals)
desviacion = np.std(rr_intervals)
```
Dandonos los valores de:

Cantidad total de intervalos R-R detectados: 92

------------------------------
Intervalo 1: 0.990 s


Intervalo 2: 1.008 s

Intervalo 3: 1.032 s

Intervalo 4: 1.050 s

Intervalo 5: 1.066 s

Intervalo 6: 1.017 s

Intervalo 7: 0.980 s

Intervalo 8: 0.980 s

Intervalo 9: 0.978 s

Intervalo 10: 0.975 s

Intervalo 11: 0.996 s

Intervalo 12: 0.997 s

Intervalo 13: 1.389 s

Intervalo 14: 1.050 s

Intervalo 15: 1.080 s

Intervalo 16: 1.081 s

Intervalo 17: 1.043 s

Intervalo 18: 1.277 s

Intervalo 19: 0.973 s

Intervalo 20: 1.004 s

Intervalo 21: 1.008 s

Intervalo 22: 0.829 s

Intervalo 23: 1.022 s

Intervalo 24: 1.067 s

Intervalo 25: 1.062 s

Intervalo 26: 1.066 s

Intervalo 27: 1.017 s

Intervalo 28: 1.024 s

Intervalo 29: 1.034 s

Intervalo 30: 1.020 s

Intervalo 31: 0.891 s

Intervalo 32: 1.094 s

Intervalo 33: 1.025 s

Intervalo 34: 1.031 s

Intervalo 35: 1.402 s

Intervalo 36: 1.048 s

Intervalo 37: 1.034 s

Intervalo 38: 1.034 s

Intervalo 39: 0.910 s

Intervalo 40: 1.006 s

Intervalo 41: 0.985 s

Intervalo 42: 0.957 s

Intervalo 43: 0.961 s

Intervalo 44: 1.249 s

Intervalo 45: 1.192 s

Intervalo 46: 1.171 s

Intervalo 47: 1.115 s

Intervalo 48: 0.996 s

Intervalo 49: 0.999 s

Intervalo 50: 1.004 s

Intervalo 51: 1.017 s

Intervalo 52: 1.137 s

Intervalo 53: 1.020 s

Intervalo 54: 0.996 s

Intervalo 55: 0.957 s

Intervalo 56: 1.480 s

Intervalo 57: 0.961 s

Intervalo 58: 0.962 s

Intervalo 59: 0.962 s

Intervalo 60: 1.062 s

Intervalo 61: 1.143 s

Intervalo 62: 1.120 s

Intervalo 63: 1.074 s

Intervalo 64: 1.839 s

Intervalo 65: 1.123 s

Intervalo 66: 1.123 s

Intervalo 67: 1.102 s

Intervalo 68: 1.452 s

Intervalo 69: 0.989 s

Intervalo 70: 1.006 s

Intervalo 71: 1.844 s

Intervalo 72: 1.069 s

Intervalo 73: 1.050 s

Intervalo 74: 0.992 s

Intervalo 75: 1.055 s

Intervalo 76: 1.004 s

Intervalo 77: 1.011 s

Intervalo 78: 1.003 s

Intervalo 79: 1.368 s

Intervalo 80: 1.050 s

Intervalo 81: 1.050 s

Intervalo 82: 1.032 s

Intervalo 83: 1.487 s

Intervalo 84: 1.013 s

Intervalo 85: 1.015 s

Intervalo 86: 1.022 s

Intervalo 87: 1.342 s

Intervalo 88: 0.889 s

Intervalo 89: 0.905 s

Intervalo 90: 1.048 s

Intervalo 91: 0.978 s

Intervalo 92: 1.078 s

------------------------------

Media de los intervalos R-R: 1.0766478473129355

Desviación estándar de los intervalos R-R: 0.16821923088165547



La media de los intervalos R-R (1.0766 s) equivale a una frecuencia cardíaca promedio de aproximadamente 56 latidos por minuto (bpm), en el contexto de un ECG normal, los intervalos R-R suelen ser de entre 0.6 y 1.2 segundos, lo que corresponde a una frecuencia cardíaca típica de entre 50 y 100 latidos por minuto.

La desviación estándar es de 0.1682 s, lo cual indica cierta variabilidad en los intervalos. Esto es generalmente positivo, pues una mayor variabilidad en reposo suele asociarse con una respuesta flexible del sistema nervioso autónomo y una buena salud cardiovascular.

Con esta señal, podríamos dividir los intervalos R-R en bandas de frecuencia LF (0.04-0.15 Hz) y HF (0.15-0.4 Hz) mediante un análisis de wavelet. La potencia en LF representa en general la actividad simparasimpática, mientras que HF se asocia a lo parasimpático. Al calcular la relación LF/HF.

Algunos intervalos son inusualmente largos, como los de 1.389 s, 1.402 s y 1.839 s, lo que podría indicar pausas o irregularidades en el ritmo. La media y desviación estándar de estos intervalos sugieren una posible influencia del sistema nervioso autónomo (tanto simpático como parasimpático). La presencia de intervalos largos y una frecuencia cardíaca baja podrían indicar una regulación más orientada hacia el tono parasimpático.

### Onceava parte

Se hace el análisis de frecuencia con CWT, en donde scales_lf define un rango de valores para la banda de baja frecuencia (LF), con coeficientes de 7 hasta 25. Estos valores están calibrados para abarcar aproximadamente el rango de frecuencia 0.04-0.15 Hz. Y los de scales_hf que definen un rango más bajo de escalas para la banda de alta frecuencia (HF), con coeficientes de de 3 a 6, que abarca aproximadamente 0.15-0.4 Hz.

```python
scales_lf = np.arange(7, 26)  # Aproximado para 0.04-0.15 Hz
scales_hf = np.arange(3, 7)   # Aproximado para 0.15-0.4 Hz
```
Se hace el cálculo de la Transformada de Wavelet Continua (CWT), se selecciona la wavelet compleja Morlet (cmor1.5-1.0) para realizar la CWT. Utilizando rr_intervals con las escalas scales_lf y el período de muestreo media_rr.

```python
wavelet = 'cmor1.5-1.0'
coefficients_lf, frequencies_lf = pywt.cwt(rr_intervals, scales_lf, wavelet, sampling_period=media_rr)
coefficients_hf, frequencies_hf = pywt.cwt(rr_intervals, scales_hf, wavelet, sampling_period=media_rr)

```
Dando la siguiente gráfica:

![image](https://github.com/user-attachments/assets/7423b337-e3f0-4bb4-afd8-faf8bf2e97d1)

Para este tipo de análisis, se usa la wavelet "cmor1.5-1.0" (Morlet compleja). Esta wavelet es adecuada para estudios de frecuencia cardíaca debido a su habilidad para capturar variaciones en la frecuencia y amplitud con alta resolución en el dominio del tiempo y frecuencia. La wavelet Morlet es particularmente útil en el análisis de señales biomédicas, ya que es simétrica y mantiene una buena representación de la fase y frecuencia.

En el primer gráfico (banda LF), la potencia espectral se concentra en frecuencias que varían entre 0.05 y 0.13 Hz. Observamos una tendencia general de la potencia a mantenerse estable en gran parte del tiempo, con picos ocasionales. La estabilidad de la potencia espectral en esta banda indica que hay consistencia en las variaciones lentas de la frecuencia cardíaca, que suelen estar relacionadas con la modulación simpática del sistema nervioso autónomo.

Hacia el final del periodo, parece haber un ligero aumento en la potencia en frecuencias más altas dentro de la banda LF (aproximadamente 0.12-0.13 Hz). Esto sugiere un incremento temporal en la actividad parasimpática, pero los cambios en esta banda son relativamente suaves y controlados.

En el segundo gráfico (banda HF), la potencia espectral varía de manera más abrupta, especialmente hacia el final del periodo. Las frecuencias dentro de la banda HF muestran picos altos de amplitud en momentos específicos. La potencia espectral es más alta en el rango de 0.2 a 0.3 Hz, con un aumento de actividad en ciertos puntos que puede representar una respuesta rápida en la modulación parasimpática del sistema cardíaco( como ocurre en los patrones de respiración).

A diferencia de la banda LF, la banda HF tiene variaciones más marcadas en la potencia espectral, lo que indica que durante este tiempo el sistema que esta tomando el control es el sistema nervioso parasimpático. 

Los gráficos muestran cómo las bandas LF y HF reflejan distintos aspectos de la variabilidad de la frecuencia cardíaca. La banda LF se mantiene relativamente estable con picos moderados, reflejando un control autónomo más constante. En cambio, la banda HF muestra cambios más pronunciados en la potencia espectral, indicando una respuesta rápida a factores externos o internos, como la respiración. Este análisis sugiere que el uso de la wavelet Morlet compleja es adecuado para capturar estas características dinámicas, proporcionando una buena representación de las variaciones en ambas bandas de frecuencia.

# Instrucciones para el usuario 

Se deberá cambiar la línea para cargar su archivo en el programa de "main.py".
```python
ecg_signal = np.loadtxt('nombre_de_la_señal.txt')
```
 La persona debe cambiar este valor según la frecuencia de muestreo de su propia señal. 
 ```python
fs = "frecuencia que se requiere"
```
Si la persona quiere analizar otro rango de frecuencias, teniendo en cuenta que si se cambia las condiciones del filtro pueden variar.
 ```python
lowcut = "frecuencia que se requiere"
highcut = "frecuencia que se requiere"
```


Por favor, cite este artículo:
<br>
Lopez L., Sandoval R. (2024). Github 'Laboratorio 3 Procesamiento de señales'[Online].
### Informacion de contacto
est.fabiana.lopez@unimilitar.edu.co
<br>
est.tania.sandoval@unimilitar.edu.co

