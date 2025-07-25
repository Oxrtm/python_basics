print('*** Revision Valor Positivo ***')
numero = int(input('Que numero quieres evaluar? '))
if numero > 0:
    print(f'Es positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero: {numero}')