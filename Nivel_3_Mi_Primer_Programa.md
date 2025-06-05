# Nivel 2: Mi Primer Programa de Conexión a Base de Datos

## 🎯 Objetivo
Crear un programa Python súper simple que se conecte a MySQL y nos muestre si la conexión funciona.

---

## 📋 Prerrequisitos
- ✅ Nivel 0 completado (Python instalado)
- ✅ Nivel 1 completado (MySQL funcionando con `mi_primera_db`)

---

## 📚 Conceptos Nuevos (Explicados Simple)

### **¿Qué es un programa?**
Un programa es una lista de instrucciones que le damos a la computadora. Es como una receta de cocina: paso 1, paso 2, paso 3, etc.

### **¿Qué significa "conectar a la base de datos"?**
Es como hacer una llamada telefónica entre nuestro programa Python y MySQL. Si la llamada se conecta, podemos enviar y recibir información.

### **Términos de programación:**
- **Variable**: Caja donde guardamos información (como `nombre = "Juan"`)
- **Función**: Conjunto de instrucciones que hace algo específico
- **Importar**: Usar código que otros programadores ya escribieron
- **Try/Except**: "Intenta hacer esto, si no funciona, haz esto otro"

---

## 💻 Paso 1: Crear Nuestro Programa

### **1.1 Crear la carpeta y archivo**
1. Ve a tu Escritorio
2. Abre la carpeta `Mi_Proyecto_Base_Datos`
3. Entra a la carpeta `codigo`
4. Crea un archivo nuevo llamado `test_conexion.py`

### **1.2 Escribir el código completo**

Abre `test_conexion.py` en tu editor de código y escribe este código exactamente:

