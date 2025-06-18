# mostrar_datos_v2.py
# Ventana que muestra los datos de la base de datos, filtrando por edad > 22

print("📊 Creando ventana con datos filtrados de la base...")

# Importar librerías
import tkinter as tk
import mysql.connector

def obtener_datos_filtrados():
    """
    Se conecta a MySQL y obtiene información de la base de datos,
    filtrando personas mayores de 22 años.
    
    Retorna:
    - conectado: True si la conexión funciona, False si no
    - cantidad: Número de personas mayores de 22 años (0 si hay error)
    - personas: Lista de tuplas [(nombre, edad), ...] de personas mayores de 22 (vacía si hay error)
    """
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
            
            # Consulta 1: Contar cuántas personas MAYORES DE 22 AÑOS hay
            cursor.execute("SELECT COUNT(*) FROM personas WHERE edad > 22")
            cantidad = cursor.fetchone()[0]
            
            # Consulta 2: Obtener nombres y edades de personas MAYORES DE 22 AÑOS
            cursor.execute("SELECT nombre, edad FROM personas WHERE edad > 22 ORDER BY nombre")
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
    print("🔄 Actualizando datos filtrados...")
    
    # Obtener datos frescos y filtrados de la base de datos
    conectado, cantidad, personas = obtener_datos_filtrados() # Usamos la nueva función
    
    # Decidir colores y mensajes según el resultado
    if conectado:
        color = "#28a745"  # Verde
        estado = "✅ CONECTADO (Filtro: Edad > 22)"
        info_cantidad = f"👥 Personas (>22 años) en la base: {cantidad}"
        
        # Crear texto con la lista de personas
        if cantidad > 0:
            lista_personas = "📋 Lista de personas (>22 años):\n"
            for nombre, edad in personas:
                lista_personas += f"   • {nombre} ({edad} años)\n"
        else:
            lista_personas = "📋 No hay personas mayores de 22 años en la base de datos"
            
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
    
    print("🖼️ Creando ventana para datos filtrados...")
    
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Datos Filtrados de MySQL (Edad > 22)")
    ventana.geometry("450x380") # Un poco más ancha para el título largo
    ventana.resizable(False, False)
    
    # ================================================
    # ELEMENTO 1: Estado de conexión
    # ================================================
    etiqueta_estado = tk.Label(
        ventana,
        text="🔍 Verificando...",
        font=("Arial", 18, "bold"),
        fg="white"
    )
    etiqueta_estado.pack(pady=15)
    
    # ================================================
    # ELEMENTO 2: Cantidad de personas (filtradas)
    # ================================================
    etiqueta_cantidad = tk.Label(
        ventana,
        text="⏳ Obteniendo datos...",
        font=("Arial", 12),
        fg="white"
    )
    etiqueta_cantidad.pack(pady=5)
    
    # ================================================
    # ELEMENTO 3: Lista de personas (filtradas)
    # ================================================
    etiqueta_personas = tk.Label(
        ventana,
        text="📊 Cargando información...",
        font=("Arial", 10),
        fg="white",
        justify="left"
    )
    etiqueta_personas.pack(pady=10)
    
    # ================================================
    # ELEMENTO 4: Botón Refrescar
    # ================================================
    boton_refrescar = tk.Button(
        ventana,
        text="🔄 Refrescar",
        font=("Arial", 11),
        command=actualizar_ventana,
        bg="#17a2b8",
        fg="white",
        width=12
    )
    boton_refrescar.pack(pady=5)
    
    # ================================================
    # ELEMENTO 5: Botón Cerrar
    # ================================================
    boton_cerrar = tk.Button(
        ventana,
        text="❌ Cerrar",
        font=("Arial", 11),
        command=ventana.destroy,
        bg="#6c757d",
        fg="white",
        width=12
    )
    boton_cerrar.pack(pady=5)
    
    print("✅ Ventana creada con todos los elementos")
    
    # ================================================
    # CARGAR DATOS INICIALES
    # ================================================
    actualizar_ventana()
    
    return ventana

# ================================================
# PROGRAMA PRINCIPAL
# ================================================

def main():
    """
    Función principal que ejecuta todo el programa.
    """
    print("🚀 Iniciando programa mostrar datos filtrados")
    print("=" * 45)
    
    # Verificar librerías
    try:
        import mysql.connector
        print("✅ mysql.connector disponible")
    except ImportError:
        print("❌ Error: mysql.connector no está instalado")
        print("💡 Ejecuta: pip install mysql-connector-python")
        return
    
    print("🔍 Creando interfaz con datos filtrados de la base...")
    
    # Crear y mostrar la ventana
    ventana_principal = crear_ventana()
    
    print("📱 Mostrando ventana...")
    print("💡 Usa el botón 'Refrescar' para actualizar los datos")
    print("💡 Cierra la ventana cuando termines")
    
    # Mantener la ventana abierta
    ventana_principal.mainloop()
    
    print("\n👋 ¡Programa de datos filtrados terminado!")

if __name__ == "__main__":
    main()