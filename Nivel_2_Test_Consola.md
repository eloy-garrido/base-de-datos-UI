# Nivel 2: Test de Conexión en Consola

## 🎯 Objetivo
Crear un programa Python súper simple que pruebe si podemos conectarnos a MySQL y nos muestre el resultado en la consola (pantalla negra).

---

## 📋 Prerrequisitos
- ✅ Nivel 0 completado (Python instalado)
- ✅ Nivel 1 completado (MySQL funcionando con `mi_primera_db`)

---

## 📚 Conceptos Básicos

### **¿Qué es la consola?**
La consola (también llamada "línea de comandos" o "cmd") es la pantalla negra donde escribimos comandos. Es donde veremos si nuestro programa funciona.

### **¿Qué vamos a hacer?**
Crear un programa que:
1. Intente conectarse a MySQL
2. Nos diga "SÍ funciona" o "NO funciona"
3. Muestre la información en la consola
4. ¡Y ya! Súper simple.

---

## 💻 Paso 1: Crear Nuestro Programa Simple

### **1.1 Crear el archivo**
1. Ve a tu carpeta `Mi_Proyecto_Base_Datos/codigo/`
2. Crea un archivo nuevo llamado `test_simple.py`

### **1.2 Escribir el código**

Abre `test_simple.py` en tu editor y escribe exactamente esto:

```python
# test_simple.py
# Mi primer programa súper simple que prueba la conexión a MySQL

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
```

---

## 🔍 Explicación del Código (Súper Simple)

### **¿Qué hace cada parte?**

#### **1. Mensaje de inicio:**
```python
print("🚀 Iniciando test de conexión simple...")
```
**Qué hace:** Nos dice que el programa empezó. `print()` muestra texto en la consola.

#### **2. Importar librería:**
```python
try:
    import mysql.connector
    print("✅ Librería mysql.connector importada correctamente")
except:
    print("❌ Error: No se pudo importar mysql.connector")
    exit()
```
**Qué hace:** 
- `import` trae código de otros programadores
- `try/except` significa "intenta esto, si no funciona haz esto otro"
- `exit()` cierra el programa si algo está mal

#### **3. Datos de conexión:**
```python
HOST = "localhost"
PUERTO = 3306
USUARIO = "root"
PASSWORD = ""
BASE_DATOS = "mi_primera_db"
```
**Qué hace:** Guarda la información necesaria para conectar. Son como las "coordenadas" de nuestra base de datos.

#### **4. Intentar conectar:**
```python
conexion = mysql.connector.connect(
    host=HOST,
    port=PUERTO,
    user=USUARIO,
    password=PASSWORD,
    database=BASE_DATOS
)
```
**Qué hace:** Le dice a Python "conéctate a MySQL usando estos datos".

#### **5. Verificar si funcionó:**
```python
if conexion.is_connected():
    print("🎉 ¡ÉXITO! La conexión funciona perfectamente")
```
**Qué hace:** Pregunta "¿está conectado?" y muestra un mensaje de éxito.

---

## ▶️ Paso 2: Ejecutar el Programa

### **2.1 Preparativos**
Antes de ejecutar, asegúrate de:
1. ✅ XAMPP está abierto
2. ✅ MySQL está verde (Running) en XAMPP
3. ✅ Completaste el Nivel 1

### **2.2 Ejecutar**
1. Abre la línea de comandos (cmd)
2. Ve a tu carpeta:
   ```bash
   cd Desktop/Mi_Proyecto_Base_Datos/codigo
   ```
3. Ejecuta el programa:
   ```bash
   python test_simple.py
   ```

### **2.3 ¿Qué deberías ver si todo funciona?**

```
🚀 Iniciando test de conexión simple...
✅ Librería mysql.connector importada correctamente

📋 Intentando conectar con estos datos:
   🏠 Host: localhost
   🔌 Puerto: 3306
   👤 Usuario: root
   🗃️ Base de datos: mi_primera_db

⏳ Conectando...
🎉 ¡ÉXITO! La conexión funciona perfectamente
📊 Hay 3 personas en la base de datos
🔐 Conexión cerrada correctamente

👋 ¡Programa terminado!
💡 Si viste '🎉 ¡ÉXITO!', tu conexión funciona perfectamente
```

### **2.4 ¿Qué deberías ver si algo falla?**

**Si mysql.connector no está instalado:**
```
🚀 Iniciando test de conexión simple...
❌ Error: No se pudo importar mysql.connector
💡 Solución: Ejecuta 'pip install mysql-connector-python'
```

**Si MySQL no está funcionando:**
```
🚀 Iniciando test de conexión simple...
✅ Librería mysql.connector importada correctamente

📋 Intentando conectar con estos datos:
   🏠 Host: localhost
   🔌 Puerto: 3306
   👤 Usuario: root
   🗃️ Base de datos: mi_primera_db

⏳ Conectando...
❌ Error de MySQL: 2003 (HY000): Can't connect to MySQL server on 'localhost:3306'

💡 Posibles soluciones:
   • ¿Está XAMPP ejecutándose?
   • ¿Está MySQL verde en XAMPP?
   • ¿Completaste el Nivel 1?

👋 ¡Programa terminado!
💡 Si viste '🎉 ¡ÉXITO!', tu conexión funciona perfectamente
```

---

## 🛠️ Solución de Problemas

### **❌ Error: "No se pudo importar mysql.connector"**
**Solución:**
```bash
pip install mysql-connector-python
```

### **❌ Error: "python no se reconoce como comando"**
**Solución:** Problema del PATH, revisa el Nivel 0.

### **❌ Error: "Can't connect to MySQL server"**
**Solución paso a paso:**
1. Abre XAMPP Control Panel
2. ¿Está MySQL verde? Si no, haz clic en "Start"
3. ¿Sigue sin funcionar? Reinicia tu computadora
4. ¿Cambiaste el puerto? Modifica `PUERTO = 3307` en el código

### **❌ Error: "Unknown database 'mi_primera_db'"**
**Solución:** No completaste el Nivel 1. Ve a MySQL Workbench y ejecuta:
```sql
CREATE DATABASE mi_primera_db;
USE mi_primera_db;
CREATE TABLE personas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), edad INT);
INSERT INTO personas (nombre, edad) VALUES ('Juan', 25), ('María', 30), ('Carlos', 20);
```

---

## ✅ Lista de Verificación

Al completar este nivel deberías:
- [ ] Ver el mensaje "🎉 ¡ÉXITO! La conexión funciona perfectamente"
- [ ] Ver "📊 Hay 3 personas en la base de datos"
- [ ] No ver ningún mensaje de error
- [ ] Entender cómo funciona el código básico

---

## 🎓 ¡Felicitaciones!

Has logrado:
- ✅ **Escribir tu primer programa** que se conecta a una base de datos
- ✅ **Usar librerías externas** (mysql.connector)
- ✅ **Manejar errores** con try/except
- ✅ **Obtener datos** de una base de datos real
- ✅ **Debugging básico** al resolver problemas

**¿Qué aprendiste?**
- Cómo importar librerías
- Cómo conectar Python con MySQL
- Cómo manejar errores básicos
- Cómo obtener información de una base de datos

**Próximo paso:** En el Nivel 3 crearemos una ventana simple que muestre si estás conectado o no.

**Tiempo estimado:** 15-20 minutos