```python
# test_conexion.py
# Mi primer programa que se conecta a MySQL
# 
# Este programa hace lo siguiente:
# 1. Se conecta a la base de datos MySQL
# 2. Cuenta cuántas personas hay en nuestra tabla
# 3. Muestra los nombres y edades
# 4. Abre una ventana para mostrar si todo funcionó

# ==================================================
# PASO 1: IMPORTAR LIBRERÍAS
# ==================================================
# Una librería es código que otros programadores ya escribieron
# Es como usar una receta que alguien más ya inventó

print("📦 Importando librerías...")

# Importar mysql.connector para hablar con MySQL
# Sin esto, Python no sabría cómo conectarse a bases de datos
import mysql.connector

# Importar tkinter para crear ventanas
# tkinter = "Tk interface" = interfaz gráfica
import tkinter as tk

# Importar messagebox para mostrar mensajes emergentes
from tkinter import messagebox

print("✅ Librerías importadas correctamente")

# ==================================================
# PASO 2: FUNCIÓN PARA PROBAR LA CONEXIÓN
# ==================================================
# Una función es como crear una "mini-máquina" que hace algo específico
# Puedes usar esta máquina cuantas veces quieras

def probar_conexion():
    """
    Esta función intenta conectarse a MySQL.
    
    ¿Qué hace?
    - Usa los datos de conexión (host, puerto, usuario, etc.)
    - Intenta conectarse a MySQL
    - Si funciona: obtiene información de la base de datos
    - Si no funciona: nos dice qué pasó
    
    Retorna:
    - True si la conexión funcionó
    - False si hubo algún problema
    """
    
    print("\n🔍 Iniciando prueba de conexión...")
    
    # --------------------------------------------------
    # DATOS DE CONEXIÓN
    # --------------------------------------------------
    # Estas son las "coordenadas" para encontrar nuestra base de datos
    # Es como tener la dirección y teléfono de alguien antes de visitarlo
    
    host = "localhost"        # localhost = mi propia computadora
    puerto = 3306             # 3306 es el número "telefónico" de MySQL
    usuario = "root"          # root = usuario administrador de MySQL
    password = ""             # Vacía = sin contraseña (configuración de XAMPP)
    base_datos = "mi_primera_db"  # El nombre de nuestra base de datos
    
    # Mostrar los datos que vamos a usar (para verificar)
    print(f"📋 Datos de conexión:")
    print(f"   Host: {host}")
    print(f"   Puerto: {puerto}")
    print(f"   Usuario: {usuario}")
    print(f"   Base de datos: {base_datos}")
    
    # --------------------------------------------------
    # INTENTAR LA CONEXIÓN CON TRY/EXCEPT
    # --------------------------------------------------
    # try/except es como decir:
    # "Intenta hacer esto, si no funciona, no te cierres, mejor dime qué pasó"
    
    try:
        # TRY = "Intenta hacer esto..."
        print("\n🔌 Intentando conectar...")
        
        # Esta línea es MUY IMPORTANTE
        # Le dice a Python: "Conéctate a MySQL usando estos datos"
        conexion = mysql.connector.connect(
            host=host,              # ¿Dónde está MySQL? En localhost
            port=puerto,            # ¿En qué puerto? En 3306
            user=usuario,           # ¿Con qué usuario? Con root
            password=password,      # ¿Con qué contraseña? Ninguna
            database=base_datos     # ¿Qué base de datos usar? mi_primera_db
        )
        
        # Verificar si realmente estamos conectados
        # is_connected() pregunta: "¿Está funcionando la conexión?"
        if conexion.is_connected():
            print("🎉 ¡CONEXIÓN EXITOSA!")
            
            # -----------------------------------------------
            # HACER CONSULTAS A LA BASE DE DATOS
            # -----------------------------------------------
            # Un cursor es como un "mensajero" que lleva nuestras preguntas
            # a la base de datos y nos trae las respuestas
            cursor = conexion.cursor()
            
            # Pregunta 1: ¿Cuántas personas hay en total?
            # COUNT(*) = cuenta todas las filas
            cursor.execute("SELECT COUNT(*) FROM personas")
            
            # fetchone() = "tráeme UNA respuesta"
            # [0] = toma el primer (y único) número de la respuesta
            cantidad = cursor.fetchone()[0]
            
            print(f"📊 Información de la base de datos:")
            print(f"   ✅ Conectado a: {base_datos}")
            print(f"   👥 Personas en la tabla: {cantidad}")
            
            # Pregunta 2: ¿Cuáles son los nombres y edades?
            cursor.execute("SELECT nombre, edad FROM personas")
            
            # fetchall() = "tráeme TODAS las respuestas"
            personas = cursor.fetchall()
            
            print(f"   📋 Lista de personas:")
            # Un bucle for es como decir: "Para cada persona en la lista..."
            for persona in personas:
                # persona[0] = nombre, persona[1] = edad
                print(f"      • {persona[0]} ({persona[1]} años)")
            
            # -----------------------------------------------
            # CERRAR LA CONEXIÓN CORRECTAMENTE
            # -----------------------------------------------
            # Es importante cerrar las conexiones cuando terminamos
            # Es como colgar el teléfono después de hablar
            cursor.close()      # Cerrar el "mensajero"
            conexion.close()    # Cerrar la "llamada telefónica"
            print("\n🔐 Conexión cerrada correctamente")
            
            return True  # Regresa "True" = "Todo salió bien"
            
    except mysql.connector.Error as error:
        # EXCEPT = "Si algo salió mal, haz esto..."
        # mysql.connector.Error = errores específicos de MySQL
        print(f"❌ Error de MySQL: {error}")
        
        # Explicar posibles causas del error
        print("💡 Posibles soluciones:")
        print("   • ¿Está XAMPP ejecutándose?")
        print("   • ¿Está MySQL verde en XAMPP Control Panel?")
        print("   • ¿Existe la base de datos 'mi_primera_db'?")
        
        return False  # Regresa "False" = "Algo salió mal"
        
    except Exception as error:
        # Exception = cualquier otro tipo de error
        print(f"❌ Error general: {error}")
        print("💡 Esto puede ser un problema de configuración de Python")
        
        return False

# ==================================================
# PASO 3: FUNCIÓN PARA CREAR LA VENTANA DE RESULTADO
# ==================================================

def crear_ventana_resultado(conexion_exitosa):
    """
    Esta función crea una ventana para mostrar si la conexión funcionó o no.
    
    Parámetros:
    - conexion_exitosa: True si funcionó, False si no funcionó
    
    ¿Qué hace?
    - Crea una ventana nueva
    - Muestra colores verdes si funcionó, rojos si no funcionó
    - Muestra un mensaje apropiado
    - Agrega un botón para cerrar
    """
    
    print("\n🖼️ Creando ventana de resultado...")
    
    # Crear la ventana principal
    # Tk() crea una ventana vacía
    ventana = tk.Tk()
    
    # Configurar propiedades de la ventana
    ventana.title("🔗 Test de Conexión MySQL")  # Título en la barra superior
    ventana.geometry("450x350")                  # Tamaño: 450x350 píxeles
    ventana.resizable(False, False)              # No permitir cambiar tamaño
    
    # --------------------------------------------------
    # DECIDIR COLORES Y MENSAJES SEGÚN EL RESULTADO
    # --------------------------------------------------
    
    if conexion_exitosa:
        # Si la conexión funcionó = colores verdes y mensaje de éxito
        color_fondo = "#d4edda"    # Verde claro para el fondo
        color_texto = "#155724"    # Verde oscuro para el texto
        emoji = "✅"               # Emoji de éxito
        titulo = "¡CONEXIÓN EXITOSA!"
        
        # Mensaje largo explicando qué significa el éxito
        mensaje = """¡Felicitaciones! 🎉

Tu programa Python se conectó 
correctamente a MySQL.

Esto significa que:
✅ Python está funcionando
✅ MySQL está activo
✅ La base de datos existe
✅ Los datos de conexión son correctos

¡Ya puedes crear aplicaciones 
que trabajen con bases de datos!

Revisa la línea de comandos para 
ver los datos que se obtuvieron."""
        
    else:
        # Si la conexión falló = colores rojos y mensaje de error
        color_fondo = "#f8d7da"    # Rojo claro para el fondo
        color_texto = "#721c24"    # Rojo oscuro para el texto
        emoji = "❌"               # Emoji de error
        titulo = "Error de Conexión"
        
        # Mensaje con sugerencias para resolver el problema
        mensaje = """No se pudo conectar a MySQL 😞

Posibles problemas:
❓ ¿Está XAMPP ejecutándose?
❓ ¿Está MySQL activo (verde)?
❓ ¿Completaste el Nivel 1?
❓ ¿Existe la base de datos 'mi_primera_db'?
❓ ¿Cambiaste el puerto a 3307?

Revisa estos puntos en orden y 
vuelve a ejecutar el programa.

Mira la línea de comandos para 
más detalles del error."""
    
    # --------------------------------------------------
    # CONFIGURAR EL FONDO DE LA VENTANA
    # --------------------------------------------------
    # configure() cambia las propiedades de la ventana
    # bg = background = color de fondo
    ventana.configure(bg=color_fondo)
    
    # --------------------------------------------------
    # CREAR Y POSICIONAR LOS ELEMENTOS VISUALES
    # --------------------------------------------------
    
    # Elemento 1: Emoji grande arriba
    etiqueta_emoji = tk.Label(
        ventana,                    # ¿En qué ventana?
        text=emoji,                 # ¿Qué texto mostrar?
        font=("Arial", 40),         # ¿Qué fuente y tamaño?
        bg=color_fondo,             # ¿Color de fondo?
        fg=color_texto              # ¿Color del texto?
    )
    # pack() coloca el elemento en la ventana
    # pady = padding vertical = espacio arriba y abajo
    etiqueta_emoji.pack(pady=10)
    
    # Elemento 2: Título principal
    etiqueta_titulo = tk.Label(
        ventana,
        text=titulo,
        font=("Arial", 16, "bold"),  # 16 = tamaño, bold = negritas
        bg=color_fondo,
        fg=color_texto
    )
    etiqueta_titulo.pack(pady=5)
    
    # Elemento 3: Mensaje explicativo
    etiqueta_mensaje = tk.Label(
        ventana,
        text=mensaje,
        font=("Arial", 10),
        bg=color_fondo,
        fg=color_texto,
        justify="center"             # justify = alineación del texto
    )
    # padx = padding horizontal = espacio a los lados
    etiqueta_mensaje.pack(pady=10, padx=20)
    
    # Elemento 4: Botón para cerrar la ventana
    boton_cerrar = tk.Button(
        ventana,
        text="Cerrar",               # Texto del botón
        font=("Arial", 12),
        command=ventana.destroy,     # ¿Qué hacer al hacer clic? Cerrar ventana
        bg="#6c757d",                # Color de fondo del botón (gris)
        fg="white"                   # Color del texto del botón (blanco)
    )
    boton_cerrar.pack(pady=10)
    
    print("✅ Ventana creada correctamente")
    
    # --------------------------------------------------
    # MOSTRAR LA VENTANA Y ESPERAR
    # --------------------------------------------------
    # mainloop() = "mantén la ventana abierta hasta que el usuario la cierre"
    # Sin esto, la ventana aparecería y desaparecería inmediatamente
    ventana.mainloop()

# ==================================================
# PASO 4: FUNCIÓN PRINCIPAL
# ==================================================

def main():
    """
    Función principal que ejecuta todo el programa.
    
    ¿Qué hace?
    1. Muestra mensaje de inicio
    2. Llama a probar_conexion()
    3. Muestra el resultado en pantalla
    4. Llama a crear_ventana_resultado()
    5. Muestra mensaje de fin
    
    Esta función coordina todo el programa.
    """
    
    print("🚀 Iniciando programa de test de conexión")
    print("=" * 50)  # Línea decorativa de 50 caracteres "="
    
    # Llamar a la función que prueba la conexión
    # resultado será True si funcionó, False si no funcionó
    resultado = probar_conexion()
    
    # Mostrar línea decorativa y resultado final
    print("\n" + "=" * 50)
    if resultado:
        print("🎯 RESULTADO: Conexión exitosa")
        print("🎉 ¡Tu programa funcionó perfectamente!")
    else:
        print("🎯 RESULTADO: Error de conexión")
        print("🔧 Revisa los mensajes de error arriba para solucionarlo")
    
    # Mostrar ventana gráfica con el resultado
    print("\n📱 Abriendo ventana de resultado...")
    crear_ventana_resultado(resultado)
    
    print("\n👋 ¡Programa terminado!")
    print("💡 Si tuviste éxito, ya sabes cómo conectar Python con MySQL")

# ==================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==================================================

# Esta línea especial verifica si estamos ejecutando este archivo directamente
# Si es así, ejecuta la función main()
# Si alguien importa este archivo desde otro programa, no se ejecuta automáticamente

if __name__ == "__main__":
    # __name__ es una variable especial de Python
    # Si ejecutamos este archivo directamente, __name__ será "__main__"
    # Si importamos este archivo, __name__ será "test_conexion"
    
    main()  # Llamar a la función principal

# ==================================================
# FIN DEL PROGRAMA
# ==================================================

# ¡Felicitaciones! Has escrito tu primer programa que:
# ✅ Se conecta a una base de datos real
# ✅ Obtiene información de una tabla
# ✅ Muestra una interfaz gráfica
# ✅ Maneja errores de forma profesional
# ✅ Está bien documentado y es fácil de entender

# Próximo paso: Expandir este programa para insertar, 
# actualizar o eliminar datos de la base de datos.
```

