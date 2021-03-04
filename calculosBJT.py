import numpy as np

#Transistor datasheet info
beta_min = 250
beta_max = 600
beta_small_signal_min = 250
beta_small_signal_max = 900

v_ce_sat = 0.7
v_be = 0.85
v_ce = 5

#simulation info
i_c = 25.3*10**(-3)
i_b = 100*10**(-6)

#calculation
beta = i_c/i_b

voltage_source = 2*v_ce

v_e = voltage_source*0.1
r_e = v_e/i_c
r_c = (voltage_source-v_e-v_be)/i_c

r_2 = beta*r_e/10

v_b = v_be+v_e
r_1 = (voltage_source*r_2-v_b*r_2)/v_b


#results
print(beta)
print('R1 = '+ str(r_1))
print('R2 = '+ str(r_2))
print('Rc = '+ str(r_c))
print('Re = '+ str(r_e))

print('Voltage = '+ str(voltage_source))
print('VE = '+ str(v_e))
print('VB = '+ str(v_b))


