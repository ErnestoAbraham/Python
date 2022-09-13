#CONSTRUYENDO UNA CLASE COCHE
class Coche():
    #CONTRUIR SIRVE PARA INICIALIZAR LOS ATRIBUTOS SEL OBJETO
    def __init__(self):
    #Atributos
        self.LargoChasis = 250;
        self.AnchoChasis = 120;
        self.__ruedas = 4;
        self.enmarcha = False; #METODO INICIAR

#METODOS (ACCIONES QUE PUEDE HACER LOS OBJETOS)
#self significa objeto perteneciente a la clase, similar a this en c++
    def arrancar(self, arrancamos):
        #cambiando el comportamiento del coche
        self.enmarcha = arrancamos


        if (self.enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.enmarcha == True and chequeo == True):
            return "el coche esta en marcha";
        elif(self.enmarcha==True and chequeo==False):
            return "Algo esta incorrecto en el chequeo, no podemos arrancar"
        else:
            return "el coche esta parado";

#COMPORTAMIENTO DEL COCHE
    def estado(self):
        print("El coche tiene ", self.__ruedas,
              " ruedas. un ancho de ", self.AnchoChasis,
              "y un largo de ", self.LargoChasis);

    def __chequeo_interno(self):#Rencapsulando metodo
        print("realizando chequeo interno");
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite):
            return True
        else:
            return False




#INSTANCIANDO UN NUEVO OBJETO
miCoche2 = Coche();

print(miCoche2.arrancar(True));
#CHECAMOS EL ESTADO DEL COCHE
miCoche2.estado();

print("\n--- creando un segundo objeto \n");
#instanciando un nuevo objeto
miCoche2 = Coche();
print(miCoche2.arrancar(False));
#MODIFICANDO LA PROPIEDAD DE UN OBJETO
miCoche2.__ruedas = 2;
#CHECAMOS EL ESTADO DEL COCHE
miCoche2.estado();