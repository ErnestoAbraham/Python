from tkinter import *
#para usar vetanas emergentes
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Luis", "Procesador de textos 2022");

def avisoLicencia():
    messagebox.showwarning("Licencia", "producto bajo licencia Python");

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?");

    if valor=="Si":
        root.destroy();

barraMenu=Menu(root);
root.config(menu=barraMenu, width=300, height=300);

archivoMenu=Menu(barraMenu, tearoff=0);
archivoMenu.add_cascade(label="Nuevo");
archivoMenu.add_cascade(label="Guardar");
archivoMenu.add_cascade(label="Guardar Como");
archivoMenu.add_cascade(label="Cerrar");
archivoMenu.add_cascade(label="Salir", command=salirAplicacion);

archivoEdicion=Menu(barraMenu, tearoff=0);
archivoEdicion.add_cascade(label="Copiar");
archivoEdicion.add_cascade(label="Cortar");
archivoEdicion.add_cascade(label="Pegar");

archivoHerramientas=Menu(barraMenu, tearoff=0);

archivoAyuda=Menu(barraMenu, tearoff=0);
archivoAyuda.add_command(label="Licencia", command=avisoLicencia);
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional);

barraMenu.add_cascade(label="Archivo", menu=archivoMenu);
barraMenu.add_cascade(label="Edición", menu=archivoEdicion);
barraMenu.add_cascade(label="Herramienta", menu=archivoHerramientas);
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda);
root.mainloop();