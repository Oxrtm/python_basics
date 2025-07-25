print('*** Operador Logico and ***')
condicion1 = True
condicion2 = False
# Aplicamos el operador and
resultado = condicion1 and condicion2
# El operador and si cualquiera de sus operandos
# es falso, toda la expresion regresa falso
#print(f'Resultado {condicion1} and {condicion2}: {resultado}')

# Ejemplo if else con operador and
llueve = True
nublado = True
print(f'\n*** Revision del clima ***')
if llueve and nublado:
    print('llevar paraguas e impermeable, llueve y esta nublado')
elif llueve:
    print('Llevar paraguas, va a llover')
elif nublado:
    print('llevar impermeable, solo esta nublado ')
else:
    print('Dejar paraguas e impermeable, disfruta de tu dia')