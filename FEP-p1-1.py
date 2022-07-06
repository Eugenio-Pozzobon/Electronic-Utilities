import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# BOOST BCM PFC

Pav = 1500

Peak = 2 * Pav

E1 = 250
E1peak = np.sqrt(2) * E1
print('Peak value of the input voltage E1=', E1peak, 'V')
print('Peak value of the input voltage E1=100rms ', 100 * np.sqrt(2), 'V')
E2 = 400

fsw_min = 25000
print('Minimum switching frequency fsw_min=', fsw_min / 1000, 'kHz')

L = E1peak ** 2 * (E2 - E1peak) / (2 * E2 * Peak * fsw_min)
ton = (E2 - E1peak) / (E2 * fsw_min)
ton_100V = 2 * Peak * L / ((100 * np.sqrt(2)) ** 2)
print('L=', L * 10 ** 6, 'uH')
print('ton=', ton * 10 ** 6, 'u')
print('ton @100V=', ton_100V * 10 ** 6, 'u')

Icap_120_peak = Pav / E2
print('Iac_120_peak=', Icap_120_peak, 'A')

Ripple_120 = 0.025
Vac_120 = Ripple_120 * E2
C = Icap_120_peak / (2 * np.pi * 120 * Ripple_120 * E2)
R = E2 * E2 / Pav
print('Output Capacitance C=', C * 10 ** 6, 'uF')
print('R=', R, 'ohms')
print('Vac_120=', Vac_120, 'V peak')

print("\n\n Filtro de Entrada")

fsfilter = fsw_min / 10

Iin = Pav / E1
Rin = .2
Cin = Iin / (2 * np.pi * Rin * fsw_min * 100)
Lin = 1 / (Cin * pow(2 * np.pi * fsfilter, 2))

print('Cin', Cin * 1000000, 'u')
print('Lin', Lin * 1000000, 'u')

print('Ffiltro', 1 / (np.sqrt(Cin * Lin) * 2 * np.pi))

print('\n\n\n')

# power losses in components

# dados fet
rds_on_fet = 0.022
ids_fet = 3.6 # ver na simulação valor RMS

# dados diodo
ids_diode_avg = 2.87 # ver na simulação
ids_diode_rms = 5.22 # ver na simulação

# diodo boost
ids_diode_avg_boost = 2.87 # ver na simulação
ids_diode_rms_boost = 5.22 # ver na simulação

diode_boost_voltage_drop = 0.98+Icap_120_peak*0.04
diode_resistence = 0.04

print('diode_boost_voltage_drop', diode_boost_voltage_drop)

diode_rect_voltage_drop = 0.98+ids_diode_avg*0.04
print('diode_rect_voltage_drop', diode_rect_voltage_drop)

power_dissip_fet = rds_on_fet * (ids_fet ** 2)
power_dissip_diode_bulk = diode_resistence * (ids_diode_avg_boost ** 2) + diode_boost_voltage_drop * ids_diode_avg_boost
power_dissip_diode_rect = diode_resistence * (ids_diode_rms ** 2) + diode_rect_voltage_drop * ids_diode_avg

print('power dissip fet', power_dissip_fet)

print('power dissip boost diode', power_dissip_diode_bulk)
print('total power dissip rect-diode', 4 * power_dissip_diode_rect)

total_dissipation_power = power_dissip_fet + 4 * power_dissip_diode_rect + power_dissip_diode_bulk
print('total power dissipation', total_dissipation_power)

tri = 18 * 10 ** (-9) # datasheet
tfv = 24 * 10 ** (-9) # datasheet
ton_fet = tri + tfv
Eon = ids_fet * E2 * ton_fet / 2
Pon = Eon * fsw_min

trv = 48 * 10 ** (-9) # datasheet
tfi = 13 * 10 ** (-9) # datasheet
toff_fet = trv + tfi
Eon = ids_fet * E2 * toff_fet / 2
Poff = Eon * fsw_min

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
print("Eficienty:", Pav/(total_losses+Pav))
