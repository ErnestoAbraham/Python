#creando una super clase.
class Vehiculos():
    # Constructor
    def __init__(self, marca, modelo):
        # atributos
        self.marca = marca;
        self.modelo = modelo;
        self.enmarcha = False;
        self.acelerar = False;
        self.frena = False;

    #método arrancar
    def arrancar(self):

        self.enmarcha = True;

    def acelerar(self):
        self.acelerar = True;

    def frenar(self):
        self.frena = True

    #método que imprima en patalla el estado
    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo,
        "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelerar,
        "\nFrenado: ", self.frena);

#Clase moto que hereda de clase vehículos
class Moto(Vehiculos):
    #colocando un método que sea único de las motos
    haciendoCaballito = "";
    def caballito(self):
        self.haciendoCaballito = "Voy haciendo un caballito";

    # CREANDO LA CLASE FURGONETA
    class Furgoneta(Vehiculos):
        def carga(self, cargar):
            self.cargando = cargar;
            if (self.cargando == True):
                return "La furgoneta esta cargando";
            else:
                return "La furgoneta no esta cargando"

    #sobreescribiendo el métyodo que imprima en pantalla el estado
    def estado(self):
         print("Marca; ", self.marca, "\nModelo: ", self.modelo,
        "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelerar,
        "\nFrenado: ", self.frena,"\n", self.haciendoCaballito);




#Instanciando
miMoto = Moto("Honda", "CBR");
#Llamando al método estado()
miMoto.caballito();
miFurgoneta = Furgoneta("renault", "Van")
miFurgoneta.arrancar();
miFurgoneta.estado();
miMoto.estado();

    