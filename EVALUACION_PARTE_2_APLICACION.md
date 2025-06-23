# 📋 EVALUACIÓN PRÁCTICA - PARTE 2: APLICACIÓN PYTHON

## 🎯 **OBJETIVO GENERAL**
Crear una aplicación Python completa que se conecte a la base de datos creada en la Parte 1 y proporcione una interfaz gráfica funcional para gestionar los libros.

---

### **Funcionalidades Específicas:**

1. **Búsqueda Combinada**
   - Poder aplicar múltiples filtros simultáneamente
   - Mostrar contador de resultados
   - Botón "Limpiar" que resetee todos los filtros

2. **Validación de Entrada**
   - Año debe ser numérico y válido
   - Mostrar mensajes de error apropiados
   - Manejar campos vacíos correctamente

3. **Poblado Dinámico de ComboBox**
   - Obtener géneros únicos de la BD
   - Llenar ComboBox automáticamente

**Criterios de evaluación (20 puntos):**
- Interfaz de búsqueda completa (6 pts)
- Filtros funcionando individualmente (8 pts)
- Combinación de filtros (4 pts)
- Consultas parametrizadas (seguridad) (2 pts)

**💡 Referencia:** Revisa `Nivel_4.1_mayores.md`, `Nivel_4.2_Filtro_Dinamico.md` y `mostrar_datos_v3.py`

---

## ✅ **CRITERIOS DE EVALUACIÓN GENERAL**

### **📊 Distribución de Puntos**

| Componente | Puntos | Descripción |
|------------|--------|-------------|
| **Conexión BD** | 20 | Módulo de conexión robusto |
| **Interfaz Básica** | 30 | Ventana principal funcional |
| **Visualización Datos** | 30 | Mostrar libros y estadísticas |
| **Búsqueda/Filtros** | 20 | Filtros dinámicos |
| **TOTAL** | **100** | **Parte 2 completa** |

### **🎯 Criterios de Calidad**

| Aspecto | Excelente (100%) | Bueno (80%) | Regular (60%) | Deficiente (40%) |
|---------|------------------|-------------|---------------|------------------|
| **Funcionalidad** | Todo funciona perfectamente | Funciona con errores menores | Funcionalidad básica | Muchas funciones fallan |
| **Interfaz** | Interfaz intuitiva y atractiva | Interfaz funcional | Interfaz básica | Interfaz confusa |
| **Código** | Código limpio y documentado | Código organizado | Código funcional | Código desorganizado |
| **Seguridad** | Consultas parametrizadas | Mayoría parametrizadas | Algunas parametrizadas | Sin parametrización |

### **⭐ Puntos Extra (máximo +10 puntos)**
- **+3 pts**: Manejo excepcional de errores con mensajes útiles
- **+3 pts**: Interfaz especialmente atractiva y funcional
- **+2 pts**: Código muy bien documentado y organizado
- **+2 pts**: Funcionalidades adicionales (ej: ordenamiento, exportar)

### **❌ Penalizaciones**
- **-10 pts**: Uso de concatenación de strings en SQL (vulnerable)
- **-5 pts**: No usa la BD de la Parte 1
- **-5 pts**: Código sin comentarios o mal documentado
- **-3 pts**: Errores frecuentes o crasheos

---

## 🆘 **GUÍA DE RESOLUCIÓN DE PROBLEMAS**

### **🔧 Verificaciones Previas**

```python
# Verificar que la Parte 1 funciona
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca_sistema"
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM libros")
    total = cursor.fetchone()[0]
    print(f"✅ BD funcionando: {total} libros encontrados")
except Exception as e:
    print(f"❌ Error: {e}")
```

### **❌ Problemas Comunes**

#### **"Database 'biblioteca_sistema' doesn't exist"**
- **Causa**: No completaste la Parte 1
- **Solución**: Ejecuta primero todos los archivos .sql de la Parte 1

#### **"No module named 'mysql'"**
- **Causa**: mysql-connector-python no instalado
- **Solución**: `pip install mysql-connector-python`

#### **Ventana no se actualiza**
- **Causa**: Variables globales mal declaradas
- **Solución**: Usar `global` en funciones que modifican widgets

---

## 📁 **ESTRUCTURA DE ENTREGA**