---

## 🔍 Explicación Detallada por Secciones

### **Sección 1: Importaciones**
```python
import mysql.connector
import tkinter as tk
from tkinter import messagebox
```
**¿Por qué estas librerías?**
- `mysql.connector`: Es el "traductor" entre Python y MySQL
- `tkinter`: Nos permite crear ventanas, botones, mensajes
- `messagebox`: Para mostrar alertas y mensajes emergentes

### **Sección 2: Función probar_conexion()**
**¿Qué hace cada parte?**

**Variables de conexión:**
```python
host = "localhost"
puerto = 3306
usuario = "root"
password = ""
base_datos = "mi_primera_db"
```
- `host`: Dirección del servidor (localhost = tu computadora)
- `puerto`: "Número telefónico" de MySQL (3306 es el estándar)
- `usuario`: Nombre de usuario (root = administrador)
- `password`: Contraseña (vacía en XAMPP por defecto)
- `base_datos`: Nombre de nuestra base de datos

**Try/Except:**
```python
try:
    # Código que puede fallar
except mysql.connector.Error as error:
    # Errores específicos de MySQL
except Exception as error:
    # Cualquier otro error
```
**¿Por qué es importante?** Sin try/except, si algo sale mal, el programa se cierra abruptamente. Con try/except, podemos manejar los errores elegantemente.

