"""
Ticket 2 - El reporte
Archivo: reporte.py

Programa principal que lee el CSV de registros, calcula los números del mes,
cuenta las filas dañadas sin detenerse, y escribe salida/reporte.md.

En equipos de 2 o 3 no hay cargar.py, por lo que este script lee el CSV directamente
y conecta con la función crear_grafica() de grafica.py.

Uso:
    python reporte.py
"""

import csv
import os
from grafica import crear_grafica

# Rutas de archivos (se pueden cambiar fácilmente aquí, sin tocar la lógica)
ARCHIVO_DATOS = "datos/registros.csv"
CARPETA_SALIDA = "salida"
ARCHIVO_REPORTE = os.path.join(CARPETA_SALIDA, "reporte.md")
ARCHIVO_GRAFICA = os.path.join(CARPETA_SALIDA, "grafica.html")

COLUMNA_CATEGORIA = "sabor"   # columna que agrupa (ej. sabor del helado)
COLUMNA_VALOR = "valor"       # columna numérica a sumar


def leer_registros(ruta_archivo):
    """
    Lee el CSV y devuelve los registros válidos y cuántas filas se descartaron.

    Cada fila dañada se salta con try/except y se cuenta.
    El programa nunca se detiene por una fila mala.

    Retorna:
        (registros_validos, filas_descartadas): lista de diccionarios válidos y entero.
    """
    registros_validos = []
    filas_descartadas = 0

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Validar que la categoría exista y no esté vacía
                    categoria = fila[COLUMNA_CATEGORIA].strip()
                    if not categoria:
                        raise ValueError("Categoría vacía")

                    # Validar que el valor sea un número
                    valor_str = fila[COLUMNA_VALOR].strip()
                    if not valor_str:
                        raise ValueError("Valor vacío")
                    valor = float(valor_str)

                    # Validar que la fecha tenga formato razonable (contenga '-')
                    fecha = fila.get("fecha", "").strip()
                    if "-" not in fecha:
                        raise ValueError("Fecha mal escrita")

                    registros_validos.append({
                        "categoria": categoria,
                        "valor": valor,
                    })
                except (ValueError, KeyError, TypeError):
                    # Fila dañada: se salta y se cuenta
                    filas_descartadas += 1
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {ruta_archivo}")
        raise

    return registros_validos, filas_descartadas


def calcular_resumen(registros_validos):
    """
    Calcula el total y el desglose por categoría.

    Retorna:
        (total_valor, por_categoria): total numérico y lista de tuplas
        (cantidad_registros, valor_total) por categoría ordenada de mayor a menor.
    """
    total_valor = 0.0
    por_categoria = {}

    for registro in registros_validos:
        cat = registro["categoria"]
        val = registro["valor"]
        total_valor += val

        if cat not in por_categoria:
            por_categoria[cat] = {"registros": 0, "valor": 0.0}
        por_categoria[cat]["registros"] += 1
        por_categoria[cat]["valor"] += val

    # Ordenar por valor total de mayor a menor
    categorias_ordenadas = sorted(
        por_categoria.items(), key=lambda item: item[1]["valor"], reverse=True
    )

    return total_valor, categorias_ordenadas


def generar_reporte_md(fecha_generacion, filas_leidas, registros_validos,
                       filas_descartadas, total_valor, por_categoria,
                       ruta_reporte, ruta_grafica):
    """
    Escribe el archivo salida/reporte.md con el formato solicitado.

    Formato:
    # Reporte del mes: Heladería La Esquina
    Generado el: 2026-10-23
    ## Resumen
    | Dato | Valor |
    |---|---|
    | Filas leídas | 105 |
    | Registros válidos | 100 |
    | Filas descartadas | 5 |
    | Valor total | $4.350.000 |
    ## Por categoría
    | Categoría | Registros | Valor |
    |---|---|---|
    | Chocolate | 32 | $1.280.000 |
    ## Gráfica
    Ver `salida/grafica.html`
    """
    lineas = []
    lineas.append("# Reporte del mes: Heladería La Esquina")
    lineas.append(f"Generado el: {fecha_generacion}")
    lineas.append("")
    lineas.append("## Resumen")
    lineas.append("| Dato | Valor |")
    lineas.append("|---|---|")
    lineas.append(f"| Filas leídas | {filas_leidas} |")
    lineas.append(f"| Registros válidos | {len(registros_validos)} |")
    lineas.append(f"| Filas descartadas | {filas_descartadas} |")
    lineas.append(f"| Valor total | ${total_valor:,.0f} |")
    lineas.append("")
    lineas.append("## Por categoría")
    lineas.append("| Categoría | Registros | Valor |")
    lineas.append("|---|---|---|")
    for categoria, datos in por_categoria:
        lineas.append(
            f"| {categoria} | {datos['registros']} | ${datos['valor']:,.0f} |"
        )
    lineas.append("")
    lineas.append("## Gráfica")
    lineas.append(f"Ver `{ruta_grafica}`")

    with open(ruta_reporte, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas) + "\n")

    print(f"Reporte escrito en: {ruta_reporte}")


def main():
    """Ejecuta el flujo completo: leer, calcular, graficar y escribir reporte."""
    import datetime

    # 1. Leer registros del CSV
    registros_validos, filas_descartadas = leer_registros(ARCHIVO_DATOS)
    filas_leidas = len(registros_validos) + filas_descartadas

    # 2. Calcular resumen
    total_valor, por_categoria = calcular_resumen(registros_validos)

    # 3. Generar gráfica (Ticket 3)
    categorias = [cat for cat, _ in por_categoria]
    valores = [datos["valor"] for _, datos in por_categoria]
    crear_grafica(categorias, valores, ARCHIVO_GRAFICA)

    # 4. Escribir reporte.md (Ticket 2)
    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    generar_reporte_md(
        fecha_hoy,
        filas_leidas,
        registros_validos,
        filas_descartadas,
        total_valor,
        por_categoria,
        ARCHIVO_REPORTE,
        ARCHIVO_GRAFICA,
    )

    # Resumen por consola
    print(f"Filas leídas: {filas_leidas}")
    print(f"Registros válidos: {len(registros_validos)}")
    print(f"Filas descartadas: {filas_descartadas}")
    print(f"Valor total: ${total_valor:,.0f}")
    print("Reporte generado correctamente.")


if __name__ == "__main__":
    main()
