import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

## BCM

# Prated=200
# E1=200
# E2=400
# fsw_min=50*10**3
# Tmax=1/fsw_min
# print ( ' fsw at the nominal operation =', fsw_min/1000,'kHz')
# print ( ' Tmax=', Tmax*10**6,'us')
#
# ton=4.5*10**-6
# t1=np.linspace(0,2*Tmax,1000)
# ts1=t1<ton
# ts2=(t1>=ton)*(t1<Tmax)
# ts3=(t1>Tmax)*(t1<(ton+Tmax))
# ts4=(t1>Tmax)*(t1>(ton+Tmax))
# vag=1*ts1+0*ts2+1*ts3+0*ts4
# plt.grid()
# plt.plot(t1*10**6,15*vag,'r')
# plt.xlabel('t (us)')
# plt.ylabel('vgs (V)' )
# plt.title('MOSFET gate source voltage')
#
# # inductance value
#
# L=E1**2*(E2-E1)/(2*E2*Prated*fsw_min)
# print( 'L=',L*10**6,'uH')
#
# ton=(E2-E1)/(E2*fsw_min)
# t=sp.symbols('t')
# Irms=sp.sqrt(1/Tmax*sp.integrate( (E1*t/L)**2,(t,0,ton)))
# print('Irms_MOSFET=',Irms,'A')
# print('ton=',ton*10**6,'us')
#
# Ipeak=E1*ton/L
# print('Ipeak=',Ipeak,'A')
# t=sp.symbols('t')
# Irms_diode=sp.sqrt( 1/Tmax*sp.integrate( (Ipeak+(E1-E2)/L*(t-ton))**2,(t,ton,Tmax) ) )
# print('Irms_diode=',Irms_diode,'A')
# Iav_diode=1/Tmax*sp.integrate( (Ipeak+(E1-E2)*(t-ton)/L),(t,ton,Tmax))
# print('Iav_diode=',Iav_diode,'A')
#
# print('ton=',ton*10**6,'us')
# iL1=(E1*t/L)
# iL2=Ipeak+(E1-E2)/L*(t-ton)
# Irms_inductor=sp.sqrt(1/Tmax*(sp.integrate(iL1**2,(t,0,ton))+sp.integrate(iL2**2,(t,ton,Tmax))))
# print('RMS value of the inductor current =',Irms_inductor,'A')
# print('Peak value of the inductor current =',Ipeak,'A')
#
# P=np.linspace(0.1*Prated,Prated,100)
# fsw=E1**2*(E2-E1)/(2*E2*P*L)
# ton=(E2-E1)/(E2*fsw)
# plt.grid()
# plt.plot(P,fsw/1000,'r')
# plt.xlabel('P (W)')
# plt.ylabel('fsw (kHz)' )
# plt.title('Switching Frequency as function of the Power')
#
# ## BOST PFC BCM
#
# print("\n\n\n")
#
# t=np.linspace(0,0.05,1000)
# w=2*pi*60
# Vgrid=311*np.sin(w*t)
# E1=np.abs(Vgrid)
# E2=400*(1+t*0)
# plt.grid()
# plt.plot(t*10**3,E1,'r')
# plt.plot(t*10**3,E2,'b')
# plt.ylabel('E1 and E2 (V)')
# plt.xlabel('t (ms)' )
# plt.title('E1 obtained from a the rectification of as ac voltage')
#
# ton=10*10**-6
# Pav=Iav*E1
# plt.grid()
# plt.plot(t*10**3,Pav,'r')
# plt.ylabel('P (W)')
# plt.xlabel('t (ms)' )
# plt.title('Rectifier dc side Power')
#
# t=np.linspace(0,0.05,1000)
# w=2*pi*60
# Vgrid=311*np.sin(w*t)
# E1=np.abs(Vgrid)
# E2=400*(1+t*0)
# fsw=E1**2*(E2-E1)/(2*E2*Pav*L)

# Design

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
ids_fet = 15.69 # ver na simulação valor RMS

# dados diodo
ids_diode_avg = 0
ids_diode_rms = 0
diode_voltage_drop = 0.7
diode_bulk_resistence = 2

power_dissip_fet = rds_on_fet * (ids_fet ** 2)
power_dissip_diode = diode_bulk_resistence * (ids_diode_rms ** 2) + diode_voltage_drop * ids_diode_avg

print('power dissip fet', power_dissip_fet)

print('power dissip diode', power_dissip_diode)

print('total power dissip rect-diode', 4 * power_dissip_diode)
print('total power dissipation', power_dissip_fet + 5 * power_dissip_diode)

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

tb_diode = 0
IRR_diode = 0
Cap_Rev_Diode = 0
ReverseVoltage = 0

PowerComLossDiodeConv = 1 / 2 * Cap_Rev_Diode * ReverseVoltage ** 2 * fsw_min + 1 / 6 * IRR_diode * ReverseVoltage * tb_diode * fsw_min

print('power comutation losses in diode', PowerComLossDiodeConv)
