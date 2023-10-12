import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class Jugador:
    def __init__(self, x=0, y=0, tipo='Humano'):
        self.x = x
        self.y = y
        self.tipo = tipo


def seleccionar_personaje():
    global jugador
    dialogo = tk.Toplevel(ventana)
    dialogo.title("Seleccionar Personaje")
    tk.Label(dialogo, text="Elige un personaje:").pack(pady=10)

    combobox = ttk.Combobox(dialogo, values=["Humano", "Mono", "Pulpo", "Pie Grande"], state="readonly")
    combobox.pack(pady=10, padx=10)
    combobox.set("Humano")

    def confirmar_seleccion():
        global jugador
        jugador.tipo = combobox.get()  # Asignamos el tipo al objeto jugador
        print(f"Tipo de jugador seleccionado: {jugador.tipo}")  # Añadir esta línea
        dialogo.destroy()

    btn_confirmar = tk.Button(dialogo, text="Confirmar", command=confirmar_seleccion)
    btn_confirmar.pack(pady=10)
    ventana.wait_window(dialogo)
personaje_seleccionado = ""

def mostrar_info(x, y):
    tipo_terreno = {
        '0': "Montaña",
        '1': "Pradera",
        '2': "Agua",
        '3': "Arena",
        '4': "Bosque",
        '5': "Pantano",
        '6': "Nieve"
    }.get(m[x][y], "Desconocido")
    valor = m[x][y]
    estado_jugador = "El jugador ha pasado por aquí" if visitados[x][y] else "El jugador no ha pasado por aquí"
    
    respuesta = messagebox.askyesnocancel("Información", f"Estado: {estado_jugador}\n\nCoordenadas: ({x}, {y})\n\nTipo de terreno: {tipo_terreno}\n\n¿Deseas modificar esta casilla?")
    
    if respuesta == True:
        nuevo_valor = simpledialog.askstring("Modificar Casilla", "Ingresa el nuevo valor (0-6):")
        if nuevo_valor in ['0', '1', '2', '3', '4', '5', '6']:
            m[x][y] = nuevo_valor
            botones[x][y].config(bg=colores[nuevo_valor], text=nuevo_valor)

def actualizar_colores_casillas():
    for i in range(len(m)):
        for j in range(len(m[i])):
            # Si la casilla es adyacente al jugador, la pintas con su color original.
            if (i == jugador.x and (j == jugador.y - 1 or j == jugador.y + 1)) or (j == jugador.y and (i == jugador.x - 1 or i == jugador.x + 1)):
                botones[i][j].config(bg=colores[m[i][j]])
            # Si la casilla no ha sido visitada, la pintas de gris.
            elif not visitados[i][j]:
                botones[i][j].config(bg="#D3D3D3")  # Color gris

            # Aquí es donde modificamos el texto de los botones.
            if visitados[i][j]:
                botones[i][j].config(text="X")
            else:
                botones[i][j].config(text="O")

def actualizar_contador():
    mensaje_contador.config(text=f"El número que llevas es: {contador.get()}")

def mover_jugador(x, y):
    print(f"Intentando mover al jugador de tipo: {jugador.tipo}")  # Añadir esta línea
    if 0 <= x < len(m) and 0 <= y < len(m[0]):
        valor_casilla = int(m[x][y])
        if jugador.tipo == 'Humano':
            if m[x][y] == '0':  # Montaña
                return  # No puede moverse, por lo que simplemente retornamos sin hacer nada
            elif m[x][y] == '1':
                contador.set(contador.get() + 1)
            elif m[x][y] == '2':
                contador.set(contador.get() + 2)
            elif m[x][y] == '3':
                contador.set(contador.get() + 3)
            elif m[x][y] == '4':
                contador.set(contador.get() + 4)
            elif m[x][y] == '5':
                contador.set(contador.get() + 5)
            elif m[x][y] == '6':
                contador.set(contador.get() + 6)
    
        elif jugador.tipo == 'Mono':
            if m[x][y] == '0':  # Montaña
                return  # No puede moverse, por lo que simplemente retornamos sin hacer nada
            elif m[x][y] == '1':
                contador.set(contador.get() + 2)
            elif m[x][y] == '2':
                contador.set(contador.get() + 4)
            elif m[x][y] == '3':
                contador.set(contador.get() + 3)
            elif m[x][y] == '4':
                contador.set(contador.get() + 1)
            elif m[x][y] == '5':
                contador.set(contador.get() + 5)
            elif m[x][y] == '6':
                return
        
        elif jugador.tipo == 'Pulpo':
            if m[x][y] == '0':  # Montaña
                return  # No puede moverse, por lo que simplemente retornamos sin hacer nada
            elif m[x][y] == '1':
                contador.set(contador.get() + 2)
            elif m[x][y] == '2':
                contador.set(contador.get() + 1)
            elif m[x][y] == '3':
                return
            elif m[x][y] == '4':
                contador.set(contador.get() + 3)
            elif m[x][y] == '5':
                contador.set(contador.get() + 2)
            elif m[x][y] == '6':
                return

        elif jugador.tipo == 'Pie Grande':
            if m[x][y] == '0':  # Montaña
                contador.set(contador.get() + 15)
            elif m[x][y] == '1':
                contador.set(contador.get() + 4)
            elif m[x][y] == '2':
                return
            elif m[x][y] == '3':
                return
            elif m[x][y] == '4':
                contador.set(contador.get() +4)
            elif m[x][y] == '5':
                contador.set(contador.get() + 5)
            elif m[x][y] == '6':
                contador.set(contador.get() + 3)

        boton_anterior = botones[jugador.x][jugador.y]
        boton_anterior.config(bg=colores[m[jugador.x][jugador.y]])
        
        jugador.x, jugador.y = x, y
        actualizar_colores_casillas()
        botones[jugador.x][jugador.y].config(bg='red')
        
        visitados[jugador.x][jugador.y] = True
        actualizar_contador()

        if (jugador.x, jugador.y) == (fin_x, fin_y):
            messagebox.showinfo("Victoria", f"Has llegado al final!\n\nPuntuación: {contador.get()}")


