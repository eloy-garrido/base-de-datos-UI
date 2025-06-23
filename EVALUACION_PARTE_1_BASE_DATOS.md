# 📋 EVALUACIÓN PRÁCTICA - PARTE 1: BASE DE DATOS

## 🎯 **OBJETIVO GENERAL**
Diseñar y crear una base de datos completa para un sistema de biblioteca, demostrando dominio de SQL y diseño de bases de datos.

---

## 📖 **INSTRUCCIONES GENERALES**

### **📚 METODOLOGÍA A UTILIZAR**

**ANTES DE COMENZAR, DEBES:**
1. **Revisar todos los ejercicios anteriores** (Niveles 0-2) para recordar conceptos de BD
2. **Tener acceso a todos tus apuntes** y códigos de los niveles anteriores
3. **Asegurarte de que MySQL funciona** (XAMPP, MySQL Workbench)

### **🚫 RESTRICCIONES IMPORTANTES**

- ❌ **NO SE PERMITE EL USO DE INTELIGENCIA ARTIFICIAL** (ChatGPT, Claude, etc.)
- ❌ **NO se permite copiar SQL** de internet
- ✅ **SÍ puedes consultar** tus códigos anteriores (Niveles 0-2)
- ✅ **SÍ puedes usar** la documentación oficial de MySQL
- ✅ **SÍ puedes revisar** los archivos .md de instrucciones del proyecto

### **⏰ TIEMPO Y MODALIDAD**
- **Duración**: 1 clase (máximo 2 horas)
- **Modalidad**: Presencial, individual
- **Entrega**: Al final de la clase

### **📝 ENTREGA**
- Crear una carpeta llamada `evaluacion_parte1` dentro de tu proyecto
- Entregar los archivos SQL especificados

---

## 📊 **ESTRUCTURA DE LA PARTE 1**

| Componente | Puntos | Tiempo Estimado | Descripción |
|------------|--------|-----------------|-------------|
| **1. Diseño de BD** | 30 pts | 30 min | Análisis y diseño conceptual |
| **2. Creación SQL** | 40 pts | 60 min | DDL (CREATE DATABASE, TABLE) |
| **3. Inserción Datos** | 20 pts | 20 min | DML (INSERT) |
| **4. Consultas Verificación** | 10 pts | 10 min | SELECT para validar |
| **TOTAL** | **100 pts** | **120 min** | **2 horas máximo** |

---

## 🗃️ **COMPONENTE 1: DISEÑO CONCEPTUAL (30 puntos)**

### **Objetivo**
Analizar los requerimientos y diseñar la estructura de la base de datos.

### **📋 Requerimientos del Sistema**

**El sistema de biblioteca debe manejar:**

#### **Información de Libros:**
- Identificador único para cada libro
- Título del libro (obligatorio, máximo 100 caracteres)
- Autor del libro (obligatorio, máximo 80 caracteres)  
- Género literario (opcional, máximo 50 caracteres)
- Año de publicación (opcional, número entero)
- Estado de disponibilidad para préstamo (por defecto disponible)
- Fecha de registro en el sistema (automática)

#### **Reglas de Negocio:**
1. Cada libro debe tener un identificador único que se asigne automáticamente
2. El título y autor son obligatorios
3. Por defecto, todos los libros están disponibles para préstamo
4. El sistema debe registrar automáticamente cuándo se agregó cada libro
5. Los géneros pueden repetirse entre diferentes libros
6. Puede haber libros del mismo título de diferentes autores

### **📝 Entregable 1: `diseño_conceptual.md`**

Crea un archivo que contenga:

```markdown
# DISEÑO CONCEPTUAL - SISTEMA BIBLIOTECA
**Estudiante:** [Tu nombre]
**Fecha:** [Fecha actual]

## 1. ANÁLISIS DE REQUERIMIENTOS
[Explica con tus palabras qué debe hacer el sistema]

## 2. ENTIDADES IDENTIFICADAS
[Lista las entidades principales que identificaste]

## 3. ATRIBUTOS POR ENTIDAD
[Lista todos los atributos de cada entidad con su tipo de dato]

## 4. RESTRICCIONES Y REGLAS
[Lista las restricciones que debe cumplir la BD]

## 5. JUSTIFICACIÓN DEL DISEÑO
[Explica por qué elegiste esta estructura]
```

**Criterios de evaluación (30 puntos):**
- Identificación correcta de entidades (10 pts)
- Definición apropiada de atributos (10 pts)
- Comprensión de restricciones (5 pts)
- Justificación del diseño (5 pts)

---

## 🛠️ **COMPONENTE 2: CREACIÓN CON SQL (40 puntos)**

### **Objetivo**
Implementar el diseño usando comandos DDL de SQL.

### **📝 Entregable 2: `creacion_bd.sql`**

Crea un archivo SQL con la siguiente estructura:

