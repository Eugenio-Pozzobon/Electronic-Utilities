# Q1

RTT_q1 = .1
SegmentoMax_q1 = 1000
Janela_segmentos = (16+3)*1000
print('a) 32k')
print("b) Velocidade: ", Janela_segmentos/RTT_q1, 'bit/s')


# Q4

print('\n\n Q4:')

valor_a_1 = 191
valor_a_2 = 138
valor_a_3 = 163
valor_a_4 = 13

valor_b_3 = 113
valor_b_4 = 32

valor_c_1 = 131
valor_c_2 = 175
valor_c_3 = 123
valor_c_4 = 244

mask255 = 255
mask224 = 224
mask240 = 240
mask0 = 0

print('\nA) ip:',valor_a_1,'.', valor_a_2,'.',valor_a_3,'.',valor_a_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask240 ,'.', mask0)
print('Result:', mask255 & valor_a_1 ,'.', mask255 & valor_a_2,'.', mask240 & valor_a_3,'.', mask0 & valor_a_4)

print('\nA) ip:',valor_a_1,'.', valor_a_2,'.',valor_a_3,'.',valor_a_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask224 ,'.', mask0)
print('Result:', mask255 & valor_a_1 ,'.', mask255 & valor_a_2,'.', mask224 & valor_a_3,'.', mask0 & valor_a_4)

print('\nA) ip:',valor_a_1,'.', valor_a_2,'.',valor_a_3,'.',valor_a_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask0 ,'.', mask0)
print('Result:', mask255 & valor_a_1 ,'.', mask255 & valor_a_2,'.', mask0 & valor_a_3,'.', mask0 & valor_a_4)

print('\nB) ip:',valor_a_1,'.', valor_a_2,'.',valor_b_3,'.',valor_b_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask240 ,'.', mask0)
print('Result:', mask255 & valor_a_1 ,'.', mask255 & valor_a_2,'.', mask240 & valor_b_3,'.', mask0 & valor_b_4)

print('\nB) ip:',valor_a_1,'.', valor_a_2,'.',valor_b_3,'.',valor_b_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask224 ,'.', mask0)
print('Result:', mask255 & valor_a_1 ,'.', mask255 & valor_a_2,'.', mask224 & valor_b_3,'.', mask0 & valor_b_4)

print('\nB) ip:',valor_a_1,'.', valor_a_2,'.',valor_b_3,'.',valor_b_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask0 ,'.', mask0)
print('Result:', mask255 & valor_a_1 ,'.', mask255 & valor_a_2,'.', mask0 & valor_b_3,'.', mask0 & valor_b_4)


print('\nC) ip:',valor_c_1,'.', valor_c_2,'.',valor_c_3,'.',valor_c_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask240 ,'.', mask0)
print('Result:', mask255 & valor_c_1 ,'.', mask255 & valor_c_2,'.', mask240 & valor_c_3,'.', mask0 & valor_c_4)

print('\nC) ip:',valor_c_1,'.', valor_c_2,'.',valor_c_3,'.',valor_c_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask224 ,'.', mask0)
print('Result:', mask255 & valor_c_1 ,'.', mask255 & valor_c_2,'.', mask224 & valor_c_3,'.', mask0 & valor_c_4)

print('\nC) ip:',valor_c_1,'.', valor_c_2,'.',valor_c_3,'.',valor_c_4)
print('Mask:', mask255 ,'.', mask255 ,'.', mask0 ,'.', mask0)
print('Result:', mask255 & valor_c_1 ,'.', mask255 & valor_c_2,'.', mask0 & valor_c_3,'.', mask0 & valor_c_4)


# Q5

RTT_Q5 = .2
SegmentoMax_Q5 = 1000
t = 500*1000

janela_segmentos = RTT_Q5*t

print("\n\n Q5: Janela", janela_segmentos)

# Se o limiar é 64 segmentos, resta a transmissão de:

print("Resta transmitir: ", (janela_segmentos-64000), 'bytes, levando um tempo (s) de ',(janela_segmentos-64000)/1000*RTT_Q5)