def manejar_teclas(event):
    if event.keysym == 'Up':
        mover_jugador(jugador.x - 1, jugador.y)
    elif event.keysym == 'Down':
        mover_jugador(jugador.x + 1, jugador.y)
    elif event.keysym == 'Left':
        mover_jugador(jugador.x, jugador.y - 1)
    elif event.keysym == 'Right':
        mover_jugador(jugador.x, jugador.y + 1)

# Leer el archivo y preparar el mapa
with open("prueba.txt", "r") as archivo:
    contenido = archivo.read()

filas = contenido.split('\n')
m = [list(fila.strip()) for fila in filas if fila.strip()]
visitados = [[False for _ in range(len(m[0]))] for _ in range(len(m))]

colores = {
    '0': "#D2691E",  # Montaña
    '1': "#B8860B",  # Pradera
    '2': "#00BFFF",  # Agua
    '3': "#F0E68C",  # Arena
    '4': "#3CB371",  # Bosque
    '5': "#800080",  # Pantano (morado)
    '6': "#FFFFFF"   # Nieve (blanco)
}

ventana = tk.Tk()
ventana.title("Botones de caracteres")
ventana.bind('<Key>', manejar_teclas)
ventana.focus_set()


jugador = Jugador()
seleccionar_personaje()

ventana_contador = tk.Toplevel(ventana)
ventana_contador.title("Contador")
mensaje_contador = tk.Label(ventana_contador, text="")
mensaje_contador.pack(pady=20, padx=20)

inicio_x = simpledialog.askinteger("Inicio", "Coordenada X de inicio:", minvalue=0, maxvalue=len(m)-1)
inicio_y = simpledialog.askinteger("Inicio", "Coordenada Y de inicio:", minvalue=0, maxvalue=len(m[0])-1)
jugador.x = inicio_x
jugador.y = inicio_y
fin_x = simpledialog.askinteger("Final", "Coordenada X final:", minvalue=0, maxvalue=len(m)-1)
fin_y = simpledialog.askinteger("Final", "Coordenada Y final:", minvalue=0, maxvalue=len(m[0])-1)

visitados[jugador.x][jugador.y] = True

contador = tk.IntVar(value=int(m[inicio_x][inicio_y]))
actualizar_contador()

botones = []
for i in range(len(m)):
    fila_botones = []
    for j in range(len(m[i])):
        # Elimina la asignación de "texto = char" y solo usa "texto" para marcar inicio y final
        if (i, j) == (inicio_x, inicio_y):
            texto = "I"
        elif (i, j) == (fin_x, fin_y):
            texto = "F"
        else:
            texto = ""  # Esta línea asegura que las casillas normales no tengan texto

        boton = tk.Button(ventana, text=texto, bg="#D3D3D3", command=lambda x=i, y=j: mostrar_info(x, y))
        boton.grid(row=i, column=j, padx=5, pady=5)
        fila_botones.append(boton)
    botones.append(fila_botones)


# Ahora que todos los botones están creados, actualizamos sus colores.
actualizar_colores_casillas()

ventana.mainloop()