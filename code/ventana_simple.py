print("🎨 Creando mi primera ventana...")

# Importar librerías
import tkinter as tk
import mysql.connector

def probar_conexion():
    """
    Prueba si MySQL funciona.
    Retorna True si funciona, False si no funciona.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="mi_primera_db"
        )
        if conexion.is_connected():
            conexion.close()
            return True
        return False
    except:
        return False

# ================================================
# PASO 1: Probar conexión antes de crear ventana
# ================================================
print("🔍 Probando conexión a MySQL...")
conectado = probar_conexion()

if conectado:
    print("✅ MySQL funciona - ventana será VERDE")
else:
    print("❌ MySQL no funciona - ventana será ROJA")

# ================================================
# PASO 2: Crear la ventana
# ================================================
print("🖼️ Creando ventana...")

# Crear ventana
ventana = tk.Tk()
ventana.title("Test MySQL")        # Título en la barra superior
ventana.geometry("300x200")        # Tamaño: 300 ancho x 200 alto
ventana.resizable(False, False)    # No permitir cambiar tamaño

# ================================================
# PASO 3: Decidir color y mensaje según el resultado
# ================================================
if conectado:
    color = "#28a745"              # Verde
    mensaje = "✅ CONECTADO"
else:
    color = "#dc3545"              # Rojo
    mensaje = "❌ NO CONECTADO"

# ================================================
# PASO 4: Configurar la ventana
# ================================================

# Poner color de fondo a toda la ventana
ventana.configure(bg=color)

# Crear texto grande en el centro
texto = tk.Label(
    ventana,                       # ¿En qué ventana?
    text=mensaje,                  # ¿Qué texto mostrar?
    font=("Arial", 20, "bold"),    # Fuente grande y negrita
    bg=color,                      # Mismo color de fondo
    fg="white"                     # Texto blanco
)
texto.pack(pady=50)                # Colocar con espacio arriba/abajo

# Crear botón para cerrar
boton = tk.Button(
    ventana,                       # ¿En qué ventana?
    text="Cerrar",                 # Texto del botón
    command=ventana.destroy,       # ¿Qué hacer al hacer clic? Cerrar ventana
    font=("Arial", 12),            # Fuente del botón
    bg="white",                    # Fondo blanco del botón
    fg="black"                     # Texto negro del botón
)
boton.pack(pady=10)                # Colocar con un poco de espacio

# ================================================
# PASO 5: Mostrar la ventana
# ================================================
print(f"📱 Mostrando ventana: {mensaje}")
print("💡 Cierra la ventana cuando termines de verla")

# mainloop() = "mantener la ventana abierta hasta que el usuario la cierre"
ventana.mainloop()

print("👋 Ventana cerrada - programa terminado")