```sql
-- =============================================
-- CREACIÓN DE BASE DE DATOS - SISTEMA BIBLIOTECA
-- Estudiante: [Tu nombre]
-- Fecha: [Fecha actual]
-- =============================================

-- SECCIÓN 1: CREAR BASE DE DATOS
-- [Tu código aquí]

-- SECCIÓN 2: SELECCIONAR BASE DE DATOS
-- [Tu código aquí]

-- SECCIÓN 3: CREAR TABLA(S)
-- [Tu código aquí]

-- SECCIÓN 4: VERIFICAR ESTRUCTURA
-- [Tu código aquí]
```

### **Especificaciones Técnicas Requeridas:**

#### **Base de Datos:**
- Nombre: `biblioteca_sistema`
- Usar `IF NOT EXISTS` para evitar errores

#### **Tabla: `libros`**
**Debes determinar tú mismo:**
- Tipos de datos apropiados para cada campo
- Restricciones necesarias (PRIMARY KEY, NOT NULL, etc.)
- Valores por defecto donde corresponda
- Configuración de auto-incremento

**Campos requeridos:**
1. Campo de identificación única
2. Campo para título
3. Campo para autor  
4. Campo para género
5. Campo para año de publicación
6. Campo para disponibilidad
7. Campo para fecha de registro

### **Comandos que DEBES incluir:**
```sql
-- Mostrar bases de datos para verificar creación
SHOW DATABASES;

-- Mostrar estructura de tabla creada
DESCRIBE [nombre_tabla];

-- Mostrar comando de creación de tabla
SHOW CREATE TABLE [nombre_tabla];
```

**Criterios de evaluación (40 puntos):**
- Sintaxis SQL correcta (15 pts)
- Tipos de datos apropiados (10 pts)
- Restricciones correctas (10 pts)
- Comandos de verificación (5 pts)

---

## 📊 **COMPONENTE 3: INSERCIÓN DE DATOS (20 puntos)**

### **Objetivo**
Poblar la base de datos con datos de prueba usando comandos DML.

### **📝 Entregable 3: `datos_prueba.sql`**

```sql
-- =============================================
-- INSERCIÓN DE DATOS DE PRUEBA
-- Estudiante: [Tu nombre]
-- Fecha: [Fecha actual]
-- =============================================

-- SECCIÓN 1: USAR BASE DE DATOS
-- [Tu código aquí]

-- SECCIÓN 2: INSERTAR DATOS
-- [Tu código aquí]

-- SECCIÓN 3: VERIFICAR INSERCIÓN
-- [Tu código aquí]
```

### **Datos Específicos a Insertar:**

Debes insertar **exactamente estos 8 libros**:

1. **"Cien años de soledad"** - Gabriel García Márquez - Realismo Mágico - 1967 - Disponible
2. **"1984"** - George Orwell - Ciencia Ficción - 1949 - Disponible  
3. **"El Quijote"** - Miguel de Cervantes - Novela - 1605 - NO Disponible
4. **"Crónica de una muerte anunciada"** - Gabriel García Márquez - Realismo Mágico - 1981 - Disponible
5. **"Fahrenheit 451"** - Ray Bradbury - Ciencia Ficción - 1953 - Disponible
6. **"La Casa de los Espíritus"** - Isabel Allende - Realismo Mágico - 1982 - NO Disponible
7. **"El nombre del viento"** - Patrick Rothfuss - Fantasía - 2007 - Disponible
8. **"Neuromante"** - William Gibson - Cyberpunk - 1984 - Disponible

**Criterios de evaluación (20 puntos):**
- Sintaxis INSERT correcta (8 pts)
- Todos los datos insertados (8 pts)
- Consultas de verificación (4 pts)

---

## 🔍 **COMPONENTE 4: CONSULTAS DE ANÁLISIS (10 puntos)**

### **Objetivo**
Demostrar conocimiento de consultas SELECT con diferentes operadores.

### **📝 Entregable 4: `consultas_analisis.sql`**

```sql
-- =============================================
-- CONSULTAS DE ANÁLISIS
-- Estudiante: [Tu nombre]
-- Fecha: [Fecha actual]
-- =============================================

-- CONSULTA 1: Libros por género
-- [Tu código aquí]

-- CONSULTA 2: Libros más antiguos (antes de 1980)
-- [Tu código aquí]

-- CONSULTA 3: Autores con más de un libro
-- [Tu código aquí]

-- CONSULTA 4: Libros disponibles de Ciencia Ficción
-- [Tu código aquí]

-- CONSULTA 5: Estadísticas generales
-- [Tu código aquí]
```

### **Consultas Específicas a Implementar:**

1. **Libros agrupados por género** (con conteo)
2. **Libros publicados antes de 1980**
3. **Autores que tienen más de un libro en el sistema**
4. **Solo libros disponibles del género "Ciencia Ficción"**
5. **Estadísticas generales** (total libros, disponibles, no disponibles, género más común)

