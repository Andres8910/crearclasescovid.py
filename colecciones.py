import datetime #importo una funcion para que pueda tener fechas

class Incidente:
    def __init__(self, Fecha, Pais, NContagios, NFallecidos):
        self.Fecha = Fecha  #Tipo datetime
        self.Pais = Pais     #String
        self.NContagios = NContagios #int
        self.NFallecidos = NFallecidos #int

#Aqui hice dos objetos para la clase Incidente

IncidenteHoy = Incidente(datetime.datetime.now(),'Mexico',1500,18)
IncidenteAyer = Incidente(datetime.datetime(2020, 5, 17),'Mexico',800,10)

#se crea una lista en snake notation
mi_lista = []

#Se agregan elementos con append
mi_lista.append(IncidenteHoy)
mi_lista.append(IncidenteAyer)

#Imprime una secuencia, que es las dos listas

# el len extrae la cantidad de elementos en la lista que son IncidenteHoy y IncidenteAyer
print(len(mi_lista))

#=================================================================================

#se imprime con un bucle for los objetos que estan en la lista
for cont in mi_lista:
  print(cont.Pais)

class Pais:  #---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS#
    # El __init__ es un constructor , que es un metodo y sirve para generar objetos parametrizados

    def __init__(self, NombreING, NombreESP, Fallecidos, Contagiados, PDC):
        self.NombreING = NombreING #String
        self.NombreESP = NombreESP #String
        self.Fallecidos = Fallecidos #int
        self.Contagiados = Contagiados #int
        self.PDC = PDC #Tipo datetime


#========================================================================
#Reto Hacer 5 obejtos y isntanciar 5 paises en una lista 

Germany = Pais('Germany','Alemania',5000,15000,datetime.datetime(2020, 4, 11))
Canada = Pais('Canada','Canadá',2500,7800,datetime.datetime(2020, 5, 11))
China = Pais('China','China',100000,250000,datetime.datetime(2020, 2, 1))
Russia = Pais('Russia','Rusia',700,2000,datetime.datetime.now())
Brazil = Pais('Brazil','Brasil',10000,30000,datetime.datetime(2020, 3, 3))

mis_paises = []

mis_paises.append(Germany)
mis_paises.append(Canada)
mis_paises.append(China)
mis_paises.append(Russia)
mis_paises.append(Brazil)

print("================================")

print(len(mis_paises))

for contador in mis_paises:
  print(contador.NombreING)