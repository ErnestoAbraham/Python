from tkinter import*
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="abrir", initialdir="C:")
    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
