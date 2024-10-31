from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pywt  
from mpl_toolkits.mplot3d import Axes3D


# Leer los datos desde el archivo de texto
ecg_signal = np.loadtxt('datos2.txt')

# Especificar la frecuencia de muestreo manualmente
fs = 1000  

# Filtro Butterworth
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

# Filtro de 10 Hz - 150 Hz
lowcut = 10.0
highcut = 150.0
filtered_ecg = apply_filter(ecg_signal, lowcut, highcut, fs)

time = np.linspace(0, 300, len(ecg_signal))
limit=300
# Graficar la señal original y la señal filtrada
plt.figure(figsize=(12, 6))

#señal original
plt.subplot(2, 1, 1)
plt.plot(time, ecg_signal, label='Señal Original', color='blue')
plt.title('Señal ECG Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0, limit)
plt.legend()

# señal filtrada
plt.subplot(2, 1, 2)
plt.plot(time, filtered_ecg, label='Señal Filtrada', color='red')
plt.title('Señal ECG Filtrada (10 Hz - 150 Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0, limit)  
plt.legend()

plt.tight_layout()
plt.show()

Amplitud_picos = 500  # Ajustar este valor teniendo en cuenta el valor medio de los picos R 

# Deteccion de picos
distancia_estimada = int(fs * 0.4) #distancia mínima entre picos
peaks, _ = find_peaks(filtered_ecg, distance= distancia_estimada, height=Amplitud_picos)

#picos detectados
r_peaks_time = time[peaks]

# Grafica picos R detectados
plt.figure(figsize=(12, 6))
plt.plot(time, filtered_ecg, label='Señal Filtrada', color='red')
plt.plot(r_peaks_time, filtered_ecg[peaks], 'o', label='Picos R detectados', color='green')
plt.title('Detección de Picos R en la Señal Filtrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0, limit)
plt.legend()
plt.show()

#intervalos RR
rr_intervals = np.diff(r_peaks_time)
#print("Intervalos R-R (en segundos):", rr_intervals)

print("Cantidad total de intervalos R-R detectados:", len(rr_intervals))

print("Intervalo R-R (en segundos):")
print("-" * 30)

for i, interval in enumerate(rr_intervals, start=1):
    print(f"Intervalo {i}: {interval:.3f} s")

print("-" * 30)

#HRV

# Media y desviacion estardar de intervalos R-R
media = np.mean(rr_intervals)
desviacion = np.std(rr_intervals)

print("Media de los intervalos R-R:", media)
print("Desviación estándar de los intervalos R-R:", desviacion)

filtered_ecg = np.ravel(filtered_ecg)


rr_intervals = [0.990, 1.008, 1.032, 1.050, 1.066, 1.017, 0.980, 0.980, 0.978, 0.975, 0.996, 0.997, 1.389, 1.050, 1.080, 1.081, 1.043, 1.277, 0.973, 1.004, 1.008, 0.829, 1.022, 1.067, 1.062, 1.066, 1.017, 1.024, 1.034, 1.020, 0.891, 1.094, 1.025, 1.031, 1.402, 1.048, 1.034, 1.034, 0.910, 1.006, 0.985, 0.957, 0.961, 1.249, 1.192, 1.171, 1.115, 0.996, 0.999, 1.004, 1.017, 1.137, 1.020, 0.996, 0.957, 1.480, 0.961, 0.962, 0.962, 1.062, 1.143, 1.120, 1.074, 1.839, 1.123, 1.123, 1.102, 1.452, 0.989, 1.006, 1.844, 1.069, 1.050, 0.992, 1.055, 1.004, 1.011, 1.003, 1.368, 1.050, 1.050, 1.032, 1.487, 1.013, 1.015, 1.022, 1.342, 0.889, 0.905, 1.048, 0.978, 1.078]
# Crear vector de tiempo basado en los intervalos R-R
time_rr = np.cumsum(rr_intervals)
media_rr = np.mean(rr_intervals)

# Definir las escalas para cada banda de frecuencia
scales_lf = np.arange(7, 26)  # Aproximado para 0.04-0.15 Hz
scales_hf = np.arange(3, 7)   # Aproximado para 0.15-0.4 Hz

# Calcular coeficientes de CWT con una wavelet cmor1.5-1.0
wavelet = 'cmor1.5-1.0'
coefficients_lf, frequencies_lf = pywt.cwt(rr_intervals, scales_lf, wavelet, sampling_period=media_rr)
coefficients_hf, frequencies_hf = pywt.cwt(rr_intervals, scales_hf, wavelet, sampling_period=media_rr)

# Visualización en 3D
fig = plt.figure(figsize=(12, 10))

# Gráfico 3D para banda LF
ax1 = fig.add_subplot(211, projection='3d')
T, F = np.meshgrid(time_rr, frequencies_lf)
amp_lf = np.abs(coefficients_lf) ** 2
ax1.plot_surface(T, F, amp_lf, cmap='viridis', edgecolor='none')
ax1.set_title("Coeficientes CWT en Banda LF (0.04-0.15 Hz)")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Frecuencia (Hz)")
ax1.set_zlabel("Amplitud")

# Gráfico 3D para banda HF
ax2 = fig.add_subplot(212, projection='3d')
T, F = np.meshgrid(time_rr, frequencies_hf)
amp_hf = np.abs(coefficients_hf) ** 2
ax2.plot_surface(T, F, amp_hf, cmap='plasma', edgecolor='none')
ax2.set_title("Coeficientes CWT en Banda HF (0.15-0.4 Hz)")
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Frecuencia (Hz)")
ax2.set_zlabel("Amplitud")

plt.tight_layout()
plt.show()
