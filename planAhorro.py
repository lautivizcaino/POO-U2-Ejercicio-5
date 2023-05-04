class PlanAhorro:
    __codigo=int
    __modelo=str
    __version=str
    __valor=float
    __cantCuotas=60
    __cantCuotasPagas=10
    def __init__(self,codigo=0,modelo='',version='',valor=0.0):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
    def getCod(self):
        return self.__codigo
    def getMod(self):
        return self.__modelo
    def getVer(self):
        return self.__version
    def setValor(self,nValor):
        self.__valor=nValor
    def getImpCuota(self):
        return self.__valor/self.__cantCuotasPagas+self.__valor*0.1
    def __str__(self):
        return '%s %s %s %s'%(self.__codigo,self.__modelo,self.__version,self.__valor)
    @classmethod
    def getCuotasLic(cls):
        return cls.__cantCuotasPagas
    @classmethod
    def setCuotasPagas(cls,cuotas):
        cls.__cantCuotasPagas=cuotas
    @classmethod
    def verCuotas(cls):
        print('Cantidad de cuotas del vehiculo: %s'%(cls.__cantCuotas))
        print('Cantidad de cuotas pagas para licitar el vehiculo: %s'%(cls.__cantCuotasPagas))