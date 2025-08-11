# 🗄️ Semana 04 — Bases de Datos con Python

Esta semana aprenderás a conectar tus programas de Python con bases de datos para **guardar, buscar y manipular información de forma persistente**.
Nos enfocaremos en **SQLite** por su simplicidad, pero también revisaremos nociones de MySQL para que puedas trabajar con bases de datos más grandes en el futuro.

> 💡 **Organización del curso**
> Cada participante debe crear una **carpeta con su nombre** dentro del repositorio.
> Ahí podrán explorar los temas, hacer sus pruebas y si lo desean, **copiar este README.md** en su carpeta para tenerlo más a la mano.

---

## 🎯 Objetivos y habilidades a desarrollar

Durante esta semana, aprenderás a:

- 🔌 Conectar Python a una base de datos SQLite.
- 🏗 Crear tablas y definir esquemas.
- ✏ Insertar, actualizar y eliminar registros.
- 🔍 Consultar datos usando **SELECT** y filtros.
- 🛡 Usar **consultas preparadas** para mayor seguridad.
- 🧩 Separar la lógica de base de datos en módulos.
- 📝 Documentar funciones y clases con **docstrings**.

---

## 📌 Contenido de estudio

> 📚 **Recursos recomendados para esta semana**

1. 🐍 **SQLite en Python (Documentación oficial)**
   [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)

2. 🗃 **W3Schools - Python MySQL**
   [https://www.w3schools.com/python/python_mysql_getstarted.asp](https://www.w3schools.com/python/python_mysql_getstarted.asp)

3. 📄 **Tutorial de SQLite con Python (Real Python)**
   [https://realpython.com/python-sql-libraries/](https://realpython.com/python-sql-libraries/)

4. 📌 **Temas que debes dominar**:
   - Conexión a una base de datos desde Python
   - Creación de tablas y definición de campos
   - Inserción, actualización y eliminación de datos
   - Consultas básicas y avanzadas con **SELECT**
   - Uso de parámetros en consultas para evitar SQL Injection
   - Manejo de errores con **try/except**
   - Modularización del código de base de datos

---

## 💻 Ejemplo básico: Conexión y creación de tabla en SQLite

> ✏ **Prueba y modifica** este código para entender cómo Python interactúa con una base de datos.

```python
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL
)
""")

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()
```

---

## 🛠 Buenas prácticas
- Siempre cerrar la conexión con `conexion.close` () para liberar recursos.

- Usar **consultas preparadas** con `?` para evitar inyecciones SQL.

- Separar la lógica de base de datos en un módulo independiente.

- Documentar cada función con **docstrings** indicando parámetros y retorno.

- Manejar errores con `try/except` para evitar que el programa se detenga.

---

## 🎯 Reto semanal
**Reto**: Crea una **agenda de contactos** usando SQLite.
La agenda debe permitir:

- Agregar un contacto (nombre, teléfono, correo)

- Listar todos los contactos

- Buscar contactos por nombre

**📌 Condiciones:**

- La lógica de base de datos debe estar en un módulo separado.

- Usar consultas preparadas para inserciones y búsquedas.

- No incluir código sugerido ni salida esperada en este README.

---

## 📅 Sugerencia de estudio diario

| Día       | Actividad                                            |
| --------- | ---------------------------------------------------- |
| Lunes     | Leer sobre SQLite y su integración con Python.       |
| Martes    | Practicar conexión y creación de tablas.             |
| Miércoles | Insertar, eliminar y modificar registros.            |
| Jueves    | Realizar consultas con filtros y ordenar resultados. |
| Viernes   | Modularizar el código de base de datos.              |
| Sábado    | Trabajar en el reto semanal.                         |
| Domingo   | Revisar y documentar el código.                      |

---
\
**💡 Consejo final**

> Trabajar con bases de datos es como tener memoria a largo plazo para tus programas:
si estructuras bien la información hoy, podrás reutilizarla y mejorarla en el futuro.
