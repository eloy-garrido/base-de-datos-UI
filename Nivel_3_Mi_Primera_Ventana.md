# Nivel 3: Mi Primera Ventana

## 🎯 Objetivo
Crear una ventana súper simple que muestre "CONECTADO" o "NO CONECTADO" con colores verde o rojo.

---

## 📋 Prerrequisitos
- ✅ Nivel 0 completado (Python instalado)
- ✅ Nivel 1 completado (MySQL funcionando)
- ✅ Nivel 2 completado (test de consola funcionando)

---

## 📚 Conceptos Nuevos (Solo 3)

### **¿Qué es una ventana?**
Una ventana es una caja visual que aparece en tu pantalla, como cuando abres el Bloc de Notas o cualquier programa.

### **¿Qué es tkinter?**
Es la herramienta que viene incluida con Python para crear ventanas. No necesitas instalar nada extra.

### **¿Qué vamos a crear?**
- Una ventana de 300x200 píxeles
- Fondo verde si MySQL funciona, rojo si no funciona
- Texto grande que diga "CONECTADO" o "NO CONECTADO"
- Un botón para cerrar

---

## 💻 Paso 1: Crear el Programa

### **1.1 Crear el archivo**
1. Ve a tu carpeta `Mi_Proyecto_Base_Datos/codigo/`
2. Crea un archivo nuevo llamado `ventana_simple.py`

### **1.2 Escribir el código completo**

```python
# ventana_simple.py
# Mi primera ventana súper simple

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
```

---

## 🔍 Explicación Simple

### **¿Qué hace cada parte?**

**1. Probar conexión:**
```python
conectado = probar_conexion()
```
Antes de crear la ventana, probamos si MySQL funciona. Guardamos el resultado en `conectado` (True o False).

**2. Crear ventana:**
```python
ventana = tk.Tk()
ventana.title("Test MySQL")
ventana.geometry("300x200")
```
- `tk.Tk()` = crear una ventana vacía
- `title()` = poner texto en la barra superior
- `geometry()` = definir el tamaño

**3. Decidir colores:**
```python
if conectado:
    color = "#28a745"    # Verde
    mensaje = "✅ CONECTADO"
else:
    color = "#dc3545"    # Rojo
    mensaje = "❌ NO CONECTADO"
```
Si MySQL funciona: verde. Si no funciona: rojo.

**4. Crear elementos:**
```python
texto = tk.Label(...)
texto.pack(pady=50)
```
- `Label` = crear texto
- `pack()` = colocar en la ventana
- `pady` = espacio vertical

**5. Mostrar ventana:**
```python
ventana.mainloop()
```
Esta línea mantiene la ventana abierta hasta que el usuario la cierre.

---

## ▶️ Paso 2: Ejecutar el Programa

### **2.1 Preparativos**
1. ✅ XAMPP está ejecutándose
2. ✅ MySQL está verde en XAMPP
3. ✅ El Nivel 2 funcionó

### **2.2 Ejecutar**
1. Abre cmd
2. Ve a tu carpeta:
   ```bash
   cd Desktop/Mi_Proyecto_Base_Datos/codigo
   ```
3. Ejecuta:
   ```bash
   python ventana_simple.py
   ```

### **2.3 ¿Qué deberías ver?**

**En la consola:**
```
🎨 Creando mi primera ventana...
🔍 Probando conexión a MySQL...
✅ MySQL funciona - ventana será VERDE
🖼️ Creando ventana...
📱 Mostrando ventana: ✅ CONECTADO
💡 Cierra la ventana cuando termines de verla
👋 Ventana cerrada - programa terminado
```

**Y además se abrirá una VENTANA:**
- 🟢 **Si MySQL funciona**: Ventana verde con "✅ CONECTADO" en grande
- 🔴 **Si MySQL no funciona**: Ventana roja con "❌ NO CONECTADO" en grande
- 🔲 **Botón "Cerrar"** abajo para cerrar la ventana

---

## 🛠️ Solución de Problemas

### **❌ Error: "No module named 'mysql'"**
**Solución:**
```bash
pip install mysql-connector-python
```

### **❌ No aparece ninguna ventana**
**Causas:**
1. Error en el código (revisa que copiaste exactamente)
2. El programa se cerró por un error

**Solución:** Revisa los mensajes en la consola para ver qué error apareció.

### **❌ Ventana roja (NO CONECTADO)**
**Significa:** MySQL no está funcionando
**Solución:**
1. ¿Está XAMPP abierto?
2. ¿Está MySQL verde en XAMPP?
3. ¿Funcionó el Nivel 2?

---

## ✅ Lista de Verificación

Al completar este nivel deberías:
- [ ] Ver una ventana que se abre automáticamente
- [ ] Ver fondo verde y texto "✅ CONECTADO" (si MySQL funciona)
- [ ] Poder cerrar la ventana con el botón "Cerrar"
- [ ] Ver mensajes informativos en la consola

---

## 🎓 ¡Felicitaciones!

Has logrado crear tu primera interfaz gráfica simple que:
- ✅ **Se conecta a MySQL**
- ✅ **Muestra el resultado visualmente**
- ✅ **Usa colores para comunicar el estado**
- ✅ **Tiene un botón funcional**

**¿Qué aprendiste?**
- Cómo crear una ventana básica con tkinter
- Cómo cambiar colores de fondo
- Cómo crear texto y botones
- Cómo combinar lógica (conexión) con visual (ventana)

**Próximo paso:** En el Nivel 4 crearemos una interfaz más completa con más funcionalidades.

**Tiempo estimado:** 10-15 minutos