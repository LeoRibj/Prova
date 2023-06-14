from .Conta import Conta

class HistoryContas:
    def __init__(self) -> None:
        self.__contas  = []
   
    def getMediaKw(self)->Conta:
        x=0
        for i in self.__contas:
            x=x+i.getKwGatsto()
        x = x / len(self.__contas)
        return print("media é %.2f" % x)

    def getValorMediaContas(self):
        y=0
        for i in self.__contas:
            y+=i.getValorPagar()
        y = y / len(self.__contas)
        return print("media valor contas: %.2f" % y)
    def getMesMaiorConsumo(self):
        data=0
        for i in self.__contas:
            if i.getValorPagar() > data:
                data=i.getValorPagar()
        print("maior consumo foi ",data)

    def getMesMenorConsumo(self):
        data=1000000
        mes=""
        for i in self.__contas:
            if i.getValorPagar() < data:
                data=i.getValorPagar()
            
            

        print("menor consumo foi",data)
    def setConta(self,conta:Conta):
        self.__contas.append(conta)