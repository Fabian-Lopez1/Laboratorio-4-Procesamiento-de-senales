from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pywt  
from scipy.interpolate import interp1d

# Leer los datos desde el archivo de texto
emg_signal = np.loadtxt('datos2.txt')

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
filtered_emg = apply_filter(emg_signal, lowcut, highcut, fs)

time = np.linspace(0, 300, len(emg_signal))
limit=300
# Graficar la señal original y la señal filtrada
plt.figure(figsize=(12, 6))

#señal original
plt.subplot(2, 1, 1)
plt.plot(time, emg_signal, label='Señal Original', color='blue')
plt.title('Señal ECG Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0, limit)
plt.legend()

# señal filtrada
plt.subplot(2, 1, 2)
plt.plot(time, filtered_emg, label='Señal Filtrada', color='red')
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
peaks, _ = find_peaks(filtered_emg, distance= distancia_estimada, height=Amplitud_picos)

#picos detectados
r_peaks_time = time[peaks]

# Grafica picos R detectados
plt.figure(figsize=(12, 6))
plt.plot(time, filtered_emg, label='Señal Filtrada', color='red')
plt.plot(r_peaks_time, filtered_emg[peaks], 'o', label='Picos R detectados', color='green')
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

filtered_emg = np.ravel(filtered_emg)

# Datos hipotéticos de intervalos R-R en segundos
rr_intervals = [ 2.971, 3.024, 3.097, 3.150, 3.197, 3.050, 2.940, 2.940, 2.934, 2.924, 2.987, 2.992, 4.168, 3.150, 3.239, 3.244, 3.129, 3.832, 2.919, 3.013, 3.024, 2.488, 3.066, 3.202, 3.186, 3.197, 3.050, 3.071, 3.102, 3.060, 2.672, 3.281, 3.076, 3.092, 4.205, 3.144, 3.102, 3.102, 2.730, 3.018, 2.955, 2.871, 2.882, 3.748, 3.575, 3.512, 3.344, 2.987, 2.997, 3.013, 3.050, 3.412, 3.060, 2.987, 2.871, 4.441, 2.882, 2.887, 2.887, 3.186, 3.428, 3.360, 3.223, 5.517, 3.370, 3.370, 3.307, 4.357, 2.966, 3.018, 5.533, 3.207, 3.150, 2.976, 3.165, 3.013, 3.034, 3.008, 4.105, 3.150, 3.150, 3.097, 4.462, 3.039, 3.045, 3.066, 4.026, 2.667, 2.714, 3.144, 2.934, 3.234]  # Inserta tus intervalos R-R aquí
media_rr = np.mean(rr_intervals)

# Crear vector de tiempo basado en los intervalos R-R
time_rr = np.cumsum(rr_intervals)

# Definir las escalas para cada banda de frecuencia
scales_lf = np.arange(70, 260)  # Aproximado para 0.04-0.15 Hz
scales_hf = np.arange(30, 70)   # Aproximado para 0.15-0.4 Hz

# Calcular coeficientes de CWT con una wavelet cmor1.5-1.0
wavelet = 'cmor1.5-1.0'

# Coeficientes y frecuencias para LF
coefficients_lf, frequencies_lf = pywt.cwt(rr_intervals, scales_lf, wavelet, sampling_period=media_rr)
# Coeficientes y frecuencias para HF
coefficients_hf, frequencies_hf = pywt.cwt(rr_intervals, scales_hf, wavelet, sampling_period=media_rr)

# Calcular la potencia promedio en cada banda
lf_power = np.mean(np.abs(coefficients_lf) ** 2)
hf_power = np.mean(np.abs(coefficients_hf) ** 2)

print(f"Potencia en la banda LF (0.04-0.15 Hz): {lf_power}")
print(f"Potencia en la banda HF (0.15-0.4 Hz): {hf_power}")

# Visualización (opcional)
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.imshow(np.abs(coefficients_lf), extent=[0, time_rr[-1], 0.15, 0.04], aspect='auto', cmap='jet')
plt.colorbar(label="Amplitud")
plt.title("Coeficientes CWT en Banda LF (0.04-0.15 Hz)")
plt.ylabel("Frecuencia (Hz)")

plt.subplot(2, 1, 2)
plt.imshow(np.abs(coefficients_hf), extent=[0, time_rr[-1], 0.4, 0.15], aspect='auto', cmap='jet')
plt.colorbar(label="Amplitud")
plt.title("Coeficientes CWT en Banda HF (0.15-0.4 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia (Hz)")

plt.tight_layout()
plt.show()