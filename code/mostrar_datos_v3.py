# mostrar_datos_v3.py
# Ventana que muestra datos filtrados por una edad mínima ingresada por el usuario.

print("📊 Creando ventana con filtro de edad dinámico...")

# Importar librerías
import tkinter as tk
from tkinter import messagebox # Para mostrar mensajes de error
import mysql.connector

# Variables globales para los widgets que necesitamos actualizar o leer
ventana = None
etiqueta_estado = None
etiqueta_cantidad = None
etiqueta_personas = None
entrada_edad = None # Nuevo: para el campo de entrada de edad

def obtener_datos_dinamicos(edad_minima_str):
    """
    Se conecta a MySQL y obtiene información de la base de datos,
    filtrando personas mayores a la edad_minima especificada.
    
    Retorna:
    - conectado: True si la conexión funciona, False si no
    - cantidad: Número de personas que cumplen el filtro (0 si hay error o edad inválida)
    - personas: Lista de tuplas [(nombre, edad), ...] (vacía si hay error o edad inválida)
    - mensaje_filtro: Un string indicando el estado del filtro o error.
    """
    try:
        edad_minima = int(edad_minima_str)
        if edad_minima < 0:
            # Consideramos edades negativas como inválidas también
            return False, 0, [], "Edad inválida (debe ser >= 0)"
    except ValueError:
        return False, 0, [], "Edad inválida (debe ser un número)"

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="mi_primera_db"
        )
        
        if conexion.is_connected():
            cursor = conexion.cursor()
            
            # Consultas parametrizadas para seguridad
            sql_contar = "SELECT COUNT(*) FROM personas WHERE edad > %s"
            sql_seleccionar = "SELECT nombre, edad FROM personas WHERE edad > %s ORDER BY nombre"
            
            cursor.execute(sql_contar, (edad_minima,))
            cantidad = cursor.fetchone()[0]
            
            cursor.execute(sql_seleccionar, (edad_minima,))
            personas = cursor.fetchall()
            
            cursor.close()
            conexion.close()
            
            return True, cantidad, personas, f"Edad > {edad_minima}"
        else:
            return False, 0, [], "No conectado a DB"
            
    except Exception as error:
        print(f"Error al obtener datos: {error}")
        return False, 0, [], f"Error DB: {error}"

def actualizar_ventana():
    """
    Actualiza la información mostrada en la ventana según la edad mínima ingresada.
    """
    global etiqueta_estado, etiqueta_cantidad, etiqueta_personas, entrada_edad, ventana
    print("🔄 Actualizando datos con filtro dinámico...")
    
    edad_ingresada = entrada_edad.get() # Obtener valor del Entry
    
    conectado, cantidad, personas, mensaje_filtro = obtener_datos_dinamicos(edad_ingresada)
    
    if conectado:
        color = "#28a745"  # Verde
        estado_conexion = "✅ CONECTADO"
        estado_final = f"{estado_conexion} (Filtro: {mensaje_filtro})"
        info_cantidad_texto = f"👥 Personas ({mensaje_filtro}): {cantidad}"
        
        if cantidad > 0:
            lista_personas_texto = f"📋 Lista de personas ({mensaje_filtro}):\n"
            for nombre, edad_persona in personas:
                lista_personas_texto += f"   • {nombre} ({edad_persona} años)\n"
        else:
            lista_personas_texto = f"📋 No hay personas que cumplan el filtro: {mensaje_filtro}"
            
    else:
        color = "#dc3545"  # Rojo
        estado_final = f"❌ {mensaje_filtro}" # Mostrar el error específico
        if mensaje_filtro.startswith("Edad inválida"):
            messagebox.showerror("Error de Entrada", mensaje_filtro.replace("Edad inválida", "La edad mínima ingresada es inválida."))
            info_cantidad_texto = "🔢 Ingrese una edad válida"
            lista_personas_texto = ""
        else: # Error de conexión o DB
            info_cantidad_texto = "❌ No se pudo conectar a MySQL o error en DB"
            lista_personas_texto = "💡 Revisa que XAMPP esté funcionando y la consola para errores"

    ventana.configure(bg=color)
    etiqueta_estado.configure(text=estado_final, bg=color)
    etiqueta_cantidad.configure(text=info_cantidad_texto, bg=color)
    etiqueta_personas.configure(text=lista_personas_texto, bg=color)
    
    print(f"✅ Ventana actualizada: {estado_final}")