### **Sección 3: Función crear_ventana_resultado()**
**¿Qué hace cada elemento?**

**Crear ventana:**
```python
ventana = tk.Tk()
ventana.title("🔗 Test de Conexión MySQL")
ventana.geometry("450x350")
```
- `Tk()`: Crea una ventana vacía
- `title()`: Pone texto en la barra superior
- `geometry()`: Define el tamaño en píxeles

**Elementos visuales:**
```python
etiqueta_emoji = tk.Label(ventana, text=emoji, font=("Arial", 40))
etiqueta_emoji.pack(pady=10)
```
- `Label`: Crea texto que se muestra en la ventana
- `pack()`: Coloca el elemento en la ventana
- `pady`: Espacio vertical alrededor del elemento

### **Sección 4: Función main()**
**¿Por qué existe?**
La función `main()` es como el "director de orquesta" que coordina todo:
1. Inicia el programa
2. Llama a las otras funciones en orden
3. Maneja los resultados
4. Termina el programa

### **Sección 5: if __name__ == "__main__":**
**¿Qué significa esto?**
```python
if __name__ == "__main__":
    main()
```
Es una convención de Python que significa: "Si estamos ejecutando este archivo directamente (no importándolo), entonces ejecuta main()".

---

## ▶️ Paso 2: Ejecutar el Programa

