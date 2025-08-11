# 🤖 Semana 03 — Introducción a la IA Clásica en Python

Esta semana daremos un salto hacia el mundo de la **Inteligencia Artificial**, pero empezaremos por la base: **IA clásica**.
Aprenderás conceptos fundamentales, implementaciones simples y cómo modelar problemas usando **clases y objetos** (POO), continuando lo aprendido en la Semana 2.

> 💡 **Organización del curso**
> Cada participante debe crear una **carpeta con su nombre** dentro del repositorio.
> Ahí podrán explorar los temas, hacer sus pruebas y si lo desean, **copiar este README.md** en su carpeta para tenerlo más a la mano.

---

## 🎯 Objetivos y habilidades a desarrollar

Durante esta semana, aprenderás a:

- 🧠 Comprender qué es la **IA clásica** y en qué se diferencia de la IA moderna.
- 📜 Implementar **algoritmos de búsqueda** como BFS y DFS.
- 🎯 Aplicar **toma de decisiones** mediante reglas.
- 🛠 Modelar problemas usando **POO** y estructuras lógicas.
- 🗺 Representar problemas como **espacios de estados**.
- 🔍 Aplicar **búsquedas heurísticas simples** (como búsqueda voraz).
- 📂 Separar la lógica de IA en módulos reutilizables.

---

## 📌 Contenido de estudio

> 📚 **Recursos recomendados para esta semana**

1. 📄 **Fundamentos de IA**
   [Introducción a la IA (Wikipedia)](https://es.wikipedia.org/wiki/Inteligencia_artificial)
   Explicación básica del concepto y ramas de la IA.

2. 🧮 **Algoritmos de búsqueda**
   [Red Blob Games - Pathfinding](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
   Una de las mejores explicaciones visuales sobre búsqueda de caminos.

3. 🐍 **Implementación en Python**
   [GeeksForGeeks - BFS y DFS en Python](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)
   Ejemplos prácticos y fáciles de seguir.

4. 📌 **Temas que debes dominar**:
   - Concepto de **agente** y **entorno**
   - **Algoritmos de búsqueda no informada**:
     - Búsqueda en amplitud (BFS)
     - Búsqueda en profundidad (DFS)
   - **Búsquedas informadas**:
     - Búsqueda voraz (Greedy)
   - Representación de problemas en **grafos**
   - Uso de **clases** para modelar agentes y entornos
   - Separación de la lógica de IA en módulos

---

## 💻 Ejemplo básico de IA clásica: Búsqueda en amplitud (BFS)

> ✏ **Prueba y modifica** este código para entender cómo un algoritmo recorre un grafo.

```python
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(f"Visitando: {nodo}")
            visitados.add(nodo)
            cola.extend(vecino for vecino in grafo[nodo] if vecino not in visitados)

# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(grafo, 'A')
```
---

## 🛠 Buenas prácticas para IA clásica

> 📌 La IA clásica se basa en **organización y lógica**, más que en datos masivos.

**1. Modela bien tu problema** \
Antes de programar, dibuja el problema como un grafo o mapa de estados.

**2. Usa clases para agentes y entornos** \
Esto facilita cambiar el comportamiento del agente sin reescribir todo.

**3. Mantén la IA independiente del resto del código** \
Si tu agente está en un juego, no mezcles su lógica con el renderizado.

**4. Comenta el algoritmo** \
Explica qué hace cada parte, especialmente en pasos de búsqueda y heurística.

**5. Empieza simple** \
Primero implementa un BFS o DFS, luego agrega heurísticas más complejas.

---

## 🏆 Reto semanal
**Objetivo:** \
Implementar un **agente inteligente** que resuelva un laberinto utilizando **búsqueda en amplitud (BFS)** o **búsqueda en profundidad (DFS)**.

El programa debe:

- Representar el laberinto como un grafo o matriz.

- Mostrar el camino encontrado desde la entrada hasta la salida.

- Usar clases para representar el laberinto y el agente.

> ⚠ No se incluye código sugerido: la idea es que lo desarrolles tú mismo.

---

## 📅 Sugerencia de estudio diario

| Día | Tema principal                | Práctica                                |
| --- | ----------------------------- | --------------------------------------- |
| 1   | Qué es la IA clásica          | Leer sobre agentes y entornos           |
| 2   | Representación de problemas   | Crear un grafo simple en Python         |
| 3   | Búsqueda en amplitud (BFS)    | Implementar BFS en un grafo             |
| 4   | Búsqueda en profundidad (DFS) | Implementar DFS en un grafo             |
| 5   | Búsqueda informada            | Implementar búsqueda voraz simple       |
| 6   | Reto semanal                  | Resolver un laberinto con BFS o DFS     |
| 7   | Repaso y mejoras              | Agregar visualización o más heurísticas |

---

**🚀 Consejo final**: La IA clásica es la base de muchos sistemas modernos. \
Aunque hoy se hable mucho de redes neuronales, **entender BFS, DFS y heurísticas simples** te dará una gran ventaja para comprender IA más avanzada.