### **Carpeta: `evaluacion_parte2`**
```
Mi_Proyecto_Base_Datos/
├── evaluacion_parte1/         (ya entregada)
│   ├── diseño_conceptual.md
│   ├── creacion_bd.sql
│   ├── datos_prueba.sql
│   └── consultas_analisis.sql
├── evaluacion_parte2/
│   ├── conexion_biblioteca.py     ⭐ OBLIGATORIO
│   ├── ventana_principal.py       ⭐ OBLIGATORIO
│   ├── mostrar_libros.py          ⭐ OBLIGATORIO
│   ├── busqueda_libros.py         ⭐ OBLIGATORIO
│   ├── consultas_utilizadas.sql   ⭐ OBLIGATORIO
│   └── capturas_pantalla/         (opcional)
```

### **📝 Archivo Adicional: `consultas_utilizadas.sql`**

Debes documentar TODAS las consultas SQL que uses:

```sql
-- =============================================
-- CONSULTAS SQL UTILIZADAS EN LA APLICACIÓN
-- Estudiante: [Tu nombre]
-- Fecha: [Fecha actual]
-- =============================================

-- CONSULTAS BÁSICAS
-- Obtener estadísticas generales
SELECT COUNT(*) as total FROM libros;
SELECT COUNT(*) as disponibles FROM libros WHERE disponible = TRUE;

-- Obtener todos los libros
SELECT * FROM libros ORDER BY id;

-- CONSULTAS DE ANÁLISIS
-- Libros por género
SELECT genero, COUNT(*) as cantidad FROM libros GROUP BY genero;

-- [Documenta TODAS las consultas que uses]
```

---

## 💡 **CONSEJOS PARA EL ÉXITO**

### **✨ Estrategias Recomendadas**
1. **Verifica la Parte 1 primero** - Sin BD, nada funcionará
2. **Empieza simple** - Conexión básica antes que interfaz compleja
3. **Prueba cada componente** - Verifica que funciona antes de continuar
4. **Usa tus códigos anteriores** - Adapta lo que ya funciona
5. **Documenta mientras codificas** - No lo dejes para el final

### **🎯 Para máxima puntuación**
- **Reutiliza código exitoso** de niveles anteriores
- **Usa consultas parametrizadas** siempre
- **Maneja errores apropiadamente** con try/except
- **Documenta todas las consultas** en el archivo SQL
- **Verifica que las ventanas se cierran** correctamente

---

## 🏆 **¡ÉXITO EN TU PARTE 2!**

### **🎓 Lo que habrás logrado**

Al completar ambas partes de la evaluación, habrás demostrado:

**🗃️ COMPETENCIAS DE BASE DE DATOS (Parte 1):**
- ✅ Diseño conceptual de bases de datos
- ✅ Implementación con DDL (CREATE DATABASE, TABLE)
- ✅ Manipulación de datos con DML (INSERT, SELECT)
- ✅ Consultas de análisis y agregación
- ✅ Documentación y organización de código SQL

**💻 COMPETENCIAS DE DESARROLLO (Parte 2):**
- ✅ Conexión segura Python-MySQL
- ✅ Interfaces gráficas funcionales con tkinter
- ✅ Consultas dinámicas y parametrizadas
- ✅ Manejo de errores y validación de datos
- ✅ Integración de sistemas BD-Aplicación

**🎯 COMPETENCIAS TRANSVERSALES:**
- ✅ Resolución de problemas complejos paso a paso
- ✅ Aplicación práctica de conocimientos teóricos
- ✅ Documentación técnica clara y completa
- ✅ Trabajo autónomo sin asistencia de IA
- ✅ Gestión eficiente del tiempo bajo presión

**¡Felicitaciones por completar un proyecto integral de base de datos!** 🌟

Has creado un sistema completo desde el diseño conceptual hasta la aplicación funcional, demostrando dominio tanto de bases de datos como de desarrollo de aplicaciones.

---

**Duración:** 1 clase (máximo 2 horas)  
**Modalidad:** Presencial, individual  
**Enfoque:** Aplicación Python con interfaces gráficas  
**Peso:** 50% de la evaluación total  
**Prerequisito:** Parte 1 completada y funcionando ✅