from tkinter import * 
from tkinter import messagebox

ventana = Tk()
ventana.title('Cobro Posnet')
ventana.geometry('270x230')
ventana.configure(background='#6C93A8')

def cobrar_10():
    entry_total_valor.config(state=NORMAL)
    entry_total_valor.delete('0', END)
    entry_total_valor.config(state='readonly')
    valor = entry_ingresa_valor.get()
    if valor.isdigit():
        porcentaje_valor = int(valor) * 10 / 100
        resultado = int(valor) + porcentaje_valor
        entry_total_valor.config(state=NORMAL)
        entry_total_valor.insert(END, str(resultado))
        entry_total_valor.config(state='readonly')
    else:
        messagebox.showinfo('Error', 'El valor ingresado no es correcto')
        entry_ingresa_valor.delete('0', END)


def cobrar_15():
    entry_total_valor.config(state=NORMAL)
    entry_total_valor.delete('0', END)
    entry_total_valor.config(state='readonly')
    valor = entry_ingresa_valor.get()
    if(valor.isdigit()):
        porcentaje_valor = int(valor) * 15 / 100
        resultado = int(valor) + porcentaje_valor
        entry_total_valor.config(state=NORMAL)
        entry_total_valor.insert(END, str(resultado))
        entry_total_valor.config(state='readonly')
    else:
        messagebox.showinfo('Error', 'El valor ingresado no es correcto')
        entry_ingresa_valor.delete('0', END)
        
    
    
    
        

label_ingresa_valor = Label(ventana, text='Ingrese Valor a Cobrar', bg='#6C93A8', fg='white')
label_ingresa_valor.pack(pady=5)
entry_ingresa_valor = Entry(ventana, font=('Verdana', 16), bg='#45595F', fg='white')
entry_ingresa_valor.pack(pady=5)
boton_10 = Button(ventana, text='10%', width=10, font=('Verdana', 12), activebackground='#D6814E', bg='#427180', fg='white', command=cobrar_10)
boton_10.pack(pady=5)
boton_15 = Button(ventana, text='15%', width=10, font=('Verdana', 12), activebackground='#D6814E', bg='#427180', fg='white', command=cobrar_15)
boton_15.pack(pady=5)
label_total_valor = Label(ventana, text='El Total a Cobrar es', bg='#6C93A8', fg='white')
label_total_valor.pack(pady=5)
entry_total_valor = Entry(ventana, font=('Verdana', 16), bg='#45595F', state='readonly')
entry_total_valor.pack(pady=5)



ventana.mainloop()