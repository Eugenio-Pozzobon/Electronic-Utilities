import numpy as np

#FET datasheet info
v_t = 2

#simulation info
v_ds = 8
v_gs = 3
i_d = 0.142

r_2_current = 0.000001 #microampere

#calculation
voltage_source = 2*v_ds

v_s = voltage_source*0.1
v_g = v_gs+v_s
v_d = v_s+v_ds

r_s = v_s/i_d
r_d = (voltage_source-v_d)/i_d

r_2 = v_g/r_2_current
r_1 = (voltage_source*r_2-v_g*r_2)/v_g

#analise ac
K = i_d/(pow((v_gs-v_t), 2))
gm = 2*K*(v_gs-v_t)
z_o = 1/(1/r_d)
z_i = 1/(1/r_1 + 1/r_2)

#results
print('R1 = '+ str(r_1))
print('R2 = '+ str(r_2))
print('Rdreno = '+ str(r_d))
print('Rsource = '+ str(r_s))

print('Voltage = '+ str(voltage_source))
print('VSource = '+ str(v_s))
print('VGate = '+ str(v_g))
print('VDrain = '+ str(v_d))

print('IDrain = '+ str(i_d))

print('K = '+ str(K))
print('gm = '+ str(gm))
print('Zo = '+ str(z_o))
print('Zi = '+ str(z_i))
print('Av = '+ str(gm*z_o))

#------------
z_o_sim = 8.55/gm
ro = z_o_sim/(1-(z_o_sim/r_d))

print('Zosimulado = '+ str(z_o_sim))
print('rosimulado = '+ str(ro))
print('Averro_simulado = '+ str((gm*z_o - 8.55)/(gm*z_o)))


