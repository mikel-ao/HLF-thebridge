import numpy as np
import time
import os
import subprocess
from variables import DIMENSIONES, BARCO, AGUA, TOCADO, FALLO, VIDAS_TOTALES, LETRAS, POSICIONES_JUGADOR, POSICIONES_SISTEMA

class Tablero:
    def __init__(self, coordenadas_barcos):
        self.tablero = np.full(DIMENSIONES, AGUA)  
        self.vidas = VIDAS_TOTALES # Suma de todas las vidas (19)
        for coordenadas in coordenadas_barcos.values():   # Accedemos a los valores del diccionario que son listas de tuplas
            for fila, columna in coordenadas:           # Accedemos a las tuplas
                self.tablero[fila, columna] = BARCO     # en cada coordenada de cada tupla ponemos un "B"

    def recibir_disparo(self, fila, columna):
        objetivo = self.tablero[fila, columna]
        
        if objetivo == BARCO:
            self.tablero[fila, columna] = TOCADO
            self.vidas -= 1
            print("💥 ¡TOCADO! 💥")
            time.sleep(3)
            return "TOCADO"
            
        elif objetivo == AGUA:
            self.tablero[fila, columna] = FALLO
            print("💦 Agua 💦")
            time.sleep(3)
            return "FALLO"
        
        print("🤬 ¡Esa posición ya había sido atacada! 🤬")
        time.sleep(3)
        
def solicitar_coordenadas():
    while True:
        entrada = input("Introduce coordenada 🗺️ (ej: A5) o 'S' para salir: ").upper().strip()
        
        if entrada == "S": return None                                                      # Transcripción de coordendas del juego (A1) a indices numpy (00)
                                                                                        
        if len(entrada) >= 2 and entrada[0] in LETRAS and entrada[1:].isdigit():        # la entrada tiene que tener un len igual o mayor de 2. el primer elemento es una letra y el segundo un número
            fila = LETRAS.find(entrada[0])      # la letra tiene que existir en el string LETRAS                            
            columna = int(entrada[1:]) - 1      # la parte numérica del imput se convierte a int y se le resta 1 para convertir de coordenada del juego a coordenada numpy
            
            if 0 <= fila < 10 and 0 <= columna < 10:        # comprobamos que las coordenadas numpy están dentro del rango
                return fila, columna
        
            print("❌ Error: Introduce una letra (A-J) y un número (1-10). Ej: B3 ❌")
            
def limpiar_pantalla():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    
def dibujar_tableros(jugador, sistema):
    
    separador_horizontal = "   " + "__" * 20
    
   
    print(f"\n{'FLOTA JUGADOR':^40} {'FLOTA SISTEMA':^60}")
    
    nums = "    " + "   ".join(map(str, range(1, 11)))      
    print(f"{nums}       {nums}\n{separador_horizontal}      {separador_horizontal}")

    for i in range(10):
        fila_jugador = f"{LETRAS[i]} | {' | '.join(jugador.tablero[i])} |"      #tablero jugador por filas (i)
        fila_sistema = f"{LETRAS[i]} | {' | '.join(celda if celda != BARCO else AGUA for celda in sistema.tablero[i])} |"       #tablero sistema por celdas, para ocultar barcos del sistema
        
        
        print(f"{fila_jugador}      {fila_sistema}\n{separador_horizontal}      {separador_horizontal}")

def mostrar_vidas(jugador, sistema):
    vidas_jugador = f"VIDAS JUGADOR: {jugador.vidas}"
    vidas_sistema = f"VIDAS SISTEMA: {sistema.vidas}"
    
    print("\n" + "=" * 105)
    
    print(f"{vidas_jugador:<40}          {vidas_sistema}")
    
    print("=" * 105 + "\n")