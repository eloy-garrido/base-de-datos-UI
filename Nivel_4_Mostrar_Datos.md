# Nivel 4: Mostrar Datos de la Base

## 🎯 Objetivo
Crear una ventana que no solo muestre si estamos conectados, sino también QUÉ datos hay en nuestra base de datos.

---

## 📋 Prerrequisitos
- ✅ Nivel 0 completado (Python instalado)
- ✅ Nivel 1 completado (MySQL funcionando)
- ✅ Nivel 2 completado (test de consola)
- ✅ Nivel 3 completado (primera ventana simple)

---

## 📚 Conceptos Nuevos (Solo 3)

### **¿Qué vamos a aprender?**
1. **Consultas SQL desde Python**: Hacer preguntas a la base de datos (¿cuántas personas hay? ¿cuáles son sus nombres?)
2. **Múltiples elementos visuales**: Organizar varios textos en una ventana
3. **Botón con función**: Crear un botón que haga algo útil (refrescar datos)

### **¿Qué va a mostrar la ventana?**
- Estado de conexión (como en Nivel 3)
- Cantidad de personas en la tabla
- Lista con nombres y edades
- Botón "Refrescar" para actualizar los datos
- Botón "Cerrar" para salir

---

## 💻 Paso 1: Crear el Programa

### **1.1 Crear el archivo**
1. Ve a tu carpeta `Mi_Proyecto_Base_Datos/codigo/`
2. Crea un archivo nuevo llamado `mostrar_datos.py`

### **1.2 Escribir el código completo**

```python
# mostrar_datos.py
# Ventana que muestra los datos de la base de datos

print("📊 Creando ventana con datos de la base...")

# Importar librerías
import tkinter as tk
import mysql.connector

def obtener_datos():
    """
    Se conecta a MySQL y obtiene información de la base de datos.
    
    Retorna:
    - conectado: True si la conexión funciona, False si no
    - cantidad: Número de personas en la tabla (0 si hay error)
    - personas: Lista de tuplas [(nombre, edad), ...] (vacía si hay error)
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
```

---

## 🔍 Explicación de los Nuevos Conceptos

### **1. Función obtener_datos():**
```python
cursor.execute("SELECT COUNT(*) FROM personas")
cantidad = cursor.fetchone()[0]

cursor.execute("SELECT nombre, edad FROM personas ORDER BY nombre")
personas = cursor.fetchall()
```
**¿Qué hace?**
- `COUNT(*)` cuenta cuántas filas hay en la tabla
- `fetchone()` trae UNA respuesta (la cantidad)
- `fetchall()` trae TODAS las respuestas (lista de personas)
- `ORDER BY nombre` ordena alfabéticamente

### **2. Múltiples elementos en la ventana:**
```python
etiqueta_estado = tk.Label(...)     # Estado de conexión
etiqueta_cantidad = tk.Label(...)   # Cantidad de personas  
etiqueta_personas = tk.Label(...)   # Lista de personas
```
**¿Qué hace?**
- Crear varios `Label` para mostrar diferente información
- Cada uno tiene su propio tamaño de fuente y posición
- Se organizan uno debajo del otro con `pack()`

### **3. Botón con función personalizada:**
```python
boton_refrescar = tk.Button(
    command=actualizar_ventana    # Función que se ejecuta al hacer clic
)
```
**¿Qué hace?**
- `command=` dice qué función ejecutar cuando se presiona el botón
- `actualizar_ventana()` vuelve a consultar la base de datos
- La ventana se actualiza sin cerrarse

---

## ▶️ Paso 2: Ejecutar el Programa

### **2.1 Preparativos**
1. ✅ XAMPP ejecutándose
2. ✅ MySQL verde en XAMPP  
3. ✅ Nivel 3 funcionó correctamente

### **2.2 Ejecutar**
1. Abre cmd
2. Ve a tu carpeta:
   ```bash
   cd Desktop/Mi_Proyecto_Base_Datos/codigo
   ```
3. Ejecuta:
   ```bash
   python mostrar_datos.py
   ```

### **2.3 ¿Qué deberías ver?**

**En la consola:**
```
📊 Creando ventana con datos de la base...
🚀 Iniciando programa mostrar datos
=============================================
✅ mysql.connector disponible
🔍 Creando interfaz con datos de la base...
🖼️ Creando ventana...
✅ Ventana creada con todos los elementos
🔄 Actualizando datos...
✅ Ventana actualizada: ✅ CONECTADO
📱 Mostrando ventana...
💡 Usa el botón 'Refrescar' para actualizar los datos
💡 Cierra la ventana cuando termines
```

