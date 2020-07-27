# TIPE DATA SKALAR
roti1 = 'roti_bolu'
roti2 = 'roti_kukus'
roti3 = 'roti_bakar'
roti4 = 'roti_donat'

print(roti1)
print(roti2)
print(roti3)
print(roti4)

# TIPE DATA ARRAY
print('\ntipe data array')
roti = ['roti bolu', 'roti kukus', 'roti bakar', 'roti donat']
print(roti)
roti.append('roti lapis')
print(roti)

print('\nhari ini makan roti apa?')
print(f'Makan {roti[3]}')

print('\nMakan Semua Roti')
for r in roti:
    print(f'Makan {r}')

print('\nmakan semua roti: cara ribet')
for r in range (0, len(roti)):
    print(f'makan {roti[r]}')