**Criterios de evaluación (10 puntos):**
- Uso correcto de GROUP BY (3 pts)
- Uso correcto de WHERE (3 pts)
- Consultas complejas (2 pts)
- Funciones de agregación (2 pts)

---

## ✅ **CRITERIOS DE EVALUACIÓN GENERAL**

### **📊 Distribución de Puntos**

| Componente | Puntos | Descripción |
|------------|--------|-------------|
| **Diseño Conceptual** | 30 | Análisis y documentación |
| **Creación SQL** | 40 | DDL correcto y completo |
| **Inserción Datos** | 20 | DML correcto |
| **Consultas Análisis** | 10 | SELECT avanzado |
| **TOTAL** | **100** | **Parte 1 completa** |

### **🎯 Criterios de Calidad**

| Aspecto | Excelente (100%) | Bueno (80%) | Regular (60%) | Deficiente (40%) |
|---------|------------------|-------------|---------------|------------------|
| **Sintaxis SQL** | Sin errores, código limpio | Funciona, errores menores | Funciona básicamente | Errores significativos |
| **Diseño de BD** | Estructura óptima, bien justificada | Estructura correcta | Estructura básica funcional | Estructura deficiente |
| **Documentación** | Comentarios claros y completos | Comentarios básicos | Poca documentación | Sin comentarios |
| **Completitud** | Todos los requerimientos cumplidos | Mayoría de requerimientos | Requerimientos básicos | Muchos faltantes |

---

## 🆘 **GUÍA DE RESOLUCIÓN DE PROBLEMAS**

### **🔧 Verificaciones Previas**

**Antes de empezar:**
```sql
-- Verificar que MySQL funciona
SHOW DATABASES;

-- Verificar versión
SELECT VERSION();

-- Verificar usuario actual
SELECT USER();
```

### **❌ Problemas Comunes y Soluciones**

#### **"Database already exists"**
```sql
-- Solución: Usar IF NOT EXISTS
CREATE DATABASE IF NOT EXISTS biblioteca_sistema;
```

#### **"Table already exists"**
```sql
-- Opción 1: Eliminar tabla primero
DROP TABLE IF EXISTS libros;

-- Opción 2: Usar IF NOT EXISTS
CREATE TABLE IF NOT EXISTS libros (...);
```

#### **Errores de tipos de datos**
- **VARCHAR vs TEXT**: Para campos <255 caracteres usa VARCHAR
- **INT vs BIGINT**: Para IDs usa INT AUTO_INCREMENT
- **BOOLEAN vs TINYINT**: MySQL usa TINYINT(1) para booleanos
- **TIMESTAMP vs DATETIME**: Para fecha automática usa TIMESTAMP DEFAULT CURRENT_TIMESTAMP

#### **Errores de sintaxis comunes**
```sql
-- CORRECTO
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    disponible BOOLEAN DEFAULT TRUE
);

-- INCORRECTO (falta coma)
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY
    titulo VARCHAR(100) NOT NULL  -- ❌ Falta coma antes
);
```

---

## 📁 **ESTRUCTURA DE ENTREGA**

### **Carpeta: `evaluacion_parte1`**
```
Mi_Proyecto_Base_Datos/
├── evaluacion_parte1/
│   ├── diseño_conceptual.md          ⭐ OBLIGATORIO
│   ├── creacion_bd.sql               ⭐ OBLIGATORIO
│   ├── datos_prueba.sql              ⭐ OBLIGATORIO
│   └── capturas_pantalla/            (opcional)
```

## 💡 **CONSEJOS PARA EL ÉXITO**

### **✨ Estrategias Recomendadas**
1. **Lee todo antes de empezar** - Entiende todos los requerimientos
2. **Empieza por el diseño** - No saltes directo al código
3. **Prueba cada comando** - Ejecuta y verifica antes de continuar
4. **Usa comentarios** - Documenta qué hace cada sección
5. **Verifica constantemente** - Usa DESCRIBE y SELECT para validar
6. **Guarda frecuentemente** - No pierdas tu trabajo

### **🎯 Para máxima puntuación**
- **Planifica antes de codificar**
- **Usa nombres descriptivos** para campos y restricciones
- **Incluye todos los comentarios** solicitados
- **Sigue exactamente** las especificaciones de datos
- **Verifica cada paso** con consultas

---

## 🏆 **¡ÉXITO EN TU PARTE 1!**

Esta primera parte establece la base fundamental para la Parte 2. Un buen diseño de base de datos facilitará enormemente la implementación de la aplicación Python.

**Recuerda:** Una base de datos bien diseñada es la clave del éxito de cualquier aplicación. ¡Tómate el tiempo necesario para hacerlo bien!

---

**Duración:** 1 clase (máximo 2 horas)  
**Modalidad:** Presencial, individual  
**Enfoque:** Diseño de BD y SQL  
**Peso:** 50% de la evaluación total