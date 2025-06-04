# Nivel 3: Mini Interfaz Gráfica de Conexión

## 🎯 Objetivo
Crear una ventana simple que muestre "CONECTADO" o "NO CONECTADO" con colores verde o rojo.

---

## 📋 Prerrequisitos
- ✅ Nivel 0 completado (Python instalado)
- ✅ Nivel 1 completado (MySQL funcionando)
- ✅ Nivel 2 completado (test de consola funcionando)
- 🔧 **IMPORTANTE**: Completar el Paso 0 de este nivel (instalar librerías)

---

## 📚 Conceptos Nuevos

### **¿Qué es una interfaz gráfica?**
Es una ventana con elementos visuales como botones, textos y colores. En lugar de ver solo texto negro en la consola, veremos una ventana bonita.

### **¿Qué es Tkinter?**
Es una librería que viene incluida con Python para crear ventanas. No necesitas instalar nada extra.

### **¿Qué vamos a crear?**
Una ventana simple que:
- Se conecte a MySQL
- Si funciona: fondo verde, texto "CONECTADO"
- Si no funciona: fondo rojo, texto "NO CONECTADO"
- Un botón para cerrar

---

## 🔧 Paso 0: Preparar las Librerías

### **0.1 Verificar que tienes todo lo necesario**
Antes de crear la interfaz, necesitamos asegurarnos de tener todas las librerías:

#### **Librería 1: tkinter (ya incluida con Python)**
- ✅ **Ya tienes**: tkinter viene automáticamente con Python
- ✅ **No necesitas instalar nada**

#### **Librería 2: mysql-connector-python (necesitas instalarla)**
- ❓ **Posiblemente no la tienes**: Esta librería se instala por separado
- 🔧 **Necesitas instalarla**: Sigue el paso siguiente

### **0.2 Instalar mysql-connector-python**

1. **Abre la línea de comandos (cmd)**
2. **Ejecuta este comando:**
   ```bash
   pip install mysql-connector-python
   ```
3. **Espera a que termine** (verás mensajes como "Installing...")
4. **Verifica que se instaló correctamente:**
   ```bash
   pip list | findstr mysql
   ```
   Deberías ver: `mysql-connector-python   8.x.x`

**Si pip no funciona, prueba:**
```bash
python -m pip install mysql-connector-python
```

### **0.3 Verificación rápida**
Para asegurarte de que todo está listo, ejecuta esta prueba rápida:

1. **Abre Python**:
   ```bash
   python
   ```
2. **Prueba importar las librerías**:
   ```python
   import tkinter
   import mysql.connector
   print("¡Todo listo para el Nivel 3!")
   exit()
   ```
3. **Si no hay errores**, ¡estás listo!

---

## 💻 Paso 1: Crear la Interfaz Simple

### **1.1 Crear el archivo**
1. Ve a tu carpeta `Mi_Proyecto_Base_Datos/codigo/`
2. Crea un archivo nuevo llamado `interfaz_simple.py`

### **1.2 Escribir el código**

