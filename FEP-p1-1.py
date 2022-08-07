import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# BOOST BCM PFC

Pav = 1500

Peak = 2 * Pav

E1 = 100
E1peak = np.sqrt(2) * E1
print('Peak value of the input voltage E1=', E1peak, 'V')
print('Peak value of the input voltage E1=100rms ', 100 * np.sqrt(2), 'V')
E2 = 400

fsw_min = 25000
print('Minimum switching frequency fsw_min=', fsw_min / 1000, 'kHz')

L = E1peak ** 2 * (E2 - E1peak) / (2 * E2 * Peak * fsw_min)
ton = (E2 - E1peak) / (E2 * fsw_min)

ton_250V = 2 * Peak * L / ((250 * np.sqrt(2)) ** 2)
print('L=', L * 10 ** 6, 'uH')
print('ton=', ton * 10 ** 6, 'u')
print('ton @250V=', ton_250V * 10 ** 6, 'u')

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
Cin = Iin / (2 * np.pi * fsfilter * 100)
Lin = 1 / (Cin * pow(2 * np.pi * fsfilter, 2))

print('Cin', Cin * 1000000, 'u')
print('Lin', Lin * 1000000, 'u')

print('Zeta', Lin/(2*np.sqrt(Cin* Lin)), 'u')

print('Ffiltro', 1 / (np.sqrt(Cin * Lin) * 2 * np.pi))

print('\n\n\n')

# INDUTOR

Ipeak = 44.1884
Irms_inductor = 17.8488
ILav = 13.6703

print("\n\n\nINDUTOR")
Bmax=0.1
Jmax=300*10**4
kw=0.6
AeAw=L*Ipeak*Irms_inductor/(Bmax*Jmax*kw)
print( "AeAw=",AeAw*10**8,'cm^4')

M=19.45/10
D=28.2/10
F=19.2/10
C=19.8/10
Aw=M*2*D
Ae=F*C
print ( 'Ae=', Ae,'cm^2')
print ( 'Aw=', Aw,'cm^2')
print ( 'AeAw=',Ae*Aw,'cm^4')

N=L*Ipeak/(Bmax*Ae*10**(-4))
print ( 'L=',L*10**6,'uH')
print ( 'Number of Turns N=',int(N))

mu0=4*np.pi*10**-7
lg=int(N)**2*mu0*(Ae*10**(-4))/L
print('L=',L*10**6 )
print ( 'N=', int(N))
print('Total Air gap length lg=',lg*1000,'mm')

Acu=Irms_inductor/Jmax
print ('Jmax=',Jmax*10**(-4),'cm^2')
print ( 'Conductor total cross section, Acu=',Acu*10**6,'mm^2')

# PERDAS COBRE

lcu=(F+M)*2+(1.2*C)*2
lcuT=lcu*N/100
print ( ' Length of a turn lcu=',lcu,'cm')
print ( ' Total Length of the winding lcuT=',lcuT,'m')

Ro=1.68*10**(-8)*(1+0.00404*(100-20))
Rdc=Ro*lcuT/Acu
print( ' DC resisitance of the winding Rdc=',Rdc,'ohm')
fsw=fsw_min
Skin_depth=np.sqrt(Ro/(np.pi*fsw*mu0))
print ('fsw=',fsw/1000,'kHz')
print ('Skin_depth=',Skin_depth*1000,'mm')
r1=sp.sqrt(Acu/np.pi)
print ('Radius of the conductor, r=',r1*1000,'mm')
print ('Ratio r/Skin_depth =',r1/Skin_depth)
ks=1+( (r1/Skin_depth)**4 )/( 48 + 0.8*(r1/Skin_depth)**4 )
##ks=0.25+0.5*(r1/Skin_depth)+3/32*(r1/Skin_depth)**(-1)
print('ks=',ks)
Rac=ks*Rdc
print('DC resistance     , Rdc=',Rdc,'ohm')
print('AC resistance @fsw, Rac=',Rac,'ohm')
print('AC resistance @fsw, Rac=',Ro*lcuT/(np.pi*(2*sp.sqrt(Acu/np.pi)-Skin_depth)*Skin_depth), 'ohm' )
Iac_fsw=Ipeak/2
Pcu=Rdc*ILav**2+Rdc/2*ks*(Iac_fsw)**2
print('Dc copper losses', Rdc*ILav**2, 'W')
print('AC copper losses', Rdc/2*ks*(Iac_fsw)**2, 'W')
print( 'Copper losses Pcu=',Pcu,'W')

print( 'Total losses Ptot=',Pcu + 10,'W')

# power losses in components

# dados fet
rds_on_fet = 0.022
ids_fet = 3.5 # ver na simulação valor RMS

# dados diodo
ids_diode_avg = 2.7004 # ver na simulação para 100V (eliminar filtro de entrada)
ids_diode_rms = 4.9535 # ver na simulação para 100V

# diodo boost
ids_diode_avg_boost = 3.73749 # ver na simulação para 100V
ids_diode_rms_boost = 6.06068 # ver na simulação para 100V

diode_boost_voltage_drop = 0.98+ids_diode_avg_boost*0.04
diode_resistence = 0.04

print('diode_boost_voltage_drop', diode_boost_voltage_drop)

diode_rect_voltage_drop = 0.98+ids_diode_avg*diode_resistence
print('diode_rect_voltage_drop', diode_rect_voltage_drop)

power_dissip_fet = rds_on_fet * (ids_fet ** 2)
power_dissip_diode_bulk = diode_resistence * (ids_diode_avg_boost ** 2) + diode_boost_voltage_drop * ids_diode_avg_boost
power_dissip_diode_rect = diode_resistence * (ids_diode_rms ** 2) + diode_rect_voltage_drop * ids_diode_avg

print('power dissip fet', power_dissip_fet)

print('power dissip boost diode', power_dissip_diode_bulk)
print('power dissip rect-diode',  power_dissip_diode_rect)
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

total_losses = total_dissipation_power + Poff + Pon + Pcu + 10
print("Total Losses:", total_losses)
print("Eficienty:", Pav/(total_losses+Pav))

