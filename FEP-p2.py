import numpy as np
import matplotlib.pyplot as plt


## PWM Inverter

print("\n\n\n PWM Inverter")
VinPico = 800
VoutRMS = 565.68
Pout = 30000
fs = 30000 #FET


# power losses in components

# dados fet
rds_on_fet = 0.030
ids_fet = 22.23 # ver na simulação valor RMS

power_dissip_fet = rds_on_fet * (ids_fet ** 2)


print('power dissip fet', power_dissip_fet)

tri = 9 * 10 ** (-9) # datasheet
tfv = 15 * 10 ** (-9) # datasheet
ton_fet = tri + tfv
Eon = ids_fet * VinPico * ton_fet / 2
Pon = Eon * fs

trv = 24 * 10 ** (-9) # datasheet
tfi = 9 * 10 ** (-9) # datasheet
toff_fet = trv + tfi
Eon = ids_fet * VinPico * toff_fet / 2
Poff = Eon * fs

print('power on fet', Pon)
print('power off fet', Poff)

print('Total fet comutation losses', Poff + Pon)

total_losses = power_dissip_fet + Poff + Pon
print("Total Losses 1 fet:", total_losses)
print("Total Losses x6 fet:", 6*total_losses)
print("Eficienty:", Pout/(3*total_losses+Pout))

# thermal project

Rjc = 0.52 # °C/W

# Selected heat sink: OMNI-UNI-27-50 (2 FET POR HEAT SINK) https://br.mouser.com/datasheet/2/433/omniKlip_Wakefield_Vette_Data_Sheet-1500651.pdf
# Thermal Paste: https://www.thermaltake.com/tg-50-thermal-compound.html

Rdc = 0.0035/(8.38*2.7) # °C/W
Rhs_ca = 0.8 # °C/W

Rja = (Rhs_ca+Rdc+Rjc) # °C/W

Tjmax = 150*0.9
Tamb = 80

RjaMax = (Tjmax-Tamb)/(total_losses) # °C/W

print('\nProjeto Térmico')
print('Rja Máximo', RjaMax)
print('Rdc Obtido',Rdc)
print('Rja Obtido',Rja)

