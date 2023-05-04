from planAhorro import PlanAhorro
import csv
class GestorPlanes:
    __listaPlanes=[]
    def __init__(self):
        self.__listaPlanes=[]
    def agregarPlan(self,plan):
        self.__listaPlanes.append(plan)
    def testPlanes(self):
        file= open('planes.csv')
        reader= csv.reader(file,delimiter=';')
        for row in reader:
            codigo=int(row[0])
            modelo=row[1]
            version=row[2]
            valor=int(row[3])
            cantCuotas=int(row[4])
            cantCuotasPagas=int(row[5])
            plan= PlanAhorro(codigo,modelo,version,valor)
            self.agregarPlan(plan)
    def actualizarValor(self):
        for i in range(len(self.__listaPlanes)):
            print('\nCodigo de plan: %s, Modelo: %s, Versión: %s'%(self.__listaPlanes[i].getCod(),self.__listaPlanes[i].getMod(),self.__listaPlanes[i].getVer()))
            self.__listaPlanes[i].setValor(int(input('Ingrese nuevo valor de vehiculo: ')))
    def mostrarDatos(self,valor):
        for i in range(len(self.__listaPlanes)):
            if self.__listaPlanes[i].getImpCuota()<valor:
                print('\nCodigo de plan: %s, Modelo: %s, Versión: %s'%(self.__listaPlanes[i].getCod(),self.__listaPlanes[i].getMod(),self.__listaPlanes[i].getVer()))

    def mostrarMonto(self):
        for i in range(len(self.__listaPlanes)):
            print('Importe del vehiculo con codigo %s: %.2f\n'%(self.__listaPlanes[i].getCod(),self.__listaPlanes[i].getCuotasLic()*self.__listaPlanes[i].getImpCuota()))
    def modificarCuotasLic(self,cod):
        for i in range(len(self.__listaPlanes)):
            if cod==self.__listaPlanes[i].getCod():
                self.__listaPlanes[i].setCuotasPagas(int(input('\nIngrese cantidad de cuotas pagas para licitar: ')))
                
    def __str__(self):
        s=''
        for plan in self.__listaPlanes:
            s+= str(plan) + '\n'
        return s