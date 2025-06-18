# Nivel 4.2: Filtro de Edad Dinámico desde la Ventana

## 🎯 Objetivo
Modificar la aplicación para permitir al usuario ingresar una edad mínima en la ventana. La lista de personas se actualizará mostrando solo aquellas que superen la edad ingresada. Para esto, crearemos un nuevo archivo `mostrar_datos_v3.py` basado en `mostrar_datos_v2.py`.

---

## 📋 Prerrequisitos
- ✅ Nivel 4.1 completado (ventana mostrando datos filtrados por edad > 22, usando `mostrar_datos_v2.py`)
- ✅ Entender los conceptos básicos de Tkinter y conexión a MySQL de niveles anteriores.

---

## 📚 Conceptos Nuevos a Aplicar

1.  **Widget `Entry` de Tkinter**: Usaremos este widget para crear un campo de texto donde el usuario pueda escribir la edad mínima.
2.  **Obtener valor de un `Entry`**: Aprenderemos a leer el texto que el usuario ha ingresado en el campo `Entry`.
3.  **Validación básica de entrada**: Implementaremos una verificación simple para asegurar que el usuario ingrese un número válido para la edad.
4.  **Consultas SQL Parametrizadas**: Reforzaremos la práctica de pasar valores a las consultas SQL de forma segura para prevenir vulnerabilidades como la inyección SQL.

### **¿Cómo se verá la ventana?**
- Estado de conexión (como antes).
- Una etiqueta "Edad Mínima:" seguida de un campo de texto para ingresar la edad.
- Información sobre la cantidad de personas que cumplen con el filtro de edad ingresado.
- La lista de nombres y edades de esas personas.
- El botón "Refrescar" que aplicará el filtro de edad.
- El botón "Cerrar".

---

## 💻 Paso 1: Preparar el Nuevo Archivo (`mostrar_datos_v3.py`)

1.  Ve a tu carpeta
2.  Copia el archivo `mostrar_datos_v2.py` y renombra la copia a `mostrar_datos_v3.py`.
    Esto nos da un buen punto de partida.

---

## 💻 Paso 2: Modificar `crear_ventana()` en `mostrar_datos_v3.py`

El primer cambio es agregar el campo de entrada para la edad.

1.  **Declarar `entrada_edad` como global**: Al inicio de la función `crear_ventana()`, asegúrate de que `entrada_edad` esté en la lista de variables globales, ya que la necesitaremos en `actualizar_ventana()`.
    ```python
    # En crear_ventana()
    global ventana, etiqueta_estado, etiqueta_cantidad, etiqueta_personas, entrada_edad # Añadir entrada_edad
    ```

2.  **Añadir el Label y el Entry para la edad**: Justo antes de `etiqueta_cantidad` (o donde prefieras ubicarlo), añade los siguientes widgets. Usaremos un `Frame` para agruparlos horizontalmente.

     ```python
    # ... dentro de crear_ventana(), después de etiqueta_estado.pack()
    
    # Sección para entrada de edad
    frame_edad = tk.Frame(ventana, bg=ventana.cget('bg')) # Usar el color de fondo de la ventana
    frame_edad.pack(pady=5)
    
    tk.Label(frame_edad, text="Edad Mínima:", font=("Arial", 11), fg="white", bg=frame_edad.cget('bg')).pack(side=tk.LEFT, padx=5)
    
    entrada_edad = tk.Entry(frame_edad, font=("Arial", 11), width=5)
    entrada_edad.pack(side=tk.LEFT)
    entrada_edad.insert(0, "0") # Establecer un valor por defecto, por ejemplo "0"
    
    # El resto de los widgets (etiqueta_cantidad, etiqueta_personas, botones) continúan después...
    ```
    *   `ventana.cget('bg')` obtiene el color de fondo actual de la ventana para que el `Frame` se integre bien.
    *   `entrada_edad.insert(0, "0")` pone "0" como texto inicial en el campo de entrada.

---

## 💻 Paso 3: Modificar `obtener_datos_filtrados()` para que sea Dinámica

Ahora, esta función tomará la edad mínima como argumento.

1.  **Renombrar y añadir parámetro**: Cambia el nombre de la función `obtener_datos_filtrados()` a `obtener_datos_dinamicos(edad_minima_str)`.

2.  **Validar la entrada de edad**: Al inicio de `obtener_datos_dinamicos`, convierte `edad_minima_str` a un entero y maneja el caso de que no sea un número válido.

     ```python
    # Al inicio de obtener_datos_dinamicos(edad_minima_str)
    try:
        edad_minima = int(edad_minima_str)
        if edad_minima < 0:
            # Puedes decidir cómo manejar edades negativas, aquí retornamos un error.
            return False, 0, [], "Edad inválida (debe ser >= 0)"
    except ValueError:
        # Si la conversión falla (ej. el usuario escribió 'abc')
        return False, 0, [], "Edad inválida (debe ser un número)"
    ```
    *   La función ahora retorna un cuarto valor: un mensaje sobre el filtro o error.

