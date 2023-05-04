from gestorPlanes import GestorPlanes
from planAhorro import PlanAhorro
from menu import Menu
def test():
    lista = GestorPlanes()
    lista.testPlanes()
    menu = Menu()
    menu.opciones(lista)
if __name__ == '__main__':
    test()