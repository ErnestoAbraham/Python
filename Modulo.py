#creando una super clase
class vehiculos():
    #constructor
    def __init__(self, marca, modelo):

        self.marca = marca;
        self.modelo = modelo;
        self.enmarcha = False;
        self.acelerar = False;
        self.frena = False;

    #metodo arrancar
    def arrancar(self):

        self.enmarcha = True;

    def acelerar(self):
        self.acelerar = True;

    def frenar(self):
        self.frena = True

    #metodo que imprima en patalla el estado
    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelerar,
              "\nFrenado: ", self.frena);

#creando la clase furgoneta
class Furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado = cargar;
        if (self.cargado==True):
            return "La furgoneta está cargada";
        else:
            return "La furgoneta no esta cargada";

#Clase moto que hereda de clase vehiculos
class Moto(vehiculos):
    #colocando un metodo que sea unico de las motos
    haciendoCaballito = "";
    def caballito(self):
        self.haciendoCaballito = "Voy haciendo caballito";

# sobreescribiendo el metodo que imprima en patalla el estado

    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelerar,
              "\nFrenado: ", self.frena, "\n", self.haciendoCaballito);

class VElectrico():
    def __init__(self):
        self.autonomia = 100;

    def cargaEnergia(self):
        self.cargando = True;