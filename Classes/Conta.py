from datetime import datetime
import datetime as dt
class Conta:
    def __init__(self,n_conta:str="",dataleitura:datetime=datetime.now,valor:float=0,n_leitura:str="",kwGasto:int=0) -> None:
        self.__n_conta=n_conta
        self.__dataleitura=dataleitura
        self.__valor=valor  
        self.__data_pgto=data_pgto= dt.timedelta(days=20)+dataleitura
        self.__kwGasto=kwGasto
        self.__n_leitura=n_leitura
    def getDataLeitura(self):
        return self.__dataleitura.strftime(" %d %m %Y")
    def getkwgasto(self):
        return self.__kwGasto
    def getvalorpagar(self):
        return self.__valor
    def getDadosConta(self):
        pass