# from tkinter import Tk, Button, Entry

# # Configuración ventana principal
# root = Tk()
# root.title("Calculadora POO")
# root.resizable(0, 0)
# root.geometry("300x275")

# # Configuración pantalla de salida 
# pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
# pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=10)

# #Configuración botones
# boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_1.grid(row=1, column=0, padx=1, pady=1)

# boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_2.grid(row=1, column=1, padx=1, pady=1)

# boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_3.grid(row=1, column=2, padx=1, pady=1)

# boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_4.grid(row=2, column=0, padx=1, pady=1)

# boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_5.grid(row=2, column=1, padx=1, pady=1)

# boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_6.grid(row=2, column=2, padx=1, pady=1)

# boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_7.grid(row=3, column=0, padx=1, pady=1)

# boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_8.grid(row=3, column=1, padx=1, pady=1)

# boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
# boton_9.grid(row=3, column=2, padx=1, pady=1)

# boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2")
# boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

# boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
# boton_punto.grid(row=4, column=2, padx=1, pady=1)

# boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
# boton_mas.grid(row=1, column=3, padx=1, pady=1)

# boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
# boton_menos.grid(row=2, column=3, padx=1, pady=1)

# boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
# boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)

# boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
# boton_division.grid(row=4, column=3, padx=1, pady=1)

# root.mainloop()


from tkinter import Tk, Button, Entry

root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("300x260")

def agregarNumero(numero):
    pantalla.insert(len(pantalla.get()), str(numero))


def punto():
    if "." not in pantalla.get():
        pantalla.insert(len(pantalla.get()), ".")


def negativo():
    if "-" not in pantalla.get():
        pantalla.insert(0, "-")
    else:
        pantalla.delete(0)


def operacion(operador):
    global num1, operacion
    operacion = operador
    num1 = float(pantalla.get())
    pantalla.delete(0, "end")


def resultado():
    num2 = float(pantalla.get())
    pantalla.delete(0, "end")

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División entre cero"

    pantalla.insert(0, str(resultado))

pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(1))
boton_1.grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(2))
boton_2.grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(3))
boton_3.grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(4))
boton_4.grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(5))
boton_5.grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(6))
boton_6.grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(7))
boton_7.grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(8))
boton_8.grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(9))
boton_9.grid(row=3, column=2, padx=1, pady=1)

boton_0 = Button(root, text="0", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregarNumero(0))
boton_0.grid(row=4, column=1, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=resultado)
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=punto)
boton_punto.grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operacion("+"))
boton_mas.grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=negativo)
boton_menos.grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operacion("*"))
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operacion("/"))
boton_division.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()