from tkinter import *
root=Tk()

VarOperacion=IntVar()
#Funcion que imprime
def imprimir():
    #print (VarOperacion.get()
    if VarOperacion.get()==1:
        etiqueta.config(text="has elegido masculino");
    else:
        etiqueta.config(text="has elegido femenino");

Label(root, text="Genero").pack()
Radiobutton(root, text="Masculino", variable=VarOperacion, value=1, command=imprimir).pack();
Radiobutton(root, text="Masculino", variable=VarOperacion, value=2, command=imprimir).pack();

etiqueta=Label(root);
etiqueta.pack()

root.mainloop