def crear_ventana():
    """
    Crea la ventana principal con todos los elementos, incluyendo el campo de edad.
    """
    global ventana, etiqueta_estado, etiqueta_cantidad, etiqueta_personas, entrada_edad
    
    print("🖼️ Creando ventana para filtro dinámico...")
    
    ventana = tk.Tk()
    ventana.title("Datos con Filtro de Edad Dinámico")
    ventana.geometry("500x420") 
    ventana.resizable(False, False)
    
    # Color de fondo base para los labels de información
    # Usaremos el color de fondo de la ventana para el frame_edad y sus labels internos
    # para asegurar consistencia si se cambia el color de fondo de la ventana principal.
    # Inicialmente, la ventana tendrá un color que se actualizará en actualizar_ventana.
    # Por ahora, podemos usar un color neutro o el que se usará cuando esté conectado.
    color_fondo_inicial_ventana = "#4A4A4A" # Un gris oscuro como placeholder
    ventana.configure(bg=color_fondo_inicial_ventana)

    etiqueta_estado = tk.Label(ventana, text="🔍 Verificando...", font=("Arial", 16, "bold"), fg="white", bg=ventana.cget('bg'))
    etiqueta_estado.pack(pady=10)

    # Sección para entrada de edad
    # El frame_edad y sus labels internos tomarán el color de fondo de la ventana principal
    frame_edad = tk.Frame(ventana, bg=ventana.cget('bg')) 
    frame_edad.pack(pady=5)
    tk.Label(frame_edad, text="Edad Mínima:", font=("Arial", 11), fg="white", bg=frame_edad.cget('bg')).pack(side=tk.LEFT, padx=5)
    entrada_edad = tk.Entry(frame_edad, font=("Arial", 11), width=5)
    entrada_edad.pack(side=tk.LEFT)
    entrada_edad.insert(0, "0") # Valor por defecto inicial
    
    etiqueta_cantidad = tk.Label(ventana, text="⏳ Obteniendo datos...", font=("Arial", 11), fg="white", bg=ventana.cget('bg'))
    etiqueta_cantidad.pack(pady=5)
    
    etiqueta_personas = tk.Label(ventana, text="📊 Cargando información...", font=("Arial", 10), fg="white", bg=ventana.cget('bg'), justify=tk.LEFT)
    etiqueta_personas.pack(pady=10, fill=tk.X, padx=20)
    
    boton_refrescar = tk.Button(ventana, text="🔄 Refrescar Datos", font=("Arial", 11), command=actualizar_ventana, bg="#17a2b8", fg="white", width=15)
    boton_refrescar.pack(pady=5)
    
    boton_cerrar = tk.Button(ventana, text="❌ Cerrar", font=("Arial", 11), command=ventana.destroy, bg="#6c757d", fg="white", width=15)
    boton_cerrar.pack(pady=5)
    
    print("✅ Ventana creada")
    actualizar_ventana() # Carga inicial de datos
    return ventana

# ================================================
# PROGRAMA PRINCIPAL
# ================================================
def main():
    """
    Función principal que ejecuta todo el programa.
    """
    print("🚀 Iniciando programa con filtro de edad dinámico")
    print("=" * 50)
    
    try:
        import mysql.connector
        print("✅ mysql.connector disponible")
    except ImportError:
        print("❌ Error: mysql.connector no está instalado")
        print("💡 Ejecuta: pip install mysql-connector-python")
        return
    
    ventana_principal = crear_ventana()
    ventana_principal.mainloop()
    
    print("\n👋 ¡Programa de filtro dinámico terminado!")

if __name__ == "__main__":
    main()