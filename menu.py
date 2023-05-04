from gestorPlanes import GestorPlanes

class Menu:
    __opcion=int
    def __init__(self):
        __opcion=5
    def opciones(self,lista):
        while self.__opcion!=0:
            print('\n1 - Actualizar el valor del vehiculo de cada plan')
            print('2 - Mostrar codigo del plan, modelo y version del vehiculo')
            print('3 - Mostrar el monto a pagar para licitar el vehiculo')
            print('4 - Modificar la cantidad de cuotas para licitar')
            print('0 - Salir\n')
            self.__opcion=int(input('Ingrese la opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nInciso a')
                lista.actualizarValor()
            if self.__opcion==2:
                print('\nInciso b\n')
                lista.mostrarDatos(int(input('Ingresar valor del vehiculo: ')))
            if self.__opcion==3:
                print('\nInciso c\n')
                lista.mostrarMonto()
            if self.__opcion==4:
                print('\nInciso d\n')
                lista.modificarCuotasLic(int(input('Ingrese codigo de un plan: ')))
        else:
            print('\nHa salido del sistema')