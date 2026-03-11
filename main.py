import random
import time

from variables import POSICIONES_JUGADOR, POSICIONES_SISTEMA
from funciones import Tablero, solicitar_coordenadas, limpiar_pantalla, dibujar_tableros, mostrar_vidas

print("--- BIENVENIDO A HUNDIR LA FLOTA ---")

jugador = Tablero(POSICIONES_JUGADOR)
sistema = Tablero(POSICIONES_SISTEMA)

while True:
    # --- TURNO DEL JUGADOR ---
    while True:
        limpiar_pantalla()
        dibujar_tableros(jugador, sistema)
        mostrar_vidas(jugador, sistema)
        
        print(f"\n--- ⚔️ TURNO DEL JUGADOR ⚔️ ---")
        coordenada = solicitar_coordenadas()
        
        if coordenada is None: break
            
        fila, columna = coordenada
        resultado = sistema.recibir_disparo(fila, columna)
        
        if sistema.vidas == 0 or resultado == "FALLO": break  # Si es "TOCADO" o "REPETIDO", el bucle continúa automáticamente

    if sistema.vidas == 0 or coordenada is None: break 

    # --- TURNO DEL SISTEMA ---
    while True:
        limpiar_pantalla()
        dibujar_tableros(jugador, sistema)
        mostrar_vidas(jugador, sistema)

        print(f"\n--- 🛡️ TURNO DEL SISTEMA 🛡️ ---")
        time.sleep(3) 
       
        fila_sistema, columna_sistema = random.randint(0, 9), random.randint(0, 9)
        resultado_sistema = jugador.recibir_disparo(fila_sistema, columna_sistema)
        
        if jugador.vidas == 0 or resultado_sistema == "FALLO": break
        # Si el sistema acierta, el 'while' repite la jugada

    if jugador.vidas == 0: break

# --- FINAL DEL JUEGO ---
limpiar_pantalla()
dibujar_tableros(jugador, sistema)
mostrar_vidas(jugador, sistema)
if sistema.vidas == 0: print("\n🎉 ¡VICTORIA! Flota enemiga hundida 🎉")
elif jugador.vidas == 0: print("\n🛟 DERROTA... Tu flota ha sido destruida 🛟")
else: print("\n🏳️ Te has rendido 🏳️")
input("\nPresiona ENTER para salir del juego...")