```python
# interfaz_simple.py
# Mini interfaz gráfica que muestra el estado de conexión

print("🎨 Iniciando interfaz gráfica simple...")

# Importar librerías
import tkinter as tk  # Para crear ventanas
import mysql.connector  # Para conectar con MySQL

def probar_conexion():
    """
    Función que prueba si podemos conectarnos a MySQL.
    Retorna True si funciona, False si no funciona.
    """
    try:
        # Datos de conexión (los mismos del Nivel 2)
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="mi_primera_db"
        )
        
        # Si llegamos aquí, la conexión funcionó
        if conexion.is_connected():
            conexion.close()  # Cerrar la conexión
            return True
        else:
            return False
            
    except:
        # Si hay cualquier error, retornar False
        return False

def crear_ventana():
    """
    Función que crea la ventana y muestra el resultado.
    """
    print("🖼️ Creando ventana...")
    
    # Probar la conexión primero
    conectado = probar_conexion()
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Estado de Conexión MySQL")
    ventana.geometry("400x300")  # Tamaño de la ventana
    ventana.resizable(False, False)  # No permitir cambiar tamaño
    
    # Decidir colores y texto según el resultado
    if conectado:
        # Si está conectado: colores verdes
        color_fondo = "#28a745"  # Verde
        color_texto = "white"    # Blanco
        mensaje_principal = "✅ CONECTADO"
        mensaje_detalle = "La conexión a MySQL\nfunciona correctamente"
        print("✅ Estado: CONECTADO")
    else:
        # Si no está conectado: colores rojos
        color_fondo = "#dc3545"  # Rojo
        color_texto = "white"    # Blanco
        mensaje_principal = "❌ NO CONECTADO"
        mensaje_detalle = "No se pudo conectar\na MySQL"
        print("❌ Estado: NO CONECTADO")
    
    # Configurar el color de fondo de la ventana
    ventana.configure(bg=color_fondo)
    
    # Crear el texto principal (CONECTADO o NO CONECTADO)
    etiqueta_principal = tk.Label(
        ventana,
        text=mensaje_principal,
        font=("Arial", 24, "bold"),  # Fuente grande y negrita
        bg=color_fondo,              # Mismo color de fondo
        fg=color_texto               # Color del texto
    )
    etiqueta_principal.pack(pady=50)  # Agregar a la ventana con espacio vertical
    
    # Crear el texto de detalle
    etiqueta_detalle = tk.Label(
        ventana,
        text=mensaje_detalle,
        font=("Arial", 12),          # Fuente más pequeña
        bg=color_fondo,
        fg=color_texto
    )
    etiqueta_detalle.pack(pady=10)
    
    # Crear botón para cerrar
    boton_cerrar = tk.Button(
        ventana,
        text="Cerrar",
        font=("Arial", 12),
        command=ventana.destroy,     # Cerrar ventana al hacer clic
        bg="white",                  # Fondo blanco del botón
        fg="black",                  # Texto negro del botón
        width=10                     # Ancho del botón
    )
    boton_cerrar.pack(pady=20)
    
    print("✅ Ventana creada correctamente")
    
    # Mostrar la ventana (esto mantiene la ventana abierta)
    ventana.mainloop()

# Función principal
def main():
    """
    Función principal que ejecuta todo el programa.
    """
    print("🚀 Iniciando programa de interfaz simple")
    print("=" * 40)
    
    # Verificar que tenemos las librerías necesarias
    try:
        import mysql.connector
        print("✅ mysql.connector está disponible")
    except:
        print("❌ Error: mysql.connector no está instalado")
        print("💡 Ejecuta: pip install mysql-connector-python")
        return
    
    try:
        import tkinter
        print("✅ tkinter está disponible")
    except:
        print("❌ Error: tkinter no está disponible")
        print("💡 tkinter debería venir con Python")
        return
    
    print("\n🔍 Probando conexión y creando interfaz...")
    
    # Crear y mostrar la ventana
    crear_ventana()
    
    print("\n👋 ¡Programa terminado!")

# Ejecutar el programa
if __name__ == "__main__":
    main()
```

---

## 🔍 Explicación del Código Simple

### **¿Qué hace cada función?**

#### **1. probar_conexion():**
```python
def probar_conexion():
    try:
        conexion = mysql.connector.connect(...)
        if conexion.is_connected():
            conexion.close()
            return True
        else:
            return False
    except:
        return False
```
**Qué hace:** Intenta conectarse y retorna `True` (funciona) o `False` (no funciona).

#### **2. crear_ventana():**
```python
ventana = tk.Tk()
ventana.title("Estado de Conexión MySQL")
ventana.geometry("400x300")
```
**Qué hace:** Crea una ventana de 400x300 píxeles con un título.

#### **3. Elementos visuales:**
```python
etiqueta_principal = tk.Label(
    ventana,
    text=mensaje_principal,
    font=("Arial", 24, "bold"),
    bg=color_fondo,
    fg=color_texto
)
etiqueta_principal.pack(pady=50)
```
**Qué hace:** 
- `Label` = etiqueta de texto
- `font` = tipo y tamaño de letra
- `bg` = color de fondo
- `fg` = color del texto
- `pack()` = colocar en la ventana
- `pady` = espacio vertical

---

## ▶️ Paso 2: Ejecutar el Programa

### **2.1 Preparativos**
1. ✅ XAMPP está ejecutándose
2. ✅ MySQL está verde en XAMPP
3. ✅ El Nivel 2 funcionó correctamente

### **2.2 Ejecutar**
1. Abre cmd
2. Ve a tu carpeta:
   ```bash
   cd Desktop/Mi_Proyecto_Base_Datos/codigo
   ```
3. Ejecuta:
   ```bash
   python interfaz_simple.py
   ```

### **2.3 ¿Qué deberías ver?**

**En la consola:**
```
🎨 Iniciando interfaz gráfica simple...
🚀 Iniciando programa de interfaz simple
========================================
✅ mysql.connector está disponible
✅ tkinter está disponible

🔍 Probando conexión y creando interfaz...
🖼️ Creando ventana...
✅ Estado: CONECTADO
✅ Ventana creada correctamente
👋 ¡Programa terminado!
```

**Y además se abrirá una VENTANA con uno de estos 3 posibles estados:**

