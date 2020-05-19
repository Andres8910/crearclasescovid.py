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

#se imprime con un bucle for los objetos que estan en la lista
for cont in mi_lista:
  print(cont.Pais)




