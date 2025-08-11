# 🐍 Semana 02 — Programación Orientada a Objetos (POO) en Python

En esta semana aprenderás a **estructurar tu código en clases y objetos**, para que sea más fácil de mantener, reutilizar y escalar.
Dominar POO te permitirá pensar como un **arquitecto de software** y no solo como un programador.

> 💡 **Organización del curso**
> Cada participante debe crear una **carpeta con su nombre** dentro del repositorio.
> Ahí podrán explorar los temas, hacer sus pruebas y si lo desean, **copiar este README.md** en su carpeta para tenerlo más a la mano.

---

## 🎯 Objetivos y habilidades a desarrollar

Durante esta semana, aprenderás a:

- 🏗 Crear **clases** y **objetos** en Python.
- 📦 Comprender y usar **atributos** (`self`) y **métodos**.
- ⚙ Utilizar **constructores** (`__init__`) para inicializar objetos.
- 🧬 Implementar **herencia básica** para reutilizar código.
- 🔒 Aplicar **encapsulamiento** para proteger datos internos.
- 📂 Separar tu código en **módulos reutilizables**.
- 📝 Documentar clases y métodos usando **docstrings**.

---

## 📌 Contenido de estudio

> 📚 **Recursos recomendados para esta semana**

1. 🐍 **Programación orientada a objetos en Python**
   [RealPython - OOP en Python](https://realpython.com/python3-object-oriented-programming/)
   Explicación detallada y ejemplos prácticos.

2. 📖 **Clases y objetos en W3Schools**
   [W3Schools - Clases y Objetos](https://www.w3schools.com/python/python_classes.asp)
   Guía simple para aprender lo básico rápidamente.

3. 📌 **Temas que debes dominar**:
   - Qué es una **clase** y un **objeto**
   - Diferencia entre **atributos de instancia** y **atributos de clase**
   - Métodos y la palabra clave `self`
   - Uso del **constructor** `__init__`
   - **Herencia** y sobreescritura de métodos
   - **Encapsulamiento** con guiones bajos (`_atributo`, `__atributo`)
   - Importar clases desde otros **módulos**
   - Documentar correctamente con **docstrings**

---

## 💻 Ejemplos básicos de POO en Python

> ✏ **Prueba y modifica** este código para entender cómo funciona.

```python
# Definición de clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear un objeto
persona1 = Persona("Leonardo", 25)

# Llamar a un método
persona1.saludar()
```
---

## 🛠 Buenas prácticas en POO

> 📌 La POO no solo es crear clases, sino **organizar bien el código.**

1. **Nombres descriptivos** \
    Usa nombres claros para clases y métodos:

```python
# ❌ Malo
class X:
    pass

# ✅ Bueno
class Vehiculo:
    pass
```

2. **Documenta tus clases y métodos** \
    Usa docstrings para explicar qué hace cada clase y método:

```python
class Coche:
    """Representa un coche con marca y modelo."""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

3. **Aplica encapsulamiento** \
    Protege los datos internos usando guiones bajos:

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo  # Protegido

    def mostrar_saldo(self):
        return self._saldo
```

4. **Evita clases innecesarias** \
    No crees clases solo por crearlas. Úsalas cuando realmente haya **entidades** que modelar.

5. **Organiza en módulos** \
    Guarda clases relacionadas en un mismo archivo `.py` y evita tener todo en un solo script.

---

## **🏆 Reto semanal**
**Objetivo:** \
    Crear una clase Email que contenga:

- Remitente

- Destinatario

- Asunto

- Cuerpo del mensaje

Además, implementar un método `enviar()` que **simule el envío del correo** mostrando sus datos en pantalla.

> ⚠ No se incluye código sugerido: la idea es que lo desarrolles tú mismo.

---

## **📅 Sugerencia de estudio diario**

| Día | Tema principal              | Práctica                                          |
| --- | --------------------------- | ------------------------------------------------- |
| 1   | Introducción a POO y clases | Crear una clase simple con atributos              |
| 2   | Métodos y `self`            | Crear métodos que usen atributos                  |
| 3   | Constructor `__init__`      | Inicializar objetos automáticamente               |
| 4   | Herencia                    | Crear una subclase que herede atributos y métodos |
| 5   | Encapsulamiento             | Proteger datos con `_atributo` y `__atributo`     |
| 6   | Reto semanal                | Implementar la clase `Email`                      |
| 7   | Repaso y autoevaluación     | Mejorar la clase `Email` con validaciones         |

---
\
**🚀 Consejo final**: La POO es más que una técnica, es una forma de pensar.

Cuanto más practiques modelar problemas en clases y objetos, más natural será para ti.
