import datetime #importo una funcion para que pueda tener fechas

#Aqui declare una
#clase llamada Pais
class Pais:  #---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS#
    # El __init__ es un constructor , que es un metodo y sirve para generar objetos parametrizados

    def __init__(self, NombreING, NombreESP, Fallecidos, Contagiados, PDC):
        self.NombreING = NombreING #String
        self.NombreESP = NombreESP #String
        self.Fallecidos = Fallecidos #int
        self.Contagiados = Contagiados #int
        self.PDC = PDC #Tipo datetime


#Aqui declare otra clase llamada incidente


class Incidente:
    def __init__(self, Fecha, Pais, NContagios, NFallecidos):
        self.Fecha = Fecha  #Tipo datetime
        self.Pais = Pais     #String
        self.NContagios = NContagios #int
        self.NFallecidos = NFallecidos #int


#Aqui hice un objeto para la clase Pais
MiPais = Pais('Mexico','México',1000,5000,datetime.datetime(2020, 5, 18))
print(MiPais.PDC)

#Aqui hice dos objetos para la clase Incidente

IncidenteHoy = Incidente(datetime.datetime.now(),'Mexico',1500,18)
print(IncidenteHoy.Fecha)
IncidenteAyer = Incidente(datetime.datetime(2020, 5, 17),'Mexico',800,10)
print(IncidenteAyer.Fecha)