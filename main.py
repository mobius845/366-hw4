x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

A = []
C = []
max_array = []
min_array = []

for i in range(21):
    if (i == 0):
        A.append(x)
    elif (i == 1):
        A.append(y)
    else:
        A.append(2 * A[i - 2] - A[i - 1])

for num in A:
    hex_str = hex(num & 0xFFFFFFFF)[2:]  # Convert to hexadecimal (32-bit)
    EF_count = hex_str.count('e') + hex_str.count('f')  # Count 'e' and 'f' 
    C.append(EF_count)

for col in range(7):
    col_values = [A[i * 7 + col] for i in range(3)]
    max_array.append(max(col_values))
    min_array.append(min(col_values))

B = []
for i in range(0x2010, 0x2010+21*4, 4):
    B.append(i)
  
D = []
for i in range(0x2080, 0x2080+21*4, 4):
  D.append(i)

E = []
for i in range (0x2100, 0x2100+7*4, 4):
  E.append(i)

F = []
for i in range (0x2180, 0x2180+7*4, 4):
  F.append(i)
  
print("\nArray A:")
for i in range (21):
    print(f'M[{hex(B[i])}]: {A[i]:8}', end=', ')
    if (i % 7 == 6):
        print('\n')

print("\nEF Count Array C:")
for i in range (21):
    print(f'M[{hex(D[i])}]: {C[i]:8}', end=', ')
    if (i % 7 == 6):
        print('\n')

print("\nMax Array:")
for i in range (7):
    print(f'M[{hex(E[i])}]: {max_array[i]:8}', end=', ')
    if (i % 7 == 6):
        print('\n')

print("\nMin Array:")
for i in range (7):
    print(f'M[{hex(F[i])}]: {min_array[i]:8}', end=', ')
    if (i % 7 == 6):
        print('\n')