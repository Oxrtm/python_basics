# Menu interactivo con ciclo while
print('*** Sistema de Administracion de Cuentas ***')

salir = False
while not salir:
    print(f'''Menu:
        1. Crear cuenta
        2. Eliminar cuenta
        3. Salir''')
    opcion = int(input('Escoge una opcion: '))
    if opcion == 1:
        print('Creando tu cuenta....\n')
    elif opcion == 2:
        print('Eliminado tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto...\n')
        salir = True
    else:
        print('Opcion invalidad. selecciona otra opcion...\n')