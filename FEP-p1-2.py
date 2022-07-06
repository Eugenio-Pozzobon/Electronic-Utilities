import numpy as np
import matplotlib.pyplot as plt


## Flyback CCM

print("\n\n\n FLYBACK CCM")
Vin1 = 400
Vout1 = 120
rippleMaxOutput = 1
Pout1 = 1500
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


# power losses in components

# dados fet
rds_on_fet = 0.022
ids_fet = 5.5 # ver na simulação valor RMS

# dados diodo
ids_diode_avg = 12.17 # ver na simulação
ids_diode_rms = 12.17 # ver na simulação
diode_voltage_drop = 0.98+ids_diode_avg*0.04
diode_bulk_resistence = 0.04

print('diode_voltage_drop', diode_voltage_drop)
power_dissip_fet = rds_on_fet * (ids_fet ** 2)
power_dissip_diode = diode_bulk_resistence * (ids_diode_rms ** 2) + diode_voltage_drop * ids_diode_avg

print('power dissip diode', power_dissip_diode)
print('power dissip fet', power_dissip_fet)

total_dissipation_power = power_dissip_fet + power_dissip_diode
print('total power dissipation', total_dissipation_power)

tri = 18 * 10 ** (-9) # datasheet
tfv = 24 * 10 ** (-9) # datasheet
ton_fet = tri + tfv
Eon = ids_fet * VS1 * ton_fet / 2
Pon = Eon * fs

trv = 48 * 10 ** (-9) # datasheet
tfi = 13 * 10 ** (-9) # datasheet
toff_fet = trv + tfi
Eon = ids_fet * VS1 * toff_fet / 2
Poff = Eon * fs

print('power on fet', Pon)
print('power off fet', Poff)

print('Total fet comutation losses', Poff + Pon)

# tb_diode = 0
# IRR_diode = 0
# Cap_Rev_Diode = 0
# ReverseVoltage = 0
#
# PowerComLossDiodeConv = 1 / 2 * Cap_Rev_Diode * ReverseVoltage ** 2 * fsw_min + 1 / 6 * IRR_diode * ReverseVoltage * tb_diode * fsw_min
#
# print('power comutation losses in diode', PowerComLossDiodeConv)

total_losses = total_dissipation_power + Poff + Pon
print("Total Losses:", total_losses)
print("Eficienty:", Pout1/(total_losses+Pout1))