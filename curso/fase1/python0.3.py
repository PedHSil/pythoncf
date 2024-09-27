numero_str = input(
    'Vou dobrar o numero que vc digitar: '
)

try: 
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso n é um numero')