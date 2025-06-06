print("📊 Creando ventana con datos de la base...")

# Importar librerías
import tkinter as tk
import mysql.connector

def obtener_datos():
    try:
        # Conectar a MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="mi_primera_db"
        )
        
        if conexion.is_connected():
            cursor = conexion.cursor()
            
            # Consulta 1: Contar cuántas personas hay
            cursor.execute("SELECT COUNT(*) FROM personas")
            cantidad = cursor.fetchone()[0]
            
            # Consulta 2: Obtener nombres y edades
            cursor.execute("SELECT nombre, edad FROM personas ORDER BY nombre")
            personas = cursor.fetchall()
            
            # Cerrar conexión
            cursor.close()
            conexion.close()
            
            return True, cantidad, personas
        else:
            return False, 0, []
            
    except Exception as error:
        print(f"Error al obtener datos: {error}")
        return False, 0, []

def actualizar_ventana():
    """
    Actualiza la información mostrada en la ventana.
    Esta función se ejecuta cuando presionas "Refrescar".
    """
    print("🔄 Actualizando datos...")
    
    # Obtener datos frescos de la base de datos
    conectado, cantidad, personas = obtener_datos()
    
    # Decidir colores y mensajes según el resultado
    if conectado:
        color = "#28a745"  # Verde
        estado = "✅ CONECTADO"
        info_cantidad = f"👥 Personas en la base: {cantidad}"
        
        # Crear texto con la lista de personas
        if cantidad > 0:
            lista_personas = "📋 Lista de personas:\n"
            for nombre, edad in personas:
                lista_personas += f"   • {nombre} ({edad} años)\n"
        else:
            lista_personas = "📋 No hay personas en la base de datos"
            
    else:
        color = "#dc3545"  # Rojo
        estado = "❌ NO CONECTADO"
        info_cantidad = "❌ No se pudo conectar a MySQL"
        lista_personas = "💡 Revisa que XAMPP esté funcionando"
    
    # Actualizar el color de fondo de la ventana
    ventana.configure(bg=color)
    
    # Actualizar todos los textos
    etiqueta_estado.configure(text=estado, bg=color)
    etiqueta_cantidad.configure(text=info_cantidad, bg=color)
    etiqueta_personas.configure(text=lista_personas, bg=color)
    
    print(f"✅ Ventana actualizada: {estado}")

def crear_ventana():
    """
    Crea la ventana principal con todos los elementos.
    """
    global ventana, etiqueta_estado, etiqueta_cantidad, etiqueta_personas
    
    print("🖼️ Creando ventana...")
    
    # Crear ventana (un poco más grande que en Nivel 3)
    ventana = tk.Tk()
    ventana.title("Datos de MySQL")
    ventana.geometry("400x350")        # Más grande para mostrar más información
    ventana.resizable(False, False)
    
    # ================================================
    # ELEMENTO 1: Estado de conexión (como en Nivel 3)
    # ================================================
    etiqueta_estado = tk.Label(
        ventana,
        text="🔍 Verificando...",    # Texto inicial
        font=("Arial", 18, "bold"),
        fg="white"
    )
    etiqueta_estado.pack(pady=15)
    
    # ================================================
    # ELEMENTO 2: Cantidad de personas (NUEVO)
    # ================================================
    etiqueta_cantidad = tk.Label(
        ventana,
        text="⏳ Obteniendo datos...",   # Texto inicial
        font=("Arial", 12),
        fg="white"
    )
    etiqueta_cantidad.pack(pady=5)
    
    # ================================================
    # ELEMENTO 3: Lista de personas (NUEVO)
    # ================================================
    etiqueta_personas = tk.Label(
        ventana,
        text="📊 Cargando información...",  # Texto inicial
        font=("Arial", 10),
        fg="white",
        justify="left"              # Alinear texto a la izquierda
    )
    etiqueta_personas.pack(pady=10)
    
    # ================================================
    # ELEMENTO 4: Botón Refrescar (NUEVO)
    # ================================================
    boton_refrescar = tk.Button(
        ventana,
        text="🔄 Refrescar",
        font=("Arial", 11),
        command=actualizar_ventana,     # Llamar a actualizar_ventana cuando se haga clic
        bg="#17a2b8",                   # Azul
        fg="white",
        width=12
    )
    boton_refrescar.pack(pady=5)
    
    # ================================================
    # ELEMENTO 5: Botón Cerrar (como en Nivel 3)
    # ================================================
    boton_cerrar = tk.Button(
        ventana,
        text="❌ Cerrar",
        font=("Arial", 11),
        command=ventana.destroy,
        bg="#6c757d",                   # Gris
        fg="white",
        width=12
    )
    boton_cerrar.pack(pady=5)
    
    print("✅ Ventana creada con todos los elementos")
    
    # ================================================
    # CARGAR DATOS INICIALES
    # ================================================
    # Llamar a actualizar_ventana para cargar los datos por primera vez
    actualizar_ventana()
    
    return ventana

# ================================================
# PROGRAMA PRINCIPAL
# ================================================

def main():
    """
    Función principal que ejecuta todo el programa.
    """
    print("🚀 Iniciando programa mostrar datos")
    print("=" * 45)
    
    # Verificar librerías
    try:
        import mysql.connector
        print("✅ mysql.connector disponible")
    except:
        print("❌ Error: mysql.connector no está instalado")
        print("💡 Ejecuta: pip install mysql-connector-python")
        return
    
    print("🔍 Creando interfaz con datos de la base...")
    
    # Crear y mostrar la ventana
    ventana = crear_ventana()
    
    print("📱 Mostrando ventana...")
    print("💡 Usa el botón 'Refrescar' para actualizar los datos")
    print("💡 Cierra la ventana cuando termines")
    
    # Mantener la ventana abierta
    ventana.mainloop()
    
    print("\n👋 ¡Programa terminado!")

# Ejecutar el programa
if __name__ == "__main__":
    main()