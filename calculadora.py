from tkinter import*

ventana = Tk()
ventana.title("Calculadora")

i=0

#entrada de texto
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan =4, padx=5,pady=5)

def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i=i+1

def borrar():
    e_texto.delete(0,END)
    i = 0

def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i=0

#creacion de botones
button1 = Button(ventana, text='1', width="5", height="2",command= lambda: click_boton(1))
button2 = Button(ventana, text='2', width="5", height="2",command= lambda: click_boton(2))
button3 = Button(ventana, text='3', width="5", height="2",command= lambda: click_boton(3))
button4 = Button(ventana, text='4', width="5", height="2",command= lambda: click_boton(4))
button5 = Button(ventana, text='5', width="5", height="2",command= lambda: click_boton(5))
button6 = Button(ventana, text='6', width="5", height="2",command= lambda: click_boton(6))
button7 = Button(ventana, text='7', width="5", height="2",command= lambda: click_boton(7))
button8 = Button(ventana, text='8', width="5", height="2",command= lambda: click_boton(8))
button9 = Button(ventana, text='9', width="5", height="2",command= lambda: click_boton(9))
button0 = Button(ventana, text='0', width="5", height="2",command= lambda: click_boton(0))

boton_borrar = Button(ventana, text='AC', width="5", height="2", command=lambda: borrar())
boton_parentesis1 = Button(ventana, text='(', width="5", height="2",command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=')', width="5", height="2",command= lambda: click_boton(")"))
boton_punto = Button(ventana, text='.', width="5", height="2",command= lambda: click_boton("."))

boton_div = Button(ventana, text='/', width="5", height="2",command= lambda: click_boton("/"))
boton_mult = Button(ventana, text='*', width="5", height="2",command= lambda: click_boton("*"))
boton_sum = Button(ventana, text='+', width="5", height="2",command= lambda: click_boton("+"))
boton_rest = Button(ventana, text='-', width="5", height="2",command= lambda: click_boton("-"))
boton_igual = Button(ventana, text='=', width="5", height="2",command= lambda: hacer_operacion())




#agregar botones en pantalla
boton_borrar.grid(row=1,column=0, padx=5,pady=5)
boton_parentesis1.grid(row=1,column=1, padx=5,pady=5)
boton_parentesis2.grid(row=1,column=2, padx=5,pady=5)
boton_div.grid(row=1,column=3, padx=5,pady=5)

button7.grid(row=2,column=0, padx=5,pady=5)
button8.grid(row=2,column=1, padx=5,pady=5)
button9.grid(row=2,column=2, padx=5,pady=5)
boton_mult.grid(row=2,column=3, padx=5,pady=5)

button4.grid(row=3,column=0, padx=5,pady=5)
button5.grid(row=3,column=1, padx=5,pady=5)
button6.grid(row=3,column=2, padx=5,pady=5)
boton_sum.grid(row=3,column=3, padx=5,pady=5)

button1.grid(row=4,column=0, padx=5,pady=5)
button2.grid(row=4,column=1, padx=5,pady=5)
button3.grid(row=4,column=2, padx=5,pady=5)
boton_rest.grid(row=4,column=3, padx=5,pady=5)

button0.grid(row=5,column=0, padx=5,pady=5)
boton_punto.grid(row=5,column=1, padx=5,pady=5)
boton_igual.grid(row=5,column=2, padx=5,pady=5)

ventana.mainloop()