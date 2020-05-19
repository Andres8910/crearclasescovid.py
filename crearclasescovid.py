#Aqui declare una
#clase llamada Pais
class Pais:  #---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS---ATRIBUTOS#
    # El __init__ es un constructor , que es un metodo y sirve para generar objetos parametrizados

    def __init__(self, NombreING, NombreESP, Fallecidos, Contagiados):
        self.NombreING = NombreING
        self.NombreESP = NombreESP
        self.Fallecidos = Fallecidos
        self.Contagiados = Contagiados


#Aqui declare otra clase llamada incidente


class Incidente:
    def __init__(self, Fecha, Pais, NContagios, NFallecidos):
        self.Fecha = Fecha
        self.Pais = Pais
        self.NContagios = NContagios
        self.NFallecidos = NFallecidos


MiPais = Pais('Mexico','México',1000,5000)
print(MiPais.NombreING)