3.  **Usar consultas parametrizadas**: Modifica las consultas SQL para usar placeholders (`%s`) y pasa la `edad_minima` como un parámetro en una tupla al método `execute()`.

     ```python
    # Dentro del bloque try de la conexión a la base de datos, en obtener_datos_dinamicos()
    # ... (después de que cursor = conexion.cursor())
    
    # Consultas parametrizadas para seguridad
    sql_contar = "SELECT COUNT(*) FROM personas WHERE edad > %s"
    sql_seleccionar = "SELECT nombre, edad FROM personas WHERE edad > %s ORDER BY nombre"
    
    # Ejecutar consultas con el parámetro edad_minima
    cursor.execute(sql_contar, (edad_minima,))
    cantidad = cursor.fetchone()[0]
    
    cursor.execute(sql_seleccionar, (edad_minima,))
    personas = cursor.fetchall()
    
    # ... (cerrar cursor y conexión)
    
    return True, cantidad, personas, f"Edad > {edad_minima}" # Mensaje de filtro exitoso
    ```
    *   **Importante**: `(edad_minima,)` crea una tupla con un solo elemento. `cursor.execute()` espera los parámetros en una tupla o lista.

---

## 💻 Paso 4: Modificar `actualizar_ventana()`

Esta función ahora leerá la edad del `Entry` y usará la nueva función `obtener_datos_dinamicos()`.

1.  **Obtener la edad del `Entry`**: Al inicio de `actualizar_ventana()`, obtén el valor del widget `entrada_edad`.
     ```python
    # Al inicio de actualizar_ventana()
    edad_ingresada = entrada_edad.get()
    ```

2.  **Llamar a `obtener_datos_dinamicos`**: Reemplaza la llamada a `obtener_datos_filtrados()` con una llamada a `obtener_datos_dinamicos(edad_ingresada)`.
     ```python
    # En actualizar_ventana()
    conectado, cantidad, personas, mensaje_filtro = obtener_datos_dinamicos(edad_ingresada)
    ```

3.  **Actualizar las etiquetas de la interfaz**: Ajusta los textos que se muestran en las etiquetas para reflejar el filtro aplicado o los errores.

     ```python
    # En actualizar_ventana(), dentro del if conectado:
    if conectado:
        color = "#28a745"  # Verde
        estado_conexion = "✅ CONECTADO"
        # Usar el mensaje_filtro devuelto por obtener_datos_dinamicos
        estado_final = f"{estado_conexion} (Filtro: {mensaje_filtro})"
        info_cantidad_texto = f"👥 Personas ({mensaje_filtro}): {cantidad}"
        
        if cantidad > 0:
            lista_personas_texto = f"📋 Lista de personas ({mensaje_filtro}):\n"
            for nombre, edad_persona in personas:
                lista_personas_texto += f"   • {nombre} ({edad_persona} años)\n"
        else:
            lista_personas_texto = f"📋 No hay personas que cumplan el filtro: {mensaje_filtro}"
            
    else: # No conectado o error en la edad
        color = "#dc3545"  # Rojo
        estado_final = f"❌ {mensaje_filtro}" # Mostrar el error específico
        
        # Mostrar un messagebox si la edad es inválida para mejor feedback
        if mensaje_filtro.startswith("Edad inválida"):
            # Importar messagebox al inicio del script: from tkinter import messagebox
            messagebox.showerror("Error de Entrada", mensaje_filtro.replace("Edad inválida", "La edad mínima ingresada es inválida."))
            info_cantidad_texto = "🔢 Ingrese una edad válida"
            lista_personas_texto = ""
        else: # Error de conexión o DB
            info_cantidad_texto = "❌ No se pudo conectar a MySQL o error en DB"
            lista_personas_texto = "💡 Revisa que XAMPP esté funcionando y la consola para errores"
    
    # Actualizar el color de fondo de la ventana y las etiquetas...
    ventana.configure(bg=color)
    etiqueta_estado.configure(text=estado_final, bg=color)
    etiqueta_cantidad.configure(text=info_cantidad_texto, bg=color)
    etiqueta_personas.configure(text=lista_personas_texto, bg=color)
    ```
    *   No olvides importar `messagebox` al principio de tu script: `from tkinter import messagebox`.

4.  **Ajustar títulos y mensajes**: Puedes cambiar el título de la ventana en `crear_ventana()` y los mensajes de `print()` en `main()` para reflejar que es la versión con filtro dinámico.

---

## 💻 Paso 5: Pruebas

1.  Asegúrate de tener tu servidor MySQL (XAMPP) en funcionamiento con la base de datos `mi_primera_db` y la tabla `personas` con datos variados.
2.  Ejecuta `mostrar_datos_v3.py` desde tu terminal:
    ```bash
    python mostrar_datos_v3.py
    ```
3.  La ventana debería aparecer con "0" (o el valor por defecto que pusiste) como edad mínima.
4.  Prueba ingresando diferentes números en el campo "Edad Mínima" y presiona "Refrescar".
    *   Verifica que la lista de personas y la cantidad se actualicen correctamente.
5.  Intenta ingresar texto no numérico (ej. "abc") o un número negativo para ver cómo se maneja el error (deberías ver el `messagebox`).

---

¡Felicidades! Has creado una aplicación de escritorio más interactiva que toma entradas del usuario para filtrar datos de una base de datos de forma segura. Has aprendido sobre el widget `Entry`, validación de entradas y la importancia de las consultas parametrizadas.

Este es un gran paso para construir aplicaciones más complejas y útiles.