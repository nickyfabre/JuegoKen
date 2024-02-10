# JuegoKen
Este es un juego simple desarrollado con Pygame, en el cual el jugador controla a un personaje llamado "Ken" que corre a lo largo de la playa y salta para esquivar obstáculos en su camino.
## Funcionalidad del Juego

El juego presenta las siguientes características:

- El jugador puede controlar al personaje principal utilizando la tecla "flcha-arriba" del teclado para saltar.
- El personaje puede saltar para esquivar los obstáculos.
- Los obstáculos aparecen aleatoriamente en la pantalla y el jugador debe evitar chocar con ellos.
- Cada vez que el jugador choca con un obstáculo, pierde y se reinicia el juego.
- El juego registra el puntaje del jugador, que aumenta a medida que avanza y esquiva los obstáculos.
- La velocidad del juego aumenta gradualmente para aumentar la dificultad.

## Estructura del Código

El código del juego está dividido en varias secciones principales:

- **Inicialización del juego**: Se configuran las constantes, se cargan los recursos (imágenes y sonidos) y se define la ventana de visualización.
- **Clase Ken**: Define al personaje principal del juego (Ken) y sus acciones (correr y saltar).
- **Clases de Obstáculos**: Define los obstáculos que aparecen en el juego y sus comportamientos.
- **Función principal (main)**: Controla el flujo principal del juego, incluyendo la actualización de la pantalla, la detección de colisiones y el manejo de eventos del usuario.
- **Función de Menú**: Controla la pantalla de inicio y fin del juego, mostrando mensajes y el puntaje del jugador.

## Instrucciones de Ejecución

1. Asegúrate de tener Python y Pygame instalados en tu sistema.
2. Ejecuta el archivo `main.py` para iniciar el juego.
3. Presiona cualquier tecla para empezar a jugar.
4. Utiliza la tecla "flcha-arriba" del teclado para saltar.
5. Esquiva los obstáculos y acumula la mayor cantidad de puntos posible.

## Créditos de la Música

La música utilizada en este proyecto está licenciada y pertenece al siguiente artista:
- **Canción**: I’m Just Ken
- **Artista**: Ryan Gosling

¡Diviértete jugando!
