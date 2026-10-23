"""
Ticket 1 - Los datos del cliente
Script: generar_datos.py

Genera un archivo CSV simulado con ventas de la Heladería La Esquina (Itagüí).
Crea 100 filas con 8 columnas e incluye al menos 5 filas dañadas a propósito:
- un valor vacío,
- un texto donde va un número,
- una fecha mal escrita.

Usa solo la librería estándar de Python (csv, random, datetime).
El archivo se guarda en datos/registros.csv.
"""

import csv
import random
from datetime import datetime, timedelta

# Configuración del negocio
NOMBRE_CLIENTE = "Heladería La Esquina"
CIUDAD = "Itagüí"
NUM_FILAS = 100
NUM_FILAS_DAÑADAS = 5
ARCHIVO_SALIDA = "datos/registros.csv"

# Datos posibles para simular ventas
SABORES = ["Chocolate", "Vainilla", "Fresa", "Limón", "Dulce de leche", "Mora", "Maracuyá"]
TAMAÑOS = ["Pequeno", "Mediano", "Grande"]
MEDIOS_PAGO = ["Efectivo", "Tarjeta", "Nequi", "Daviplata"]
ESTADOS = ["Completada", "Completada", "Completada", "Cancelada", "Devuelta"]

# Fecha base: un mes de ventas (octubre 2026)
FECHA_INICIO = datetime(2026, 10, 1)


def generar_fecha_aleatoria():
    """Devuelve una fecha aleatoria dentro del mes de octubre 2026."""
    dias_aleatorios = random.randint(0, 30)
    return FECHA_INICIO + timedelta(days=dias_aleatorios)


def generar_fila_valida(id_venta):
    """Crea una fila de datos válida y completa."""
    fecha = generar_fecha_aleatoria().strftime("%Y-%m-%d")
    sabor = random.choice(SABORES)
    tamaño = random.choice(TAMAÑOS)
    cantidad = random.randint(1, 5)
    valor_unitario = random.choice([4500, 5500, 6500, 7500, 8500])
    valor = cantidad * valor_unitario
    medio_pago = random.choice(MEDIOS_PAGO)
    estado = random.choice(ESTADOS)
    return [id_venta, fecha, sabor, tamaño, cantidad, valor, medio_pago, estado]


def generar_fila_dañada(tipo, id_venta):
    """
    Crea una fila dañada a propósito según el tipo:
    1 - valor vacío
    2 - texto donde va un número
    3 - fecha mal escrita
    """
    fecha = generar_fecha_aleatoria().strftime("%Y-%m-%d")
    sabor = random.choice(SABORES)
    tamaño = random.choice(TAMAÑOS)
    medio_pago = random.choice(MEDIOS_PAGO)
    estado = random.choice(ESTADOS)

    if tipo == 1:
        # Valor vacío
        return [id_venta, fecha, sabor, tamaño, 1, "", medio_pago, estado]
    elif tipo == 2:
        # Texto donde va un número (valor no numérico)
        return [id_venta, fecha, sabor, tamaño, 1, "mucho", medio_pago, estado]
    elif tipo == 3:
        # Fecha mal escrita
        return [id_venta, "23/13/2026", sabor, tamaño, 1, 5500, medio_pago, estado]
    else:
        # Valor y fecha dañados juntos
        return [id_venta, "fecha-invalida", sabor, tamaño, 1, "", medio_pago, estado]


def main():
    """Genera el archivo CSV con datos válidos y dañados."""
    import os

    # Asegurar que la carpeta datos/ exista
    os.makedirs("datos", exist_ok=True)

    columnas = [
        "id", "fecha", "sabor", "tamaño", "cantidad",
        "valor", "medio_de_pago", "estado"
    ]

    filas = []

    # Generar filas válidas
    for i in range(1, NUM_FILAS - NUM_FILAS_DAÑADAS + 1):
        filas.append(generar_fila_valida(i))

    # Generar filas dañadas a propósito
    tipos_dano = [1, 2, 3, 1, 2]  # 5 filas dañadas: 2 vacías, 2 texto, 1 fecha
    for j, tipo in enumerate(tipos_dano):
        id_venta = NUM_FILAS - NUM_FILAS_DAÑADAS + j + 1
        filas.append(generar_fila_dañada(tipo, id_venta))

    # Mezclar un poco las filas para que las dañadas no estén todas al final
    random.shuffle(filas)

    # Escribir el archivo CSV
    with open(ARCHIVO_SALIDA, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(columnas)
        escritor.writerows(filas)

    print(f"Archivo generado: {ARCHIVO_SALIDA}")
    print(f"Total de filas: {len(filas)} (incluye {NUM_FILAS_DAÑADAS} filas dañadas)")


if __name__ == "__main__":
    main()