**Y una ventana que se ve así (si todo funciona):**

```
┌─────────────────────────────────┐
│        ✅ CONECTADO             │
│                                 │
│    👥 Personas en la base: 3    │
│                                 │
│    📋 Lista de personas:        │
│       • Carlos (20 años)        │
│       • Juan (25 años)          │
│       • María (30 años)         │
│                                 │
│        [ 🔄 Refrescar ]         │
│        [   ❌ Cerrar   ]        │
└─────────────────────────────────┘
```

### **2.4 ¿Cómo probar el botón Refrescar?**

1. **La ventana está abierta y funcionando**
2. **Ve a MySQL Workbench** (o phpMyAdmin)
3. **Agrega una nueva persona:**
   ```sql
   INSERT INTO personas (nombre, edad) VALUES ('Ana', 28);
   ```
4. **Vuelve a la ventana de Python**
5. **Haz clic en "🔄 Refrescar"**
6. **¡Deberías ver que ahora aparece Ana en la lista!**

---

## 🛠️ Solución de Problemas

### **❌ Ventana roja con "NO CONECTADO"**
**Significa:** MySQL no funciona
**Solución:**
1. ¿XAMPP está abierto?
2. ¿MySQL está verde?
3. ¿El Nivel 3 funcionó?

### **❌ Muestra "0 personas" pero deberían haber 3**
**Problema:** La tabla está vacía o el nombre de tabla es incorrecto
**Solución:** Ve a MySQL Workbench y ejecuta:
```sql
SELECT * FROM personas;
```
Si no hay datos, ejecuta:
```sql
INSERT INTO personas (nombre, edad) VALUES 
('Juan', 25), ('María', 30), ('Carlos', 20);
```

### **❌ El botón "Refrescar" no hace nada**
**Problema:** Error en la función `actualizar_ventana`
**Solución:** Revisa la consola para ver si hay mensajes de error

### **❌ Error: "No module named 'mysql'"**
**Solución:**
```bash
pip install mysql-connector-python
```

---

## 🎨 Personalización (Opcional)

### **Cambiar el tamaño de la ventana:**
```python
ventana.geometry("500x400")  # Más grande
```

### **Agregar más información:**
Puedes modificar la consulta para mostrar más datos:
```python
cursor.execute("SELECT id, nombre, edad FROM personas ORDER BY edad")
```

### **Cambiar colores del botón:**
```python
boton_refrescar = tk.Button(
    bg="#28a745",    # Verde
    fg="white"
)
```

---

## ✅ Lista de Verificación

Al completar este nivel deberías:
- [ ] Ver una ventana más grande que en el Nivel 3
- [ ] Ver el estado "✅ CONECTADO" (si MySQL funciona)
- [ ] Ver la cantidad de personas (ejemplo: "👥 Personas en la base: 3")
- [ ] Ver la lista de nombres y edades
- [ ] Poder hacer clic en "🔄 Refrescar" y que actualice la información
- [ ] Poder cerrar la ventana con "❌ Cerrar"

---

## 🎓 ¡Excelente Progreso!

Has logrado crear una aplicación que:
- ✅ **Se conecta a MySQL** (del Nivel 3)
- ✅ **Muestra datos reales** de la base de datos (NUEVO)
- ✅ **Hace consultas SQL** desde Python (NUEVO)
- ✅ **Actualiza información** sin cerrar la ventana (NUEVO)
- ✅ **Organiza múltiples elementos** visuales (NUEVO)

**¿Qué aprendiste de nuevo?**
- Hacer consultas SQL (SELECT, COUNT) desde Python
- Usar `fetchone()` y `fetchall()` para obtener resultados
- Organizar múltiples elementos en una ventana
- Crear botones que ejecutan funciones personalizadas
- Actualizar la interfaz sin cerrar la ventana

**🚀 Ideas para el próximo nivel:**
- Agregar datos nuevos desde la ventana
- Editar o eliminar personas existentes
- Buscar personas por nombre
- Conectar a diferentes bases de datos

**Tiempo estimado:** 15-20 minutos

¡Ya tienes una aplicación real que muestra datos de una base de datos! 🎉