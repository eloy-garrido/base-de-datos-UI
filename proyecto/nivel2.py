print("🚀 Iniciando test de conexión simple...")

# Importar la librería para conectar con MySQL
try:
    import mysql.connector
    print("✅ Librería mysql.connector importada correctamente")
except:
    print("❌ Error: No se pudo importar mysql.connector")
    print("💡 Solución: Ejecuta 'pip install mysql-connector-python'")
    exit()  # Salir del programa si no hay librería

# Datos de conexión (los mismos del Nivel 1)
HOST = "localhost"
PUERTO = 3306
USUARIO = "root"
PASSWORD = ""  # Vacía para XAMPP
BASE_DATOS = "mi_primera_db"

print(f"\n📋 Intentando conectar con estos datos:")
print(f"   🏠 Host: {HOST}")
print(f"   🔌 Puerto: {PUERTO}")
print(f"   👤 Usuario: {USUARIO}")
print(f"   🗃️ Base de datos: {BASE_DATOS}")

# Intentar la conexión
print(f"\n⏳ Conectando...")

try:
    # Esta línea intenta hacer la conexión
    conexion = mysql.connector.connect(
        host=HOST,
        port=PUERTO,
        user=USUARIO,
        password=PASSWORD,
        database=BASE_DATOS
    )
    # Si llegamos aquí, la conexión funcionó
    if conexion.is_connected():
        print("🎉 ¡ÉXITO! La conexión funciona perfectamente")
        
        # Vamos a obtener información básica
        cursor = conexion.cursor()
        
        # Contar cuántas personas hay
        cursor.execute("SELECT COUNT(*) FROM personas")
        cantidad = cursor.fetchone()[0]
        print(f"📊 Hay {cantidad} personas en la base de datos")

        # Nueva consulta para obtener personas mayores de 22 años
        print("\n👤 Buscando personas mayores de 22 años...")
        # Asumimos que la columna de edad se llama 'edad'
        # y que almacena un valor numérico.
        # Cambia 'nombre_columna_edad' por el nombre real de tu columna de edad.
        # Cambia 'nombre', 'apellido' por las columnas que quieras mostrar.
        consulta_edad = "SELECT nombre, edad FROM personas WHERE edad > 22"
        cursor.execute(consulta_edad)
        
        personas_mayores = cursor.fetchall() # Obtener todos los resultados
        
        if personas_mayores:
            print(f"🔍 Encontradas {len(personas_mayores)} personas mayores de 22 años:")
            for persona in personas_mayores:
                # Asumiendo que las columnas son nombre, apellido, edad en ese orden
                nombre, edad_persona = persona
                print(f"  - {nombre}, Edad: {edad_persona}")
        else:
            print("🤷 No se encontraron personas mayores de 22 años.")
        
        # Cerrar todo correctamente
        cursor.close()
        conexion.close()
        print("🔐 Conexión cerrada correctamente")
        
    else:
        print("❌ Error: No se pudo establecer la conexión")

except mysql.connector.Error as error:
    # Si hay un error de MySQL, mostrar qué pasó
    print(f"❌ Error de MySQL: {error}")
    print("\n💡 Posibles soluciones:")
    print("   • ¿Está XAMPP ejecutándose?")
    print("   • ¿Está MySQL verde en XAMPP?")
    print("   • ¿Completaste el Nivel 1?")

except Exception as error:
    # Si hay cualquier otro error
    print(f"❌ Error general: {error}")

print("\n👋 ¡Programa terminado!")
print("💡 Si viste '🎉 ¡ÉXITO!', tu conexión funciona perfectamente")