### **2.1 Preparativos**
1. **Asegúrate de que XAMPP esté ejecutándose**
2. **Verifica que MySQL esté verde (Running)**
3. **Confirma que completaste el Nivel 1**

### **2.2 Ejecutar desde la línea de comandos**
1. Abre cmd (línea de comandos)
2. Navega a tu carpeta:
   ```bash
   cd Desktop/Mi_Proyecto_Base_Datos/codigo
   ```
3. Ejecuta el programa:
   ```bash
   python test_conexion.py
   ```

### **2.3 ¿Qué deberías ver?**

**En la línea de comandos (si todo funciona):**
```
📦 Importando librerías...
✅ Librerías importadas correctamente
🚀 Iniciando programa de test de conexión
==================================================
🔍 Iniciando prueba de conexión...
📋 Datos de conexión:
   Host: localhost
   Puerto: 3306
   Usuario: root
   Base de datos: mi_primera_db
🔌 Intentando conectar...
🎉 ¡CONEXIÓN EXITOSA!
📊 Información de la base de datos:
   ✅ Conectado a: mi_primera_db
   👥 Personas en la tabla: 3
   📋 Lista de personas:
      • Juan (25 años)
      • María (30 años)
      • Carlos (20 años)
🔐 Conexión cerrada correctamente
==================================================
🎯 RESULTADO: Conexión exitosa
🎉 ¡Tu programa funcionó perfectamente!
📱 Abriendo ventana de resultado...
✅ Ventana creada correctamente
👋 ¡Programa terminado!
💡 Si tuviste éxito, ya sabes cómo conectar Python con MySQL
```

**Y además aparecerá una ventana verde con el mensaje de éxito! 🎉**

---

## 🛠️ Solución de Problemas

### **Error: "No module named 'mysql'"**
**Problema:** La librería mysql-connector-python no está instalada
**Solución:**
```bash
pip install mysql-connector-python
```

### **Error: "python no se reconoce como comando"**
**Problema:** Python no está en el PATH
**Solución:** Revisa el Nivel 0, sección sobre problemas del PATH

### **Error de conexión a MySQL**
**Problema:** MySQL no está disponible
**Solución paso a paso:**
1. ¿Está XAMPP abierto? Si no, ábrelo
2. ¿Está MySQL verde en XAMPP? Si no, haz clic en "Start"
3. ¿Cambiaste el puerto a 3307? Entonces modifica esta línea en el código:
   ```python
   puerto = 3307  # Cambia de 3306 a 3307
   ```

### **Error: "Database 'mi_primera_db' doesn't exist"**
**Problema:** La base de datos no existe
**Solución:** Vuelve al Nivel 1 y ejecuta el código SQL para crear la base de datos

---

## ✅ Lista de Verificación

Si todo funcionó correctamente, deberías tener:
- [ ] El programa se ejecuta sin errores
- [ ] Aparecen mensajes informativos en la línea de comandos
- [ ] Se abre una ventana verde con "¡CONEXIÓN EXITOSA!"
- [ ] Se muestran los 3 nombres y edades de la base de datos
- [ ] El programa termina correctamente

---

## 🎓 ¡Felicitaciones!

Has creado tu primer programa que:
1. **Se conecta a una base de datos real** ✅
2. **Obtiene información de una tabla** ✅
3. **Muestra una interfaz gráfica** ✅
4. **Maneja errores de forma profesional** ✅
5. **Está completamente documentado** ✅

**¿Qué aprendiste?**
- ✅ Cómo importar y usar librerías
- ✅ Cómo crear y usar funciones
- ✅ Cómo conectar Python con MySQL
- ✅ Cómo ejecutar consultas SQL desde Python
- ✅ Cómo crear ventanas simples
- ✅ Cómo manejar errores con try/except
- ✅ Cómo organizar código de forma profesional

**Próximo paso:** Ahora puedes expandir este programa para hacer operaciones más complejas como insertar, actualizar o eliminar datos.