**Estado 1: Si falta la librería mysql-connector-python:**
- 🟠 **Fondo naranja**
- 📦 **Texto grande: "LIBRERÍA FALTANTE"**
- 📝 **Texto pequeño: "mysql-connector-python no está instalado"**
- 🔄 **Botón "Probar otra vez"** y **Botón "Cerrar"**

**Estado 2: Si la conexión funciona:**
- 🟢 **Fondo verde**
- ✅ **Texto grande: "CONECTADO"**
- 📝 **Texto pequeño: "La conexión a MySQL funciona correctamente"**
- 🔄 **Botón "Probar otra vez"** y **Botón "Cerrar"**

**Estado 3: Si la conexión NO funciona:**
- 🔴 **Fondo rojo**
- ❌ **Texto grande: "NO CONECTADO"**
- 📝 **Texto pequeño: "No se pudo conectar a MySQL"**
- 🔄 **Botón "Probar otra vez"** y **Botón "Cerrar"**

---

## 🛠️ Solución de Problemas

### **🟠 Ventana naranja (LIBRERÍA FALTANTE)**
**¿Qué significa?** Te falta instalar mysql-connector-python
**¿Cómo se ve?** Ventana naranja con mensaje "mysql-connector-python no está instalado"

**Solución paso a paso:**
1. **Cierra la ventana naranja**
2. **Abre una nueva línea de comandos (cmd)**
3. **Ejecuta exactamente:**
   ```bash
   pip install mysql-connector-python
   ```
4. **Espera a que termine** (verás mensajes como "Installing...")
5. **Vuelve a ejecutar el programa:**
   ```bash
   python interfaz_simple.py
   ```
6. **Ahora debería aparecer ventana verde o roja** (no naranja)

**Si pip no funciona, prueba:**
```bash
python -m pip install mysql-connector-python
```

### **❌ No aparece ninguna ventana**
**Causas posibles:**
1. Error en el código (revisa que copiaste exactamente)
2. Problema con tkinter (debería venir con Python)
3. El programa se cerró por un error

**Solución:**
1. Revisa los mensajes en la consola
2. Si hay errores, cópialos exactamente y busca la solución

### **❌ Ventana roja (NO CONECTADO)**
**Significa:** MySQL no está funcionando
**Solución:**
1. ¿Está XAMPP abierto?
2. ¿Está MySQL verde en XAMPP?
3. ¿Funcionó el Nivel 2?

### **❌ Error: "No module named tkinter"**
**Problema:** tkinter no está disponible (raro)
**Solución:** Reinstala Python desde python.org

### **❌ La ventana se ve mal**
**Solución:** Puedes cambiar el tamaño editando:
```python
ventana.geometry("400x300")  # Cambia los números
```

---

## 🎨 Personalización (Opcional)

### **Cambiar colores:**
```python
# Para conectado
color_fondo = "#28a745"  # Verde (puedes usar otros colores)

# Para no conectado  
color_fondo = "#dc3545"  # Rojo (puedes usar otros colores)
```

### **Cambiar tamaño:**
```python
ventana.geometry("500x400")  # Más grande
ventana.geometry("300x200")  # Más pequeño
```

### **Cambiar texto:**
```python
mensaje_principal = "🎉 ¡TODO BIEN!"  # En lugar de "CONECTADO"
mensaje_detalle = "MySQL funciona\nperfectamente"
```

---

## ✅ Lista de Verificación

Al completar este nivel deberías:
- [ ] Ver una ventana que se abre automáticamente
- [ ] Ver fondo verde y texto "CONECTADO" (si MySQL funciona)
- [ ] Poder cerrar la ventana con el botón "Cerrar"
- [ ] Entender cómo crear interfaces gráficas básicas

---

## 🎓 ¡Excelente Trabajo!

Has logrado:
- ✅ **Crear tu primera interfaz gráfica**
- ✅ **Combinar lógica de programación con elementos visuales**
- ✅ **Mostrar información de forma clara y atractiva**
- ✅ **Usar colores para comunicar estados**
- ✅ **Crear una aplicación completa y funcional**

**¿Qué aprendiste?**
- Cómo usar tkinter para crear ventanas
- Cómo cambiar colores y fuentes
- Cómo organizar elementos en una ventana
- Cómo combinar lógica (conexión) con visual (ventana)

**🚀 Ideas para expandir:**
- Agregar un botón "Probar otra vez"
- Mostrar más información de la base de datos
- Agregar campos para cambiar los datos de conexión
- Crear formularios para insertar datos

**Tiempo estimado:** 20-25 minutos

**¡Felicitaciones! Has creado tu primera aplicación con interfaz gráfica! 🎉**