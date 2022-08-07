import numpy as np
import matplotlib.pyplot as plt


## PWM Inverter

print("\n\n\n FLYBACK CCM")
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
print("Eficienty:", Pout/(6*total_losses+Pout))