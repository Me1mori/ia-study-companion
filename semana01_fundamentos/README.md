# 🐍 Semana 01 — Fundamentos de Python

Bienvenido a la **Semana 1** del curso.
Aquí aprenderás los **conceptos esenciales de Python** para dar tus primeros pasos en programación.
Al finalizar, podrás escribir pequeños programas, organizar tu código y aplicar **buenas prácticas**.

> 💡 **Organización del curso**
> Cada participante debe crear una **carpeta con su nombre** dentro del repositorio.
> Ahí podrán explorar los temas, hacer sus pruebas y si lo desean, **copiar este README.md** en su carpeta para tenerlo más a la mano.

---

## 🎯 Objetivos y habilidades a desarrollar

Durante esta semana, aprenderás a:

- 📝 Declarar y usar **variables** (`str`, `int`, `float`, `bool`)
- 🔀 Aplicar **estructuras de control**: `if`, `elif`, `else`
- 🔄 Trabajar con **bucles** (`for`, `while`)
- 🛠 Definir y usar **funciones** con parámetros y retorno de valores
- ✍ Escribir **código claro, ordenado y comentado**
- 🧠 Desarrollar **lógica de programación** resolviendo problemas simples

---

## 📌 Contenido de estudio

> 📚 **Recursos recomendados para esta semana**

1. 📄 **Documentación oficial**
   [Python Docs - Tutorial (Español)](https://docs.python.org/es/3/tutorial/index.html)
   La referencia oficial de Python: completa y confiable.

2. 🖥 **Tutorial interactivo**
   [W3Schools - Python Basics](https://www.w3schools.com/python/)
   Ideal para practicar desde el navegador sin instalar nada.

3. 📊 **Visualización de algoritmos**
   [Visualgo](https://visualgo.net/en)
   Aprende cómo funcionan los bucles, estructuras y algoritmos visualmente.

4. 📌 **Temas que debes dominar**:
   - Tipos de datos en Python y sus usos
   - Operadores aritméticos y lógicos
   - Uso de condicionales para tomar decisiones
   - Creación y control de bucles
   - Funciones y modularización del código
   - Comentarios y buenas prácticas
   - Uso básico de **VSCode** con extensiones como:
     - Python 🐍
     - Pylance 🔍
     - Autopep8 o Black 🎨

---

## 💻 Ejemplos básicos de Python

> ✏ **Prueba y modifica** estos ejemplos para experimentar.

```python
# Variables
nombre = "Leonardo"
edad = 25

# Condicionales
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Bucles
for i in range(5):
    print(f"Iteración {i}")

# Funciones
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar(nombre))
```

---

## 🛠 Buenas prácticas en Python

> 📌 Escribir código funcional es bueno, pero escribir **código limpio y mantenible** es mejor.

1. **Comenta tu código** \
    Explica la lógica para que tú y otros la entiendan después.

```python
# Calcula el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura
```

2. **Usa nombres descriptivos** \
    Evita abreviaciones confusas.

```python
# ❌ Malo
x = 10
y = 5
r = x * y

# ✅ Bueno
base = 10
altura = 5
area = base * altura
```

3. **Respeta la indentación** \
    Python depende de la indentación para funcionar correctamente.

4. **Organiza tu código** \
    Agrupa funciones relacionadas y separa secciones con líneas en blanco.

5. **Evita repetir código** \
    Si repites algo, conviértelo en una función reutilizable.

---

## 🏆 Reto semanal

**Objetivo:**

Crear un programa que reciba **dos números** y una **operación matemática** ( `+`, `-`, `*`, `/`) y muestre el resultado.

Debe validar errores como:

- 🚫 División entre cero

- ❓ Operaciones no válidas

> ⚠ No se incluye código sugerido: la idea es que desarrolles tu propia solución.

---

## 📅 Sugerencia de estudio diario

| Día | Tema principal                         | Práctica                                               |
| --- | -------------------------------------- | ------------------------------------------------------ |
| 1   | Instalación y primeros pasos en Python | Ejecutar tu primer "Hola Mundo"                        |
| 2   | Variables y tipos de datos             | Crear variables y mostrar su valor                     |
| 3   | Condicionales (`if`, `elif`, `else`)   | Hacer un programa que clasifique edades                |
| 4   | Bucles (`for`, `while`)                | Imprimir una tabla de multiplicar                      |
| 5   | Funciones                              | Crear una función que calcule el área de un rectángulo |
| 6   | Reto semanal                           | Desarrollar la calculadora                             |
| 7   | Repaso y autoevaluación                | Mejorar el código del reto semanal                     |

---
\
**🚀 Consejo final**: La programación se aprende **programando.**

No temas cometer errores, son parte del proceso.
Cada línea que escribas te acercará más a convertirte en un buen programador.

