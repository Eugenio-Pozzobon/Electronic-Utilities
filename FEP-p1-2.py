import numpy as np
import matplotlib.pyplot as plt

Vin1 = 400
Vout1 = 120
rippleMaxOutput = 1
Pout1 = 3000
fs = 20000 #FET

N1 = 33
N2 = 10
D1 = 1 / ((Vin1 / Vout1) * (N2 / N1) + 1)
M1 = (D1 / (1 - D1)) * (N2 / N1)
print('D=', D1)
print('M=', M1)

# Curva de Ganho Estático

d = np.linspace(0, 0.5, 100)
gain = (d / (1 - d)) * (1 / 3)
plt.grid()
plt.plot(d, gain, 'b.')
plt.xlabel('Razão Cíclica (D)')
plt.ylabel('Ganho Estático (M)')
plt.title('Ganho Estático do Conversor Flyback em CCM para N = 0.33')

# Resistência de Carga e Corrente de Saída

R1 = (Vout1 * Vout1) / Pout1
print('R=', R1, 'ohms')
Iout1 = Vout1 / R1
print('Iout=', Iout1, 'A')

# tensão sobre a chave

VS1 = Vin1 + Vout1 * (N1 / N2)
print('VS=', VS1, 'V')

# MOSFET

T = 1 / fs
print(' fs=', fs / 1000, 'kHz')
print(' T=', T * 10 ** 6, 'us')
t1 = np.linspace(0, 2 * T, 1000)
ts1 = t1 < D1 * T
ts2 = (t1 >= D1 * T) * (t1 < T)
ts3 = (t1 > T) * (t1 < (D1 * T + T))
ts4 = (t1 > T) * (t1 > (D1 * T + T))
vag = 1 * ts1 + 0 * ts2 + 1 * ts3 + 0 * ts4

plt.grid()
plt.plot(t1 * 10 ** 6, Vin1 * vag, 'r')
plt.xlabel('t (us)')
plt.ylabel('vgs (V)')
plt.title('MOSFET gate source voltage')

# Corrente Média de Magnetização e Corrente Média de Entrada do Conversor

Iin1 = (Vout1 * Vout1) / (Vin1 * R1)
ILm1 = (Vout1 * Vout1) / (Vin1 * R1 * D1)
print('Iin=', Iin1, 'A')
print('ILm=', ILm1, 'A')

# Valores de $L_1$, $L_2$ e $L_M$

AiL_perc1 = 50 / 100
AiL1 = ILm1 * AiL_perc1
L11 = (Vin1 * D1) / (AiL1 * fs)
L22 = (L11 * ((N2 * N2) / (N1 * N1)))
LMM = 0.99999 * (np.sqrt((L11) * (L22)))
print('Variação de Corrente em L1=', AiL1, 'A')
print('L1=', L11 * 10 ** 6, 'uH')
print('L2=', L22 * 10 ** 6, 'uH')
print('LM=', LMM * 10 ** 6, 'uH')

# correntre max e min no indutor

Imax = ILm1 + (AiL1 / 2)
Imin1 = ILm1 - (AiL1 / 2)
print('Imáxima=', Imax, 'A')
print('Imínima=', Imin1, 'A')

# valor do capacitor da saída

AvC1 = rippleMaxOutput / 100
C1 = D1 / (AvC1 * R1 * fs)
print('C=', C1 * 10 ** 6, 'uF')
