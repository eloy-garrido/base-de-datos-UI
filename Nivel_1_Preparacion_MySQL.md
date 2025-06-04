# Nivel 1: Preparación Simple de MySQL

## 🎯 Objetivo
Configurar XAMPP y crear una base de datos súper simple para nuestro primer test de conexión.

---

## 📖 Términos Básicos

### **XAMPP y MySQL:**
- **XAMPP**: Programa que instala MySQL de forma fácil
- **MySQL**: Sistema para guardar datos en tablas
- **Base de datos**: Como una carpeta que contiene tablas
- **Tabla**: Como una hoja de Excel con filas y columnas
- **localhost**: Tu propia computadora actuando como servidor
- **Puerto 3306**: Número que identifica dónde está MySQL

---

## 🔧 Paso 1: Verificar XAMPP

### **1.1 Abrir XAMPP**
1. Busca "XAMPP" en el menú Inicio de Windows
2. Abre "XAMPP Control Panel" 
3. **MUY IMPORTANTE**: Ejecuta como administrador (clic derecho → "Ejecutar como administrador")

### **1.2 Iniciar MySQL**
1. En XAMPP Control Panel, busca la fila que dice "MySQL"
2. Haz clic en el botón "Start" junto a MySQL
3. **Resultado esperado**: 
   - El botón cambia a "Stop"
   - El fondo se pone verde
   - Aparece "Running"

### **1.3 Solucionar si MySQL no inicia**

#### **Problema: "Port 3306 in use"**
**Solución simple:**
1. En XAMPP, haz clic en "Config" junto a MySQL
2. Selecciona "my.ini"
3. Se abre el Bloc de notas
4. Busca esta línea: `port=3306`
5. Cámbiala por: `port=3307`
6. Guarda el archivo (Ctrl+S)
7. En XAMPP: Stop → Start en MySQL

#### **Problema: MySQL no responde**
**Solución:**
1. Cierra XAMPP completamente
2. Reinicia tu computadora
3. Abre XAMPP como administrador
4. Intenta iniciar MySQL nuevamente

---

## 🗃️ Paso 2: Crear Base de Datos Súper Simple

### **2.1 Abrir MySQL Workbench**
1. Busca "MySQL Workbench" en el menú Inicio
2. Ábrelo
3. Verás una conexión que dice "Local instance MySQL" o similar
4. Haz clic en esa conexión
5. Si pide contraseña, déjala vacía y presiona Enter

### **2.2 Crear la base de datos más simple**

**Copia y pega exactamente este código en MySQL Workbench:**

```sql
-- Crear una base de datos simple para pruebas
CREATE DATABASE IF NOT EXISTS mi_primera_db;

-- Usar esa base de datos
USE mi_primera_db;

-- Crear una tabla súper simple
CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);

-- Insertar solo 3 datos de prueba
INSERT INTO personas (nombre, edad) VALUES 
('Juan', 25),
('María', 30),
('Carlos', 20);

-- Verificar que funciona
SELECT * FROM personas;
```

### **2.3 Ejecutar el código**
1. **Selecciona todo el código** (Ctrl+A)
2. **Ejecuta** (botón del rayo ⚡ o Ctrl+Enter)
3. **Verifica el resultado**: Debe aparecer una tabla con 3 personas

**¿Qué acabamos de hacer?**
- ✅ Creamos una base de datos llamada `mi_primera_db`
- ✅ Creamos una tabla llamada `personas` con solo 3 columnas
- ✅ Agregamos 3 personas de ejemplo
- ✅ Verificamos que todo funciona

---

## 🧪 Paso 3: Verificar que Todo Funciona

### **3.1 Verificar en MySQL Workbench**
En el panel izquierdo (Navigator):
1. Busca "mi_primera_db"
2. Expándela (clic en la flecha)
3. Expande "Tables"
4. Debe aparecer "personas"

### **3.2 Probar una consulta simple**
Ejecuta esta consulta para asegurarte de que todo funciona:

```sql
USE mi_primera_db;
SELECT nombre, edad FROM personas WHERE edad > 20;
```

**Resultado esperado**: Debe mostrar Juan (25) y María (30).

---

## ✅ Verificación Final

Antes de pasar al Nivel 2, asegúrate de tener:

### **XAMPP:**
- [ ] XAMPP abierto
- [ ] MySQL ejecutándose (verde, "Running")

### **Base de Datos:**
- [ ] Base de datos `mi_primera_db` creada
- [ ] Tabla `personas` con 3 registros
- [ ] Consulta de prueba funciona correctamente

### **Información importante para el Nivel 2:**
- **Host**: localhost
- **Puerto**: 3306 (o 3307 si lo cambiaste)
- **Usuario**: root
- **Contraseña**: (vacía, no escribas nada)
- **Base de datos**: mi_primera_db

---

## 🆘 Solución de Problemas

### **Si MySQL no inicia en XAMPP:**
1. Reinicia tu computadora
2. Abre XAMPP como administrador
3. Si sigue sin funcionar, cambia el puerto a 3307

### **Si MySQL Workbench no se conecta:**
1. Verifica que MySQL esté verde en XAMPP
2. Asegúrate de dejar la contraseña vacía
3. Usa "localhost" como host

### **Si el código SQL da error:**
1. Asegúrate de copiarlo exactamente como está
2. Selecciona todo el código antes de ejecutar
3. Ejecuta línea por línea si hay problemas

---

## 🎓 Conclusión

¡Perfecto! Ahora tienes:
- ✅ MySQL funcionando
- ✅ Una base de datos simple
- ✅ Una tabla con datos de prueba

**En el Nivel 2** crearemos un programa Python súper simple que se conecte a esta base de datos y nos diga si la conexión funciona.