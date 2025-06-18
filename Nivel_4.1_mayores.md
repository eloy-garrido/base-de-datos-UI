# Nivel 4.1: Mostrar Datos Filtrados (Mayores de 22 años)

## 🎯 Objetivo
Modificar la ventana del Nivel 4 para que muestre únicamente las personas de la base de datos que sean mayores de 22 años.

---

## 📋 Prerrequisitos
- ✅ Nivel 4 completado (ventana mostrando todos los datos)

---

## 📚 Conceptos Clave

### **¿Qué vamos a modificar?**
1.  **Consulta SQL con Filtro**: Aprenderemos a usar la cláusula `WHERE` en SQL para seleccionar solo los datos que cumplan una condición específica (edad > 22).
2.  **Adaptación del Código Python**: Ajustaremos la función que obtiene los datos para incorporar este filtro.

### **¿Qué va a mostrar la ventana?**
- Estado de conexión (como en Nivel 4).
- Cantidad de personas **mayores de 22 años** en la tabla.
- Lista con nombres y edades de las personas **mayores de 22 años**.
- Botón "Refrescar" para actualizar los datos (manteniendo el filtro).
- Botón "Cerrar" para salir.

---

## 💻 Paso 1: Entender los Cambios en el Código (`mostrar_datos.py`)

No vamos a crear un archivo Python nuevo, sino que modificaremos el existente: `Mi_Proyecto_Base_Datos/codigo/mostrar_datos.py`.

La idea principal es cambiar cómo la función `obtener_datos()` consulta la base de datos.

### **Modificaciones Clave en `mostrar_datos.py`:**

1.  **Función `obtener_datos()`**:
    *   Debemos cambiar las consultas SQL para que solo seleccionen personas mayores de 22 años.

    Veamos cómo se modificaría la sección de las consultas dentro de `obtener_datos()`:

    ```python
    # ... (inicio de la función obtener_datos sin cambios) ...
    if conexion.is_connected():
        cursor = conexion.cursor()
        
        # Consulta 1: Contar cuántas personas MAYORES DE 22 AÑOS hay
        # MODIFICACIÓN AQUÍ:
        cursor.execute("SELECT COUNT(*) FROM personas WHERE edad > 22")
        cantidad = cursor.fetchone()[0]
        
        # Consulta 2: Obtener nombres y edades de personas MAYORES DE 22 AÑOS
        # MODIFICACIÓN AQUÍ:
        cursor.execute("SELECT nombre, edad FROM personas WHERE edad > 22 ORDER BY nombre")
        personas = cursor.fetchall()
        
        # Cerrar conexión
        cursor.close()
        conexion.close()
        
        return True, cantidad, personas
    # ... (resto de la función sin cambios) ...
    ```

    **Explicación de los cambios:**
    *   `WHERE edad > 22`: Esta es la parte crucial. Le dice a MySQL que solo considere las filas (personas) donde el valor de la columna `edad` sea estrictamente mayor que 22.
    *   Ambas consultas (la que cuenta y la que obtiene los detalles) deben incluir esta condición para que los datos mostrados sean consistentes.

2.  **Función `actualizar_ventana()` y `crear_ventana()`**:
    *   ¡Buena noticia! No se necesitan cambios directos en estas funciones para este objetivo específico. Como `obtener_datos()` ahora devuelve la información ya filtrada, `actualizar_ventana()` simplemente mostrará lo que reciba.

### **¿Cómo probarlo?**

1.  Asegúrate de tener tu servidor MySQL (XAMPP) en funcionamiento y la base de datos `mi_primera_db` con la tabla `personas` creada (como en niveles anteriores).
2.  Añade algunos datos de prueba a tu tabla `personas`, asegurándote de que haya personas con edades variadas (algunas mayores de 22 y otras menores o iguales a 22). Por ejemplo:

    ```sql
    INSERT INTO personas (nombre, edad) VALUES
    ('Ana', 20),
    ('Luis', 25),
    ('Carlos', 30),
    ('Sofía', 22),
    ('Pedro', 28);
    ```

3.  Guarda los cambios en `mostrar_datos.py`.
4.  Ejecuta `mostrar_datos.py` desde tu terminal:
    ```bash
    python mostrar_datos.py
    ```
5.  La ventana debería ahora mostrar solo a Luis (25), Carlos (30) y Pedro (28), y la cantidad debería ser 3.

---

