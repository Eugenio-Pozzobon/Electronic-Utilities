# NMOS

Vgs_op = 0.5
Vds_op = 0.5
Vth_op = 0.195
Id_op = 63.486 * pow(10, -6)

xo = .4
yo = 65.6 * pow(10, -6)

dx = 300 * pow(10, -3)
dy = 2.46 * pow(10, -6)

m = dy/dx
print(m)

W = 2.5 * pow(10, -6)
L = 0.5 * pow(10, -6)

q = yo-(xo*m)
lamb_nmos = m/q

uCos_nmos = 2 * Id_op / (W / L * pow((Vgs_op - Vth_op), 2) * (1 + lamb_nmos * Vds_op))

print(lamb_nmos)
print(uCos_nmos)


# PMOS

Vgs_op_pmos = 0.5
Vds_op_pmos = 0.5
Vth_op_pmos = -0.183903
Id_op_pmos = 31.853 * pow(10, -6)

xo_pmos = .4
yo_pmos = 31.49 * pow(10, -6)

dx_pmos = 380 * pow(10, -3)
dy_pmos = 1.143 * pow(10, -6)

m_pmos = dy_pmos/dx_pmos

W_pmos = 2.5 * pow(10, -6)
L_pmos = 0.5 * pow(10, -6)

q_pmos = yo_pmos-(xo_pmos*m_pmos)
lamb_pmos = m_pmos/q_pmos

uCos_pmos = 2 * Id_op_pmos / (W_pmos / L_pmos * pow((Vgs_op_pmos - Vth_op_pmos), 2) * (1 + lamb_pmos * Vds_op_pmos))

print(lamb_pmos)
print(uCos_pmos)


#ampop
Vgs_amp_pmos = .5
Vds_amp_pmos = .5
W_pmos_calc = 2*Id_op*L_pmos/(uCos_pmos*pow((Vgs_amp_pmos-Vth_op_pmos), 2)*(1+lamb_pmos*Vds_amp_pmos))

print(W_pmos_calc)

### aula 23-05
Id_op = .000064
Vgs_amp_pmos = .25
Vds_amp_pmos = .25
W_pmos_calc = 2*Id_op*L_pmos/(uCos_pmos*pow((Vgs_amp_pmos-Vth_op_pmos), 2)*(1+lamb_pmos*Vds_amp_pmos))

print(W_pmos_calc)


Id_op = .0000128
Vgs_amp_nmos = .38

Vds_amp_nmos = .25
W_nmos_calc = 2*Id_op*L_pmos/(uCos_nmos*pow((Vgs_amp_nmos-Vth_op), 2)*(1+lamb_pmos*Vds_amp_nmos))

print(W_nmos_calc)


Id_op = .000001
Vgs_amp_nmos = .3

Vds_amp_nmos = .25
W_nmos2_calc = 2*Id_op*L_pmos/(uCos_nmos*pow((Vgs_amp_nmos-Vth_op), 2)*(1+lamb_pmos*Vds_amp_nmos))

print(W_nmos2_calc)

############
x = (21.19*0.5-58.681)/21.19
# print(1/x)
var = (6.872*0.5-25.374)/6.872
# print(1/var)

unCox = 586.81/(pow((0.5-0.2), 2)*(1+0.44*0.5))
# print(unCox)